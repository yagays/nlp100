#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

with open("output/neko.txt.mecab.pkl", "rb") as f:
    docs = pickle.load(f)

output = []
for d in docs:
    candidate = []
    for morpheme in d:
        if len(candidate) == 0 and morpheme["pos"] == "名詞":
            candidate.append(morpheme)
        elif len(candidate) == 1 and morpheme["surface"] == "の":
            candidate.append(morpheme)
        elif len(candidate) == 2 and morpheme["pos"] == "名詞":
            candidate.append(morpheme)
            output.append("".join([w["surface"] for w in candidate]))
            candidate = []
        else:
            candidate = []
