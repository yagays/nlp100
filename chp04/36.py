#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from collections import defaultdict

with open("output/neko.txt.mecab.pkl", "rb") as f:
    docs = pickle.load(f)

word_freq = defaultdict(lambda: 0)
for d in docs:
    candidate = []
    for morpheme in d:
        word_freq[morpheme["surface"]] += 1

print(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
