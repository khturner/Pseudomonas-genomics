#!/bin/bash
for url in `tail -n +2 $1 | awk -F "\t" '{print $19 "/" $23}'`
do
wget $url
done
