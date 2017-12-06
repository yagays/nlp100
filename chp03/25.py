#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re

with open("data/jawiki-country.json") as f:
    for line in f:
        jawiki = json.loads(line)
        if jawiki["title"] == "イギリス":
            uk = jawiki["text"]

d = {}
for line in uk.split("\n"):
    bs = re.match(r"^\|(.*?) = (.*?)$", line)
    if bs:
        d[bs.group(1)] = bs.group(2)

for k,v in d.items():
    print(k,v)
