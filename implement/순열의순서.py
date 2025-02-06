import sys
import math
input = sys.stdin.readline

N=int(input())
array = list(map(int, input().split()))

if array[0]==1:
  o = array[1]-1
  cand = [i+1 for i in range(N)]
  result = []
  M = math.factorial(N-1)
  mul = N-1
  while mul > 0:
    result.append(cand[o//M])
    cand.pop(o//M)
    o%=M
    M//=mul
    mul-=1
  result.append(cand[0])
  print(*result)
else:
  numbers = array[1:]
  cand = [i+1 for i in range(N)]
  M = math.factorial(N-1)
  mul = N-1
  result = 1
  for i in range(N-1):
    index = cand.index(numbers[i])
    result += index*M
    cand.pop(index)
    M//=mul
    mul-=1
  print(result)