#!/usr/bin/python

#  Make a JSON array out of a file of words

import sys

 
infile = open('randomWords.txt')
prefix = '['
result = ''

while 1 :
  line = infile.readline()
  if not line : break
  
  line = line.strip()
  result += prefix + '"' + line + '"'
  prefix = ','

print result + ']'

