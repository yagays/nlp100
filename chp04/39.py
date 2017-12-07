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
plt.scatter(range(len(word_freq_sorted)),
            [w[1] for w in word_freq_sorted])
plt.xlim(1, len(word_freq_sorted))
plt.ylim(1, word_freq_sorted[0][1])
plt.xscale("log")
plt.yscale("log")
plt.title("Zipfの法則")
plt.xlabel("単語の出現頻度順位")
plt.ylabel("出現頻度")
plt.savefig("output/39.png")
