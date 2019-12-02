import json
import csv

f = open('remote_hist_mod.json')
data = json.load(f)
f.close()

f = csv.writer(open('test.csv', 'w'))
# use encode to convert non-ASCII characters
for item in data:
    values = [ x.encode('utf8') for x in item['fields'].values() ]
    f.writerow([item['pk'], item['model']] + values)