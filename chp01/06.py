#!/usr/bin/env python
# -*- coding: utf-8 -*-


def c_ngram(s):
    char = list(s)
    return ["".join(c) for c in list(zip(char, char[1:]))]


X = set(c_ngram("paraparaparadise"))
Y = set(c_ngram("paragraph"))

print("和集合: ", X | Y)
print("積集合: ", X & Y)
print("差集合: ", X - Y)
print("'se' in X: ", "se" in X)
print("'se' in Y: ", "se" in Y)
