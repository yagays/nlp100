#!/usr/bin/env python
# -*- coding: utf-8 -*-


col1 = []
col2 = []


with open("data/hightemp.txt") as f:
    for line in f:
        l = line.rstrip().split("\t")
        col1.append(l[0])
        col2.append(l[1])

with open("output/col1.txt", "w") as f:
    for c in col1:
        f.write(c + "\n")
with open("output/col2.txt", "w") as f:
    for c in col2:
        f.write(c + "\n")
