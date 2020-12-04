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
treeCount = 0
print('table size: ' + str(numRows) + ' rows x ' + str(numCols) + ' cols')

x = 0
y = 0
deltax = 3
deltay = 1

while y < numRows:
   if lineList[y][x] == '#':
      treeCount = treeCount + 1 
   print('row ' + str(y) + ' col ' + str(x) + ': ' + lineList[y][x]) + ' tree count: ' + str(treeCount)
   x = x + deltax
   y = y + deltay
   if x >= numCols:
      x = x - numCols

print('tree total: ' + str(treeCount))

inFile.close()
