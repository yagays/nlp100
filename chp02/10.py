#!/usr/bin/env python
# -*- coding: utf-8 -*-

i = 0
with open("data/hightemp.txt") as f:
    for line in f:
        i += 1

print(i)
