import sys
input = sys.stdin.readline

array = []

N = int(input())

for i in range(N):
  c, s = map(int, input().split())
  array.append((s, c, i))

array.sort()

flagNumber = 0
sumColor = [0] * (N+1)
stackValue = 0
newValue = 0
board = [0 for _ in range(N)] 
tmpColorDict = dict()

for i in range(N):
  s, c, index = array[i]
  if flagNumber != s:
    stackValue += newValue
    flagNumber = s
    newValue = 0
    tmpColorDict.clear()
  tmpNum = tmpColorDict.get(c) if tmpColorDict.get(c) else 0
  board[index] = stackValue - sumColor[c] + tmpNum
  sumColor[c] += s
  tmpColorDict[c] = tmpNum + s
  newValue += s

for i in range(N):
  print(board[i])

  