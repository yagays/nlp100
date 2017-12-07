#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
docs = []

with open("output/neko.txt.mecab") as f:
    sentence = []
    for line in f:
        l = line.rstrip().split("\t")
        if l[0] == "EOS":
            if sentence:
                docs.append(sentence)
                sentence = []
        else:
            mecab_output = l[1].split(",")
            morpheme = {
                "surface": l[0],
                "base": mecab_output[6],
                "pos": mecab_output[0],
                "pos1": mecab_output[1]
            }
            sentence.append(morpheme)

with open("output/neko.txt.mecab.pkl", "wb") as f:
    pickle.dump(docs, f)
