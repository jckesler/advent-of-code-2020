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

endProg = lineCount
endFlag = False

for updInst in range(lineCount):
    if endFlag:
        break
    runFlag = True
    exePtr = 0
    accVal = 0
    exeCount = [0] * lineCount
    print('*** starting program ***')
    while runFlag:
        exeIncrement = 1
        if exeCount[exePtr] == 1:
            print('re-exec inst #' + str(exePtr) + ', acc is ' + str(accVal))
            runFlag = False
            continue
        exeCount[exePtr] = 1
        if inst[exePtr] == 'nop':
            print('nop', exePtr, updInst)
            if exePtr == updInst:
                exeIncrement = arg[exePtr]
                print('*' + str(exePtr) + ' ' + 'jmp: ' + str(exeIncrement))
            else:    
                print('#' + str(exePtr) + ' ' + 'nop')
        elif inst[exePtr] == 'acc':
            accVal += arg[exePtr]
            print('#' + str(exePtr) + ' ' + 'acc: ' + str(accVal))
        elif inst[exePtr] == 'jmp':
            print('jmo', exePtr, updInst)
            if exePtr == updInst:
                print('*' + str(exePtr) + ' ' + 'nop')
            else:    
                exeIncrement = arg[exePtr]
                print('#' + str(exePtr) + ' ' + 'jmp: ' + str(exeIncrement))
        else:
            print('unknow instruction: ' + str(inst[exePtr]))
        exePtr += exeIncrement
        if exePtr >= endProg:
            runFlag = False
            endFlag = True
            print('!!! end of program !!!')
            print('acc: ' + str(accVal))
