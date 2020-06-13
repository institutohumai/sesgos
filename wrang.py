import os
import pandas as pd
import json
import re
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# lista con todos los nombres de archivos
txts = [r'./data/' + f for f in os.listdir('./data') if f.endswith('.json') and '2020-06-13_04-11-17.json' in f]


for txt in txts:
    with open(txt, 'rb') as inp:
        j = json.loads(inp.read())
    d = pd.read_json(j)
