#!/usr/bin/python

import os
import sys

if len(sys.argv) < 2:
   print('syntax: ' + sys.argv[0] + ' <filename>')
   sys.exit()

filename = sys.argv[1]

inFile = open(filename, 'rb')
print('reading ' + filename)
lineList = inFile.readlines()
lineCount = len(lineList)

for i in range(lineCount):
   x = int(lineList[i])
   for j in range(lineCount):
      if i != j:
         y = int(lineList[j])
         for k in range(lineCount):
            if (i != k) and (j != k):
               z = int(lineList[k])
               sum = x + y + z
               if sum == 2020:
                  mult = x * y * z
                  print('solution: ' + str(x) + '*' + str(y) + '*' + str(z) + '=' + str(mult))

print(str(lineCount) + ' lines read')   

inFile.close()
