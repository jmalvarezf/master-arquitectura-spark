# coding: utf-8

import socket, time, csv, urllib, io, os, logging
print("Started...")
import urllib.request

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = urllib.request.urlopen(url)
try:
    os.makedirs("./training")
except:
    logging.info("Directory exists, continuing")

remote_file = csv.reader(io.TextIOWrapper(data), delimiter=";")
i = 0
j = 0
for row in remote_file:
  if i == 0:
     i += 1
     f = open("./training/data_training_" +str(i) + ".csv",'w')
     continue
  print(row)
  if i%5 == 0:
     time.sleep(1.0)
     f.close();
     j += 1
     f = open("./training/data_training_" +str(j) + ".csv",'w')
  row.append("wine" + str(i))
  f.write(";".join(row)+"\n") #Give your csv text here.
  i+=1
f.close()
