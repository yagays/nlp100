#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re

with open("data/jawiki-country.json") as f:
    for line in f:
        jawiki = json.loads(line)
        if jawiki["title"] == "イギリス":
            uk = jawiki["text"]

for line in uk.split("\n"):
    section = re.match(r"^[=]+(.*?)[=]+", line)
    if section:
        print(section.group(1), int(list(section.group(0)).count("=")/2))
