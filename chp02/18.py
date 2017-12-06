#!/usr/bin/env python
# -*- coding: utf-8 -*-

col = []
with open("data/hightemp.txt") as f:
    for line in f:
        l = line.rstrip().split("\t")
        col.append(l)

sorted_col = sorted(col, key=lambda x: x[2], reverse=True)
for c in sorted_col:
    print("\t".join(c))
