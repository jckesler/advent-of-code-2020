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

#
# really kludgy stuff, started with a set intersection approach, but had issues
#
lineCount = len(lineList)
groupCount = 0
answerCount = 0
personCount = 0
totalCount = 0
i = 0
answers = [0] * 1024

while i < lineCount:
   curLine = lineList[i]
   if len(curLine) == 1:
      groupCount = groupCount + 1
      for k in range(ord('a'), ord('z') + 1):
         if answers[k] >= personCount:
            answerCount += 1
      totalCount += answerCount
      answers = [0] * 1024
      print('group ' + str(groupCount) + ': ' + str(answerCount))
      answerCount = 0
      personCount = 0
      i += 1
      continue
   curLine = curLine.rstrip()
   for j in range(len(curLine)):
      char = curLine[j]
      if (char >= 'a') and (char <= 'z'):
         answers[ord(char)] += 1
   personCount += 1
   i += 1
   # end loop

groupCount += 1
#if personCount > 0:
for k in range(ord('a'), ord('z') + 1):
   if answers[k] >= personCount:
      answerCount += 1
totalCount += answerCount
print('group ' + str(groupCount) + ': ' + str(answerCount))

print('total for ' + str(groupCount) + ' groups: ' + str(totalCount))
