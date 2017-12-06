#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tail(n):
    l = []
    with open("data/hightemp.txt") as f:
        for i, line in enumerate(f):
            l.append(line.rstrip())
    for p in l[-n:]:
        print(p)

tail(3)
