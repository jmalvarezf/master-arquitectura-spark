# coding: utf-8

import socket, time, csv, urllib, io
print("Started...")
import urllib.request

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
data = urllib.request.urlopen(url)

remote_file = csv.reader(io.TextIOWrapper(data), delimiter=";")
i = 0
for row in remote_file:
  if i == 0:
     i+=1
     continue
  print(row)
  f = open("./data/data_"+str(i)+".csv",'w')
  row.append("wine" + str(i))
  f.write(";".join(row)) #Give your csv text here.
  f.close()
  time.sleep(1.0)
  i+=1
