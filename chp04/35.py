#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

with open("output/neko.txt.mecab.pkl", "rb") as f:
    docs = pickle.load(f)

output = set()
for d in docs:
    candidate = []
    for morpheme in d:
        if morpheme["pos"] == "名詞":
            candidate.append(morpheme)
        else:
            if len(candidate) >= 2:
                output.add("".join([w["surface"] for w in candidate]))
            candidate = []
