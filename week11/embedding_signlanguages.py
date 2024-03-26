import sys
sys.path.append('../')

from utilities import get_embedding

import json
import os

embeddings = {}

filepath = '../signlanguages'

for f in os.listdir(filepath):
    path = os.path.join(filepath, f)
    with open(path, 'r', encoding="utf8", errors='ignore') as f:
        text = f.read()

    embeddings[path] = get_embedding(text)

with open('embeddings.json', 'w+') as f:
    json.dump(embeddings, f)