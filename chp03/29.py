#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import urllib.request

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

file_name = d["国旗画像"].replace(" ", "_")
url = "https://www.mediawiki.org/w/api.php" + \
    "?action=query&format=json&prop=imageinfo&iiprop=url&titles=File:{}".format(file_name)

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode('utf8'))
    print(data["query"]["pages"]["-1"]["imageinfo"][0]["url"])
