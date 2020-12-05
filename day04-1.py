#!/usr/bin/python

import re
import sys

if len(sys.argv) < 2:
   print('syntax: ' + sys.argv[0] + ' <filename>')
   sys.exit()

filename = sys.argv[1]

inFile = open(filename, 'rb')
print('reading ' + filename)
lineList = inFile.readlines()
inFile.close()

lineCount = len(lineList)
ppValidCount = 0
ppTotCount = 1
reqFieldsFound = 0
i = 0
while i <= lineCount:
   if (i == lineCount):
      if reqFieldsFound >= 7:
         print('** pp ' + str(ppTotCount) + ' is valid')
         ppValidCount = ppValidCount + 1
   elif len(lineList[i]) == 1:
      if reqFieldsFound >= 7:
         print('** pp ' + str(ppTotCount) + ' is valid')
         ppValidCount = ppValidCount + 1
      else:
         print('** pp ' + str(ppTotCount) + ' is NOT valid')
      reqFieldsFound = 0
      ppTotCount = ppTotCount + 1
   else:
      ppSearch = re.search(r'byr:\S+', lineList[i])
      if ppSearch:
         reqFieldsFound = reqFieldsFound + 1
         print('pp ' + str(ppTotCount) + ' birth year: ' + ppSearch.group())
      ppSearch = re.search(r'iyr:\S+', lineList[i])
      if ppSearch:
         reqFieldsFound = reqFieldsFound + 1
         print('pp ' + str(ppTotCount) + ' issue year: ' + ppSearch.group())
      ppSearch = re.search(r'eyr:\S+', lineList[i])
      if ppSearch:
         reqFieldsFound = reqFieldsFound + 1
         print('pp ' + str(ppTotCount) + ' exp year: ' + ppSearch.group())
      ppSearch = re.search(r'hgt:\S+', lineList[i])
      if ppSearch:
         reqFieldsFound = reqFieldsFound + 1
         print('pp ' + str(ppTotCount) + ' height: ' + ppSearch.group())
      ppSearch = re.search(r'hcl:\S+', lineList[i])
      if ppSearch:
         reqFieldsFound = reqFieldsFound + 1
         print('pp ' + str(ppTotCount) + ' hair color: ' + ppSearch.group())
      ppSearch = re.search(r'ecl:\S+', lineList[i])
      if ppSearch:
         reqFieldsFound = reqFieldsFound + 1
         print('pp ' + str(ppTotCount) + ' eye color: ' + ppSearch.group())
      ppSearch = re.search(r'pid:\S+', lineList[i])
      if ppSearch:
         reqFieldsFound = reqFieldsFound + 1
         print('pp ' + str(ppTotCount) + ' passport id: ' + ppSearch.group())
      ppSearch = re.search(r'cid:\S+', lineList[i])
      if ppSearch:
         print('pp ' + str(ppTotCount) + ' country id: ' + ppSearch.group())
   i = i + 1

print('total number of passport entries: ' + str(ppTotCount))
print('total number of valid passports: ' + str(ppValidCount))
