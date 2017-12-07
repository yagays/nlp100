#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

with open("output/neko.txt.mecab.pkl", "rb") as f:
    docs = pickle.load(f)

s = set()
for d in docs:
    for morpheme in d:
        if morpheme["pos"] == "動詞":
            s.add(morpheme["surface"])
