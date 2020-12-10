#!/usr/local/bin/python3

import sys

if len(sys.argv) < 3:
   print('syntax: ' + sys.argv[0] + ' <filename> <blocksize>')
   sys.exit()

filename = sys.argv[1]
target = int(sys.argv[2])

inFile = open(filename, 'r')
print('reading ' + filename)
lineList = inFile.readlines()
lineCount = len(lineList) 
inFile.close()

intList = [0] * lineCount
for i in range(lineCount):
    intList[i] = int(lineList[i].rstrip())

start = 0
last = 0
print('looking for', target)
while start < lineCount:
    current = start
    total = 0
    print('starting at', start)
    while (total < target) and (current < lineCount):
        total = total + intList[current]
        print(current, intList[current], total)
        if total == target:
            last = current + 1
            break
        current += 1
    if total == target:
        break
    start += 1

print('start=', start, 'last=', last)
subset = intList[start:last]
minVal = min(intList[start:last])
maxVal = max(intList[start:last])
sumVal = minVal + maxVal
print('min=', minVal, 'max=', maxVal, 'sum=', sumVal)
