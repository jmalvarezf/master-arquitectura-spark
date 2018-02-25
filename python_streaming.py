# coding: utf-8

import socket, time, csv, urllib2
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(("localhost", 7777))
#s.listen(1)
print("Started...")
#while(1):
#  c, address = s.accept()
response = urllib2.urlopen("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv")
remote_file = csv.reader(response, delimiter=";")
i = 0
for row in remote_file:
  if i == 0:
     i+=1
     continue
  print(row)
  f = open("/home/jmalvarezf/nextcloud/Documentos/Master/Bloque_3/Spark/ejercicios_sesion3/data_ejercicio/data_"+str(i)+".csv",'w')
  f.write(";".join(row)) #Give your csv text here.
  f.close()
  time.sleep(1.0)
  i+=1
#c.close()
