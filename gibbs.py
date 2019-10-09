#!/usr/bin/env python
"""Skeleton code for Gibb's sampling

Guide
"""
import sys
#### Any additional imports
import numpy as np

#### End additional imports

try:
    xrange
except NameError:
    xrange = range  # support both Python 2 and 3

#### INSTRUCTIONS FOR USE:
# call program as follows: ./gibbs.py <Motif Length> <Data File>
# make sure the gibbs.py is marked as executable: chmod +x gibbs.py

alphabet = ['A', 'G', 'C', 'T']


#### GibbsSampler:
####  INPUTS: S - list of sequences
####          L - length of motif
####  OUTPUT: PFM - 4xL list with frequencies of each base at each position
####                Order of bases should be consistent with alphabet variable
def GibbsSampler(S, L):
    PFM = [[0.0] * L for i in range(len(alphabet))]

    ######### ADD YOUR CODE HERE ######
    score = 0
    score_new = 0
    score_thresh = 0.05
    itera = 0
    itera_thresh = 1000
    # max_score = L*len(S)

    # choose a substring of length L from each S1,...St #
    substrings = [None] * len(S)
    for i, S_i in enumerate(S):
        ind = np.random.randint(0, len(S_i) - L)
        substrings[i] = S_i[ind:ind + L]
    subs_len = len(substrings)

    # initialize PFM #
    for i in range(L):
        for s in substrings:
            PFM[alphabet.index(s[i])][i] += 1 / (subs_len * L)

    # while not converged do #
    converged = False
    while not converged:
        subs_old = substrings

        # choose a sequence at random, Sc #
        Sc = choose_sc()

        # score all substrings of length L from Sc using the PFM #
        # stochastically choose a new substring from Sc with a probability proportional to its score #



        itera += 1
        if (abs(score - score_new) < score_thresh) or (itera > itera_thresh):
            converged = True
        score = score_new

    ######### END OF YOUR CODE HERE #####
    # return chosen substrings, PFM #
    return substrings, PFM


###### YOUR OWN FUNCTIONS HERE
def choose_sc():
    Sc = 0
    return Sc

def choose_subs(subs_old, subs):


def score_subs(subs_old, subs):
    score = 0
    return score

###### END OF YOUR FUNCTIONS

def readdata(file):
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
    S = readdata(datafile)

    P = GibbsSampler(S, L)

    # Prints the PFM in a pretty format, with one row for each base and each
    # column is the probability distribution for that position in the motif
    print("    " + " ".join(["{:<5d}".format(i) for i in list(range(1, L + 1))]))

    for j in range(len(alphabet)):
        print(" {0}  ".format(alphabet[j]) +
              " ".join(["{:5.3f}".format(p) for p in P[j]]))


if __name__ == "__main__":
    main()
