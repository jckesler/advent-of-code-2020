#!/usr/local/bin/python3

import re
import sys

filename = sys.argv[1]

inFile = open(filename, 'r')
print('reading ' + filename)
lineList = inFile.readlines()
inFile.close()

lineCount = len(lineList) 
inst = [' '] * (lineCount + 1)
arg = [0] * (lineCount + 1)
for i in range(lineCount):
   curLine = lineList[i].rstrip()
   txt = curLine.split()
   inst[i] = txt[0]
   arg[i] = int(txt[1])
   print(inst[i], arg[i])

exePtr = 0
accVal = 0
endProg = lineCount
runFlag = True
exeCount = [0] * lineCount

while runFlag:
   exeIncrement = 1
   print('exe: ' + str(exePtr))
   if exeCount[exePtr] == 1:
      print('re-executing inst #' + str(exePtr) + ', acc is ' + str(accVal))
      runFlag = False
      continue
   exeCount[exePtr] = 1
   if inst[exePtr] == 'nop':
      print('nop')
   elif inst[exePtr] == 'acc':
      accVal += arg[exePtr]
      print('acc: ' + str(accVal))
   elif inst[exePtr] == 'jmp':
      exeIncrement = arg[exePtr]
      print('jmp: ' + str(exeIncrement))
   else:
      print('unknow instruction: ' + str(inst[exePtr]))
   exePtr += exeIncrement
   if exePtr >= endProg:
      runFlag = False
      print('end of program reached')
