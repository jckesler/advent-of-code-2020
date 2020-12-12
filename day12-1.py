#!/usr/local/bin/python3

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

x = 0
y = 0
d = 90
for i in range(lineCount):
    curLine = lineList[i].rstrip()
    cmd = curLine[0]
    delta = int(curLine[1:len(curLine)])
    if cmd == 'N':
        # move north
        y = y + delta
    elif cmd == 'E':
        # move east
        x = x + delta
    elif cmd == 'S':
        # move south
        y = y - delta
    elif cmd == 'W':
        # move west
        x = x - delta
    elif cmd == 'F':
        if d == 0:
            # facing north
            y = y + delta
        elif d == 90:
            # facing east
            x = x + delta
        elif d == 180:
            # facing south
            y = y - delta
        elif d == 270:
            # facing west
            x = x - delta
    elif cmd == 'R':
        print('>>>>>>>>>> rotating', delta, '>>>>>>>>>>')
        d = d + delta
        if (d >= 360):
            d = d - 360
    elif cmd == 'L':
        print('<<<<<<<<<< rotating', delta, '<<<<<<<<<<')
        d = d - delta
        if (d < 0):
            d = d + 360
    else:
        print('unknown command')
    print('move', i, '- cmd:', cmd, 'val:', delta)
    print('new position - x:', x, 'y:', y, 'direction:', d)
    print(' ')

ans = abs(x) + abs(y)
print('answer is', ans)
