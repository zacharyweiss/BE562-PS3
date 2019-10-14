"""
Zachary Weiss
13 Oct 2019
Gibb's Sampling for BE562
"""
import sys
import numpy as np

alphabet = ['A', 'G', 'C', 'T']
max_thresh = 0.78
itera_thresh = 200


#  S - list of sequences
#  L - length of motif
#  PFM - 4xL list with frequencies of each base at each position
def gibbs_sampler(S, L):
    # number of strings
    s_n = len(S)

    converged = False
    inits = 0
    while not converged:
        inits += 1
        # choose a substring of length L from each S1,...St #
        substrings = [None] * s_n
        for i, S_i in enumerate(S):
            ind = np.random.randint(0, len(S_i) - L)
            substrings[i] = S_i[ind:ind + L]

        # initialize PFM #
        PFM = [[0.0] * L for i in range(len(alphabet))]
        for i in range(L):
            for s in substrings:
                PFM[alphabet.index(s[i])][i] += 1 / s_n

        # while not converged do #
        itera = 0
        Sc_i = -1  # placeholder index of current sequence
        while not converged and itera < itera_thresh:
            # choose a sequence at random, Sc #
            ind = np.random.randint(0, s_n)
            while ind == Sc_i:
                ind = np.random.randint(0, s_n)
            Sc_i = ind
            Sc = S[Sc_i]

            # score all substrings of length L from Sc using the PFM #
            score = [1] * (len(Sc) - L)
            # score = [0] * (len(Sc) - L)
            for i in range(len(Sc) - L):
                for j in range(L):
                    score[i] *= PFM[alphabet.index(Sc[i + j])][j]
                    # score[i] += np.log(PFM[alphabet.index(Sc[i + j])][j] + 1)

            # stochastically choose a new substring from Sc with a probability proportional to its score #
            denom = sum(score)
            subs_prob = [a/denom for a in score]
            Sc_sub_ind = np.argmax(np.random.multinomial(1, subs_prob))
            substrings[Sc_i] = S[Sc_i][Sc_sub_ind:Sc_sub_ind+L]

            # update PFM
            PFM = [[0.0] * L for i in range(len(alphabet))]
            for i in range(L):
                for s in substrings:
                    PFM[alphabet.index(s[i])][i] += 1 / s_n

            max_prob = [np.max(a) for a in np.array(PFM).T.tolist()]
            avg_max_prob = np.average(max_prob)
            if not (itera % 10):
                print("{:d}: {:5.3f} {:5.3f} {:5.3f}".format(inits, avg_max_prob, max(max_prob), min(max_prob)))

            itera += 1
            if avg_max_prob > max_thresh:
                converged = True
                print("\n{:5.3f} {:5.3f} {:5.3f}".format(avg_max_prob, max(max_prob), min(max_prob)))
                print("Inits@converge: " + str(inits))
                print("Iter@converge: " + str(itera) + "\n")


    # return chosen substrings, PFM #
    return substrings, PFM


def print_motif(PFM, subs, L):
    motif = [None] * L
    for i in range(L):
        max_ind = np.argmax([a[i] for a in PFM])
        motif[i] = alphabet[max_ind] if PFM[max_ind][i] >= 0.7 else "_"
    motif = ''.join(motif)

    print("Motif: " + motif)
    for s in subs:
        print(s)

    # Prints the PFM in a pretty format, with one row for each base and each
    # column is the probability distribution for that position in the motif
    print("\n    " + " ".join(["{:<5d}".format(i) for i in list(range(1, L + 1))]))
    for j in range(len(alphabet)):
        print(" {0}  ".format(alphabet[j]) +
              " ".join(["{:5.3f}".format(p) for p in PFM[j]]))


def read_data(file):
    data = []
    with open(file, "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def main():
    if len(sys.argv) < 3:
        print("Usage: {0} <motif length> <datafile>")
        print("On a windows machine, you may need to do:")
        print("python {0} <motif length> <datafile>".format(sys.argv[0]))
        sys.exit(1)

    L = int(sys.argv[1])
    datafile = sys.argv[2]
    S = read_data(datafile)

    substrings, P = gibbs_sampler(S, L)

    print_motif(P, substrings, L)


if __name__ == "__main__":
    main()
