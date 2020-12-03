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
   policyMin = int(policyFreq[0])
   policyMax = int(policyFreq[1])
   policyChar = elementList[1][0:1]
   passwd = elementList[2]
   charCount = 0
   for j in passwd:
      if j == policyChar:
         charCount = charCount + 1
   if (charCount >= policyMin) and (charCount <= policyMax):
         print(passwd + ' is a valid passwd')
         validPasswdCount = validPasswdCount + 1

print(str(lineCount) + ' lines read')   
print(str(validPasswdCount) + ' valid passwds found')

inFile.close()
