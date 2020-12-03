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
validPasswdCount = 0

for i in range(lineCount):
   elementList = lineList[i].split()
   policyFreq = elementList[0].split('-')
   policyPos1 = int(policyFreq[0]) - 1
   policyPos2 = int(policyFreq[1]) - 1
   policyChar = elementList[1][0:1]
   passwd = elementList[2]
   foundFlag = 0
   if passwd[policyPos1] == policyChar:
      foundFlag = foundFlag + 1
   if passwd[policyPos2] == policyChar:
      foundFlag = foundFlag + 1
   if foundFlag == 1:
      validPasswdCount = validPasswdCount + 1
      print(passwd + ' is a valid passwd')

print(str(lineCount) + ' lines read')   
print(str(validPasswdCount) + ' valid passwds found')

inFile.close()
