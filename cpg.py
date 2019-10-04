import numpy as np
import pandas as pd
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument()
# args = parser.parse_args()

# TRANSITION MATRICES: m_one is inside a CpG island, m_two is outside (background)
#           A      G      C      T
m_one = [[0.180, 0.426, 0.274, 0.120],  #A
         [0.161, 0.375, 0.339, 0.125],  #G
         [0.171, 0.274, 0.367, 0.188],  #C
         [0.079, 0.384, 0.355, 0.182]]  #T
#           A      G      C      T
m_two = [[0.300, 0.285, 0.205, 0.210],  #A
         [0.248, 0.298, 0.246, 0.208],  #G
         [0.322, 0.078, 0.298, 0.302],  #C
         [0.177, 0.292, 0.239, 0.292]]  #T

bases = ["A", "G", "C", "T"]

def gen_seq(trans_prob, seq_len):
    # initialize sequence of given length
    s = ["Z"]*seq_len
    # initialize first nucleotide (even probability of being any base)
    s[0] = bases[np.where(np.random.multinomial(1, [0.25, 0.25, 0.25, 0.25]))[0][0]]

    i = 1
    while i < seq_len:
        s[i] = bases[np.where(np.random.multinomial(1, trans_prob[bases.index(s[i-1])]))[0][0]]
        i += 1

    # join sequence into single string (attempting to optimize and avoid appending with each base)
    seq = ''.join(s)
    return seq


def main():
    seq = gen_seq(m_one, 15)
    print(seq)


if __name__ == "__main__":
    main()
