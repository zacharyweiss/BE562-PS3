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

def main():



if __name__ == "__main__":
    main()
