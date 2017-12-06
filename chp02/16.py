#!/usr/bin/env python
# -*- coding: utf-8 -*-


def split_line(n):
    l = []
    with open("data/hightemp.txt") as f:
        for i, line in enumerate(f):
            l.append(line)
    i = 0
    while l:
        with open("output/py" + str(i), "w") as f:
            f.write("".join(l[:n]))
        l = l[n:]
        i += 1


split_line(2)
