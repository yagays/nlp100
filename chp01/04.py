#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

w_1 = [i - 1 for i in [1, 5, 6, 7, 8, 9, 15, 16, 19]]
d = {}

for i, element in enumerate(s.split(" ")):
    if i in w_1:
        d[i] = element[0]
    else:
        d[i] = element[:2]
print(d)
