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
word_freq_top10 = word_freq_sorted[:10]

label = [w[0] for w in word_freq_top10]
left = range(10)
height = [w[1] for w in word_freq_top10]
plt.bar(left, height, tick_label=label)
plt.title("頻度上位10語")
plt.xlabel("単語")
plt.ylabel("出現頻度")
plt.savefig("output/37.png")
