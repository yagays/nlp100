#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Morph():
    def __init__(self, surface="", base="", pos="", pos1=""):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return "<{},{},{},{}>".format(self.surface, self.base, self.pos, self.pos1)


doc = []
with open("output/neko.txt.cabocha") as f:
    sentence = []
    for line in f:
        l = line.rstrip().split("\t")
        if l[0][0] == "*":
            continue
        if l[0] == "EOS":
            if sentence:
                doc.append(sentence)
                sentence = []
        else:
            cabocha_output = l[1].split(",")
            m = Morph(l[0],
                      cabocha_output[6],
                      cabocha_output[0],
                      cabocha_output[1])
            sentence.append(m)

print(doc[2])
