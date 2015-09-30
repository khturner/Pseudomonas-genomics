#!/usr/bin/env python
from scipy.sparse import lil_matrix
import argparse

parser = argparse.ArgumentParser(description = "Build a CSR representation of a sparse matrix from UCLUST results")
parser.add_argument("-i", "--input", required = True, metavar = "FILE", help = "UCLUST results file")
parser.add_argument("-o", "--output", required = True, metavar = "PFX", help = "Prefix for output files (PFX.sm.txt - sparse matrix, PFX.cols.txt - column labels)")
args = parser.parse_args()

# read in uclust results and build sparse matrix, probably lil

