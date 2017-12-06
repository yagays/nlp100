#!/usr/bin/env python
# -*- coding: utf-8 -*-

col1 = []
with open("data/hightemp.txt") as f:
    for line in f:
        l = line.rstrip().split("\t")
        col1.append(l[0])

print(len(set(col1)))
