#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

col1 = defaultdict(lambda: 0)
with open("data/hightemp.txt") as f:
    for line in f:
        l = line.rstrip().split("\t")
        col1[l[0]] += 1

for c in sorted(col1.items(), key=lambda x: x[1], reverse=True):
    print(str(c[1]) + " " + c[0])
