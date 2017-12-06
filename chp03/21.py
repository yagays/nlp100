#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

with open("data/jawiki-country.json") as f:
    for line in f:
        jawiki = json.loads(line)
        if jawiki["title"] == "イギリス":
            uk = jawiki["text"]

for line in uk.split("\n"):
    if "Category" in line:
        print(line)
