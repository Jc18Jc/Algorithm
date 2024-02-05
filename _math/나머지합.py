import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))
remCount = [0 for _ in range(m)]

total = 0
for i in range(n):
    total+=array[i]
    total%=m
    remCount[total]+=1

answer = remCount[0]

for i in range(m):
    answer+=math.comb(remCount[i], 2)
print(answer)


####  코드 리뷰 ####

'''
import sys
input = sys.stdin.readline

N,M= map(int, input().split())
num = list(map(int, input().split()))
sum = 0
numRemainder = [0] * M

for i in range(N):
  sum += num[i]
  numRemainder[sum % M] += 1

result = numRemainder[0]

for i in numRemainder:
  result += i*(i-1)//2     # comb 대신 연산으로 함, import가 덜 들어가는 점에서 더 좋은듯
  
print(result)

'''