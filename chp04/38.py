#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from collections import defaultdict
import matplotlib.pyplot as plt

with open("output/neko.txt.mecab.pkl", "rb") as f:
    docs = pickle.load(f)

word_freq = defaultdict(lambda: 0)
for d in docs:
    candidate = []
    for morpheme in d:
        word_freq[morpheme["surface"]] += 1

word_freq_sorted = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
plt.hist([w[1] for w in word_freq_sorted], bins=100, range=(0,100), width=1.0)
plt.xlim(xmin=1, xmax=100)
plt.title("単語の出現頻度のヒストグラム")
plt.xlabel("出現頻度")
plt.ylabel("出現頻度をとる単語の種類数")
plt.savefig("output/38.png")
