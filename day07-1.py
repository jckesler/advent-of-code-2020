#!/usr/local/bin/python3

import re
import sys

def search_dict(target, node, d):
   print() 
   print('searching:')
   print(node)
   if node == target:
      return 1
   s = 0
   for key in d[node]:
      print(key, d[node])
      s += search_dict(target, key, d)
   if s > 0:
      s = 1
      print('sum', key, s) 
   return s

if len(sys.argv) < 2:
   print('syntax: ' + sys.argv[0] + ' <filename>')
   sys.exit()

filename = sys.argv[1]

inFile = open(filename, 'r')
print('reading ' + filename)
lineList = inFile.readlines()
inFile.close()

lineCount = len(lineList)

bagRule = {}

for i in range(lineCount):
   curLine = lineList[i].rstrip()
   txt = curLine.split(' bags contain ')
   bagType = txt[0]
   bagText = txt[1]
   print(bagType + ': ' + bagText)
   bagText = bagText.rstrip('.')
   bagRule[bagType] = {}
   if (bagText == 'no other bags'):
      print('no bags')
   else:
      innerBag = bagText.split(', ')
      print(innerBag)
      for j in range(len(innerBag)):
         txt = re.search(r'(\d+) (.+) bag', innerBag[j])
         if txt:
            print('inner bag ' + txt[2] + ': ' + txt[1])
            innerBagType = txt[2]
            innerBagVal = txt[1]
            bagRule[bagType][innerBagType] = innerBagVal
   print()

print('dictionary:')
print(bagRule)
print()

target = 'shiny gold'
total = 0
for key in bagRule.keys():
   if key == 'shiny gold':
      continue
   total += search_dict(target, key, bagRule)

print()
print('final answer:', total)
