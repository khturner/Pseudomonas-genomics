#!/bin/bash

# Compile single faa from proteomes of Pseudomonas strains, removing excess stuff from headers
cat faa/Pseudomonas*faa | sed 's/\\*//g' |
for strain in `ls faa | grep '^Pseudomonas' | sed 's/\\.faa//g'`
do
  cat faa/$strain.faa | sed "s/>/>${strain}_-_/g" | awk '{print $1}' >> faa/proteome.faa
done

# Presort by length
usearch -sortbylength faa/proteome.faa -fastaout faa/proteome.sorted.faa

# Run uclust
usearch -cluster_smallmem faa/proteome.sorted.faa -id 0.50 -uc uc/results.id50.uc
