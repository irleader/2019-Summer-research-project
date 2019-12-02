import json
import csv

x=open("/Users/jiajiaxu/PycharmProjects/JsonToCsv/bruny_island_raw/remote_hist_mod_summer.json","r")
x=json.load(x)

for i in range(32):
    if i==11:
        continue
    x1=x["cust_{0}".format(str(i))]['householdHist']
    f=csv.writer(open("cust{0}_{1}.csv".format(str(i),'ai'),"w"))
    f.writerow(["timestamp","power"])
    for a in x1:
        f.writerow([a[0],a[1]])

for i in range(32):
    if i==11:
        continue
    x2=x["cust_{0}".format(str(i))]['pvHist']
    f=csv.writer(open("cust{0}_{1}.csv".format(str(i),'rij'),"w"))
    f.writerow(["timestamp","power"])
    for b in x2:
        f.writerow([b[0],b[1]])

