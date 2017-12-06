#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re

def remove_markup(s):
    s = s.replace("'''''","").replace("'''","")
    s = re.sub(r'\[\[(.*?)\]\]', "", s)
    return s

with open("data/jawiki-country.json") as f:
    for line in f:
        jawiki = json.loads(line)
        if jawiki["title"] == "イギリス":
            uk = jawiki["text"]

d = {}
for line in uk.split("\n"):
    bs = re.match(r"^\|(.*?) = (.*?)$", line)
    if bs:
        d[bs.group(1)] = remove_markup(bs.group(2))

for k,v in d.items():
    print(k,v)
