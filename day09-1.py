#!/usr/local/bin/python3

import sys

if len(sys.argv) < 3:
   print('syntax: ' + sys.argv[0] + ' <filename> <blocksize>')
   sys.exit()

filename = sys.argv[1]
blockSize = int(sys.argv[2])

inFile = open(filename, 'r')
print('reading ' + filename)
lineList = inFile.readlines()
lineCount = len(lineList) 
inFile.close()

if (lineCount < blockSize):
    print('file length (' + str(lineCount) + ') less than block size (' + str(blockSize))
    sys.exit()

intList = [0] * lineCount
for i in range(lineCount):
    intList[i] = int(lineList[i].rstrip())

for i in range(blockSize, lineCount):
    curNum = intList[i]
    blockStart = i - blockSize
    blockEnd = i
    blockList = intList[blockStart:blockEnd]
    blockList.sort()
    minSum = blockList[0] + blockList[1]
    maxSum = blockList[blockSize - 2] + blockList[blockSize - 1]
    if (curNum < minSum) or (curNum > maxSum):
       print(curNum, 'is invalid')
       break
    sumList = [0] * (blockSize * blockSize)
    totSums = 0
    for j in range(blockStart, blockEnd - 1):
        for k in range(blockStart + 1, blockEnd):
           sumList[totSums] = intList[j] + intList[k]
           totSums += 1
    found = False
    for j in range(totSums):
        if curNum == sumList[j]:
            found = True
    if not found:
        print(curNum, 'is invalid') 
        break
