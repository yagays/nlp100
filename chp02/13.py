#!/usr/bin/env python
# -*- coding: utf-8 -*-

col1 = []
col2 = []

with open("output/col1.txt") as f:
    for line in f:
        col1.append(line.rstrip())

with open("output/col2.txt") as f:
    for line in f:
        col2.append(line.rstrip())

with open("output/col_merge.txt", "w") as f:
    for line in zip(col1, col2):
        f.write("\t".join(line) + "\n")
