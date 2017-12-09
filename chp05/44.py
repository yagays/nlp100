#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import pydot


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

    def __repr__(self):
        return "str:{}, dst:{}, srcs[{}]".format(self.phrase(),
                                                 self.dst,
                                                 ", ".join([str(i) for i in self.srcs]))


with open("output/neko.txt.cabocha.pkl", "rb") as f:
    doc = pickle.load(f)


def dependency_tree(sentence, filename="output/44.png"):
    edge = []
    for chunk in sentence:
        if not chunk.srcs:
            continue

        for i in chunk.srcs:
            source_chunk = sentence[i]
            target_chunk = chunk

            if source_chunk.phrase_wo_mark() and target_chunk.phrase_wo_mark():
                edge.append([source_chunk.phrase_wo_mark(), target_chunk.phrase_wo_mark()])
    graph = pydot.graph_from_edges(edge)
    graph.write_png(filename)

dependency_tree(doc[3])
