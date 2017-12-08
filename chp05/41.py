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


class Chunk():
    def __init__(self, morphs=[], dst=0, srcs=[]):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def add_morph(self, m):
        self.morphs.append(m)

    def add_src(self, i):
        self.srcs.append(i)

    def __repr__(self):
        return "str:{}, dst:{}, srcs[{}]".format("".join([m.surface for m in self.morphs]),
                                                 self.dst,
                                                 ", ".join([str(i) for i in self.srcs]))


doc = []
with open("output/neko.txt.cabocha") as f:
    sentence = []
    for line in f:
        l = line.rstrip().split("\t")
        if l[0][0] == "*":
            c = l[0].split(" ")
            sentence.append(Chunk([], int(c[2].replace("D", "")), []))
        elif l[0] == "EOS":
            if sentence:
                for i, chunk in enumerate(sentence):
                    if chunk.dst == -1:
                        continue
                    sentence[chunk.dst].add_src(i)
                doc.append(sentence)
                sentence = []
        else:
            cabocha_output = l[1].split(",")
            m = Morph(l[0],
                      cabocha_output[6],
                      cabocha_output[0],
                      cabocha_output[1])
            sentence[-1].add_morph(m)

print(doc[7])
