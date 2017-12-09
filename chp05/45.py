#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from collections import defaultdict


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

    def phrase(self):
        return "".join([m.surface for m in self.morphs])

    def phrase_wo_mark(self):
        output = ""
        for m in self.morphs:
            if m.pos != "記号":
                output += m.surface
        return output

    def include_noun(self):
        return "名詞" in [m.pos for m in self.morphs]

    def include_verb(self):
        return "動詞" in [m.pos for m in self.morphs]

    def include_particle(self):
        return "助詞" in [m.pos for m in self.morphs]

    def particle_list(self):
        output = []
        for m in self.morphs:
            if m.pos == "助詞":
                output.append(m.surface)
        return output

    def first_verb_base(self):
        for m in self.morphs:
            if m.pos == "動詞":
                return m.base

    def __repr__(self):
        return "str:{}, dst:{}, srcs[{}]".format(self.phrase(),
                                                 self.dst,
                                                 ", ".join([str(i) for i in self.srcs]))


with open("output/neko.txt.cabocha.pkl", "rb") as f:
    doc = pickle.load(f)

doc_pattern = []
for sentence in doc:
    pattern = defaultdict(list)
    for chunk in sentence:
        if not chunk.srcs:
            continue

        for i in chunk.srcs:
            source_chunk = sentence[i]
            target_chunk = chunk

            if chunk.include_verb() and source_chunk.include_particle():
                for particle in source_chunk.particle_list():
                    pattern[target_chunk.first_verb_base()].append(particle)

    doc_pattern.append(pattern)

with open("output/45.txt", "w") as f:
    for pattern in doc_pattern:
        for verb, particle in pattern.items():
            f.write(verb + "\t" + " ".join(sorted(particle)) + "\n")
