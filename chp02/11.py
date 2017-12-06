#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open("data/hightemp.txt") as f:
    for line in f:
        print(line.rstrip().replace("\t", " "))
