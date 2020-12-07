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

lineCount = len(lineList)
groupCount = 0
answerCount = 0
answerSet = {''}
answerSet.clear()

for i in range(lineCount):
   if len(lineList[i]) == 1:
      #
      # handle blank line / end group / start new group
      #
      answerCount = answerCount + len(answerSet)
      groupCount = groupCount + 1
      print('group ' + str(groupCount))
      print(answerSet)
      answerSet.clear()
   else:
      lineList[i] = lineList[i].strip()
      print(lineList[i])
      for j in range(len(lineList[i])):
         answer = lineList[i][j]
         if (answer >= 'a') and (answer <= 'z'):
            answerSet.add(answer)

if len(answerSet) > 0:
   answerCount = answerCount + len(answerSet)
   groupCount = groupCount + 1
   print('group ' + str(groupCount))
   print(answerSet)
   answerSet.clear()

print('number of groups: ' + str(groupCount))
print('sum of answer counts: ' + str(answerCount))
