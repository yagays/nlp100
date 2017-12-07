#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

with open("output/neko.txt.mecab.pkl", "rb") as f:
    docs = pickle.load(f)

s = set()
for d in docs:
    for morpheme in d:
        if morpheme["pos1"] == "サ変接続" and morpheme["pos"] == "名詞":
            s.add(morpheme["surface"])
