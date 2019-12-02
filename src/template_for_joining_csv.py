import os
import csv

# Change to path containing all the files
# Get a list of all the files
# Use double \\ to avoid escape characters
path = "/Users/jiajiaxu/PycharmProjects/JsonToCsv/homeC-generation"
os.chdir(path)
files = os.listdir()

# Create an empty list to store the csv data
mydata = list()
count = 0

# For each CSV file in the directory of interest
# Open the file and append data into the list structure
with open("FORMAT", 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        headers = row
        
for file in files:
    if file == "FORMAT":
        continue
    
    with open(file, 'r') as infile:
        data = csv.reader(infile)
        for row in data:
            mydata.append(row)
            count = count + 1

mydata = sorted(mydata)

os.chdir("/Users/jiajiaxu/PycharmProjects/JsonToCsv/homeC-generation")
with open("generation_data_all.csv", 'w', newline = '') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    for row in mydata:
         writer.writerow(row)

print(count)
