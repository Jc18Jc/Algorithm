from itertools import permutations
import sys
input = sys.stdin.readline

def calc(type):
  global f1, f2, f3
  if type == 4:
    plus=f1+f2+f3+1
    f1 = f2 = f3 = 0
    return plus
  plus = 0
  if f3:
    plus+=1
    f3=0
  if f2:
    if type >= 2:
      plus+=1
    else:
      f3=1
    f2=0
  if f1:
    if type == 3:
      plus+=1
    elif type == 2:
      f3=1
    else:
      f2=1
    f1=0
  if type == 1:
    f1=1
  elif type == 2:
    f2=1
  elif type == 3:
    f3=1
  return plus

N = int(input())
gain = [list(map(int, input().split())) for _ in range(N)]

max_score = -1
f1 = f2 = f3 = 0

players = [i for i in range(1, 9)]
for perm in permutations(players):
  order = list(perm[:3]) + [0] + list(perm[3:])
  total = 0
  base = 0
  for inningGain in gain:
    f1 = f2 = f3 = 0
    outCount = 0
    while outCount != 3:
      type = inningGain[order[base]]
      base = (base + 1) % 9
      if type == 0:
        outCount += 1
        continue
      total += calc(type)
  max_score = max(max_score, total)
print(max_score)