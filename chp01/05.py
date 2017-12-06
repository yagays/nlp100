#!/usr/bin/env python
# -*- coding: utf-8 -*-

def w_ngram(s):
    token = s.split(" ")
    return ["_".join(w) for w in list(zip(token, token[1:]))]

def c_ngram(s):
    char = list(s)
    return ["".join(c) for c in list(zip(char, char[1:]))]


s = "I am an NLPer"
print(w_ngram(s))
print(c_ngram(s))
