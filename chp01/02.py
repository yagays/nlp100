#!/usr/bin/env python
# -*- coding: utf-8 -*-

s1 = "パトカー"
s2 = "タクシー"

print("".join([s[0] + s[1] for s in zip(s1, s2)]))
