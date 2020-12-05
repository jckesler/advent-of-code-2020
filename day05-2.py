#!/usr/local/bin/python3

import re
import sys

if len(sys.argv) < 2:
   print('syntax: ' + sys.argv[0] + ' <filename>')
   sys.exit()

filename = sys.argv[1]

inFile = open(filename, 'r')
print('reading ' + filename)
lineList = inFile.readlines()
inFile.close()

maxSeatId = 0
lineCount = len(lineList)
numRows = 128
numSeatsPerRow = 8
totalSeats = numRows * numSeatsPerRow
seatStatus = [0] * totalSeats
for i in range(lineCount):
   lineList[i] = lineList[i].strip()
   rowStr = lineList[i][0:7]
   colStr = lineList[i][7:10]
   print(rowStr, colStr)
   translateTable = rowStr.maketrans('BF', '10')
   rowBin = rowStr.translate(translateTable) 
   translateTable = colStr.maketrans('RL', '10')
   colBin = colStr.translate(translateTable) 
   print(rowBin, colBin)
   if (len(rowBin) == 7) and (len(colBin) == 3):
      rowInt = int(rowBin, 2)
      colInt = int(colBin, 2)
      print('row ' + str(rowInt) + ' col ' + str(colInt))
      seatId = (rowInt * 8) + colInt
      print('** seat id ' + str(seatId))
      if seatId > maxSeatId:
         maxSeatId = seatId
      seatStatus[seatId] = 1

print('total number of tickets: ' + str(lineCount))
print('maximum seat id: ' + str(maxSeatId))

for i in range(maxSeatId):
   if seatStatus[i] == 0:
      if (seatStatus[i - 1] == 1) and (seatStatus[i + 1] == 1):
         print('your seat id is ' + str(i))
