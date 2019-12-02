import json
import csv
import pandas as pd

df=pd.read_json('remotes_mod.json')
df.to_csv("test.csv")


