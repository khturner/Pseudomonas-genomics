#!/usr/bin/env python
import argparse
from math import log

parser = argparse.ArgumentParser(description = "Build a CSR representation of a sparse matrix from UCLUST results")
parser.add_argument("-i", "--input", required = True, metavar = "FILE", help = "UCLUST results file")
parser.add_argument("-n", "--numstrains", required = True, type = int, help = "Total number of strains examined")
parser.add_argument("-o", "--output", required = True, metavar = "PFX", help = "Prefix for output files")
args = parser.parse_args()

fileuc = open(args.input)
#fileout = open(args.output + ".lgl", "w")
print("# " + str(0))

clust_bytes = [fileuc.tell()] * 1000
current_i = 0
current_j = -1
i_strains = set()
j_strains = set()
byte = fileuc.tell()
line = fileuc.readline().split("\t")

# Draft algorithm:
# start at first byte, until line[1] != current i, add line[8] split "_-_"[0] to set i
# when line[1] != current i, write the LGL header out, then start up new set j, add [8] split "_-_"[1] to set j, and store the byte position in clust_bytes
# when line[1] != current j, calculate aLMI and write it out to the output LGL, reset current j to line[1], and continue
# when line[0] == C, increment i, jump back to the i position in clust_bytes, and start over

# OK this needs serious work...
while (len(line) > 1):
  if (line[0] != "C"):
    if (int(line[1]) == current_i):
      i_strains.add(line[8].split("_-_")[0])
    elif (int(line[1]) == current_j):
      j_strains.add(line[8].split("_-_")[0])
    else:
      if (len(j_strains) > 0):
        print(i_strains)
        print(j_strains)
        #lenint = len(i_strains.intersection(j_strains))
        #aLMI = lenint * log(args.numstrains * lenint / (len(i_strains)**2), 2)
        #print(str(current_j) + "\t" + aLMI)
      current_j = int(line[1])
      clust_bytes[current_j] = byte
      j_strains = set()
    byte = fileuc.tell()
    line = fileuc.readline().split("\t")
  else:
    current_i += 1
    i_strains = set()
    fileuc.seek(clust_bytes[current_i])
    current_j = -1
    byte = fileuc.tell()
    line = fileuc.readline().split("\t")
    print("# " + current_i)

