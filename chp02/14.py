#!/usr/bin/env python
# -*- coding: utf-8 -*-


def head(n):
    with open("data/hightemp.txt") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            print(line.rstrip())


head(3)
