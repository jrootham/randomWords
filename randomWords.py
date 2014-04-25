#!/usr/bin/python

#  Create file of words indexed by dice rolls

import sys

MIN = 6
MAX = 12

LIMIT = 6 * 6 * 6 * 6 * 6 * 6

def isAscii(s):
  return all(ord(c) < 128 for c in s)
    
infile = open('/usr/share/dict/words')
count = 0

while 1 :
  line = infile.readline()
  if not line : break
  
  line = line.strip()
  
  if isAscii (line) and MIN < len(line) < MAX and not "'" in line : 
    print line
    
    count += 1
    
    if count >= LIMIT :  break

