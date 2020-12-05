#!/usr/bin/python

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
ppValidCount = 0
ppTotCount = 1
validFields = 0
i = 0

while i <= lineCount:
   if (i == lineCount):
      # handle end of file condition
      if validFields == 7: 
         ppValidCount = ppValidCount + 1
         print('** pp ' + str(ppTotCount) + ' is valid')
      else:
         print('** pp ' + str(ppTotCount) + ' is NOT valid')
   elif len(lineList[i]) == 1:
      # handle blank line / new record
      if validFields == 7: 
         ppValidCount = ppValidCount + 1
         print('** pp ' + str(ppTotCount) + ' is valid')
      else:
         print('** pp ' + str(ppTotCount) + ' is NOT valid')

      ppTotCount = ppTotCount + 1
      validFields = 0
   else:
      lineList[i] = lineList[i].strip()

      # birth year
      field = re.search(r'.*byr:(\d\d\d\d)\b', lineList[i])
      if field:
         byr = int(field.group(1))
         if (byr >= 1920) and (byr <= 2002):
            validFields = validFields + 1
            print('pp ' + str(ppTotCount) + ' birth year: ' + str(byr))

      # issue year
      field = re.search(r'.*iyr:(\d\d\d\d)\b', lineList[i])
      if field:
         iyr = int(field.group(1))
         if (iyr >= 2010) and (iyr <= 2020):
            validFields = validFields + 1
            print('pp ' + str(ppTotCount) + ' issue year: ' + str(iyr))

      # expiration year
      field = re.search(r'.*eyr:(\d\d\d\d)\b', lineList[i])
      if field:
         eyr = int(field.group(1))
         if (eyr >= 2020) and (eyr <= 2030):
            validFields = validFields + 1
            print('pp ' + str(ppTotCount) + ' exp year: ' + str(eyr))

      # height
      field = re.search(r'.*hgt:(\d+)(..)\b', lineList[i])
      if field:
         hgt = int(field.group(1))
         units = field.group(2)
         if units == 'cm':
            if (hgt >= 150) and (hgt <= 193):
               validFields = validFields + 1
               print('pp ' + str(ppTotCount) + ' height: ' + str(hgt) + ' ' + units)
         elif units == 'in':
            if (hgt >= 59) and (hgt <= 76):
               validFields = validFields + 1
               print('pp ' + str(ppTotCount) + ' height: ' + str(hgt) + ' ' + units)

      # hair color
      field = re.search(r'.*hcl:#([0-9a-f]{6})\b', lineList[i])
      if field:
         hcl = field.group(1)
         validFields = validFields + 1
         print('pp ' + str(ppTotCount) + ' hair color: ' + hcl)

      # eye color
      field = re.search(r'.*ecl:(amb|blu|brn|gry|grn|hzl|oth)\b', lineList[i])
      if field:
         ecl = field.group(1)
         validFields = validFields + 1
         print('pp ' + str(ppTotCount) + ' eye color: ' + ecl)

      # passport id
      field = re.search(r'.*pid:([0-9]{9})\b', lineList[i])
      if field:
         pid = str(field.group(1))
         validFields = validFields + 1
         print('pp ' + str(ppTotCount) + ' passport id: ' + pid)

      # country id (optional - this isn't needed, but adding as placeholder)
      field = re.search(r'.*cid:(\d+)\b', lineList[i])
      if field:
         cid = field.group(1)
         print('pp ' + str(ppTotCount) + ' country id: ' + cid)
   
   i = i + 1
   # end of while loop

print('total number of passport entries: ' + str(ppTotCount))
print('total number of valid passports: ' + str(ppValidCount))
