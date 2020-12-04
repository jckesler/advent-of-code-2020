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
numRows = len(lineList)
numCols = len(lineList[0].rstrip())
print('table size: ' + str(numRows) + ' rows x ' + str(numCols) + ' cols')

deltax = [1,3,5,7,1]
deltay = [1,1,1,1,2]
answer = 1

for i in range(5):
   x = 0
   y = 0
   treeCount = 0

   while y < numRows:
      if lineList[y][x] == '#':
         treeCount = treeCount + 1 
      x = x + deltax[i]
      y = y + deltay[i]
      if x >= numCols:
         x = x - numCols

   print('tree total for set ' + str(i) + ': ' + str(treeCount))
   answer = answer * treeCount

print('answer: ' + str(answer))

inFile.close()
