#!/usr/bin/env python
"""Skeleton code for Gibb's sampling

Guide
"""
import sys
#### Any additional imports
# optional - import any libraries you need
#   (but don't use a library that implements Gibb's sampling for you!)

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
    PFM = [ [0.0] * L for i in range(len(alphabet)) ]

    ######### ADD YOUR CODE HERE ######

    ######### END OF YOUR CODE HERE #####

    return PFM


###### YOUR OWN FUNCTIONS HERE
# optional -- feel free to add any helper functions to make your code
#             more manageable

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
    print("    " + " ".join(["{:<5d}".format(i) for i in list(range(1, L+1))]))

    for j in xrange(len(alphabet)):
        print(" {0}  ".format(alphabet[j]) +
              " ".join(["{:5.3f}".format(p) for p in P[j]]))

if __name__ == "__main__":
    main()
