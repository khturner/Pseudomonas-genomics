#!/bin/bash

# Compile single faa from proteomes of Pseudomonas strains, removing excess stuff from headers
cat faa/Pseudomonas*faa | sed 's/\\*//g' |
for strain in `ls faa | grep '^Pseudomonas' | sed 's/\\.faa//g'`
do
  cat faa/$strain.faa | sed "s/>/>${strain}_-_/g" | awk '{print $1}' >> faa/proteome.faa
done

# Run uclust
usearch -cluster_fast faa/proteome.faa -sort length -id 0.75 -uc uc/results.id75.uc
