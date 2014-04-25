from json import load

wordFile = open('randomWords.json', 'r')
wordList = load(wordFile)
wordFile.close()

def inrange(c):
  return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z'))
  
if all(map((lambda x:all(map(inrange,x))), wordList)):
  print "in range"
else:
  print "out of range"

