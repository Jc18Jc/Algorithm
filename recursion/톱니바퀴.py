wheel = [list(map(int, input())) for _ in range(4)]
k = int(input())

def turn(num, m, pre):
    if pre != 1 and num > 0 and wheel[num][6] != wheel[num-1][2]:
        turn(num-1, m*-1, 2)
    if pre != 2 and num < 3 and wheel[num][2] != wheel[num+1][6]:
        turn(num+1, m*-1, 1)
    if m==1:
        wheel[num] = [wheel[num][7]]+wheel[num][0:7]
    else:
        wheel[num] = wheel[num][1:8]+[wheel[num][0]]

for _ in range(k):
    num, m = map(int, input().split())
    turn(num-1, m, 0)

answer=0
for i in range(4):
    if wheel[i][0]==1:
        answer+=1<<i
print(answer)


### 코드리뷰 ###
'''
import sys
from collections import deque # 덱의 rotate 함수 좋은 듯
input = sys.stdin.readline
t = [deque(list(map(int,input().rstrip()))) for _ in range(4)]

k = int(input())
# 톱니가 4개밖에 없어서 재귀가 아닌 단순 반복으로 해결했다고 함
for _ in range(k): 
	r = []
	for i in range(4):
		r.append([t[i][6],t[i][2]])
	n,d = map(int,input().split())
	n = n-1
    
	if n != 0 : # 쓸데없는 조건
		for i in range(n,0,-1):
			if r[i][0] != r[i-1][1]:
				if (n-(i-1))%2 == 0: # 돌린 톱니와 짝수 or 홀수만큼 떨어져있는지 확인, 왜 ? 돌리는 것도 먼저 돌리면 안되지 않나 ?
					t[i-1].rotate(d)
				elif (n-(i-1))%2 != 0:
					t[i-1].rotate(-1*d)
			elif r[i][0] == r[i-1][1]:
				break
	if n != 3: # 마찬가지
		for i in range(n,3):
			if r[i][1] != r[i+1][0]:
				if (n-(i+1))%2 == 0:
					t[i+1].rotate(d)
				elif (n-(i+1))%2 != 0:
					t[i+1].rotate(-1*d)
			elif r[i][1] == r[i+1][0]:
				break
	t[n].rotate(d)
    
res = 0
if t[0][0] == 1:
	res+=1
if t[1][0] == 1:
	res+=2
if t[2][0] == 1:
	res+=4
if t[3][0] ==1:
	res+=8
print(res)
'''