#!/usr/local/bin/python3

import math
import sys

if len(sys.argv) < 2:
   print('syntax: ' + sys.argv[0] + ' <filename>')
   sys.exit()

filename = sys.argv[1]

inFile = open(filename, 'r')
print('reading ' + filename)
lineList = inFile.readlines()
lineCount = len(lineList) 
inFile.close()

sx = 0
sy = 0
wx = 10
wy = 1
print('starting positions:')
print('ship position - x:', sx, 'y:', sy)
print('wayp position - x:', wx, 'y:', wy)
print('----------------------------------------------')
for i in range(lineCount):
    curLine = lineList[i].rstrip()
    cmd = curLine[0]
    delta = int(curLine[1:len(curLine)])
    if cmd == 'N':
        # move north
        wy = wy + delta
    elif cmd == 'E':
        # move east
        wx = wx + delta
    elif cmd == 'S':
        # move south
        wy = wy - delta
    elif cmd == 'W':
        # move west
        wx = wx - delta
    elif cmd == 'F':
        sx = sx + (wx * delta)
        sy = sy + (wy * delta)
    elif (cmd == 'R') or (cmd == 'L'):
        if (cmd == 'L'):
            delta = -delta
        print('---------- rotating', delta, '----------')
        rad = delta * (math.pi / 180)
        sin = int(math.sin(rad))
        cos = int(math.cos(rad))
        nwx = (cos * wx) + (sin * wy)
        nwy = (-sin * wx) + (cos * wy)
        wx = nwx
        wy = nwy
    else:
        print('unknown command')
    print('move', i, '- cmd:', cmd, 'val:', delta)
    print('ship position - x:', sx, 'y:', sy)
    print('wayp position - x:', wx, 'y:', wy)
    print(' ')

ans = abs(sx) + abs(sy)
print('answer is', ans)
