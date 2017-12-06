#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def typoglycemia(sentence):
    output = []
    for token in sentence.split(" "):
        if len(token) <= 4:
            output.append(token)
        else:
            s = list(token[1:-1])
            random.shuffle(s)
            output.append(token[0] + "".join(s) + token[-1])
    return " ".join(output)

query = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(typoglycemia(query))
