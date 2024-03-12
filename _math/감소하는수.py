import math
N = int(input())

def rec(k, num):
    if k == 0:
        return
    next = 1
    n=k
    while num + next < N:
        n+=1
        next = math.comb(n, k)
    num+=math.comb(n-1, k)
    answer[k-1]=str(n-1)
    rec(k-1, num)

if N > 1022:
    print(-1)
    
else:
    num = 0
    u=1
    next=9
    while num+next < N:
        num+=next
        u+=1
        next = math.comb(10, u)

    answer = [0 for _ in range(u)]
    if u == 1:
        print(N)
    else:
        rec(u, num)
        answer.reverse()
        print(int(''.join(answer)))  


### 코드리뷰 ###
# 가능한 숫자들을 전부 배열에 넣어두고 정렬해서 출력했음, 훨씬 깔끔하긴 하다
# 나는 자릿수 파악 후 이분탐색 하듯 앞 자리 하나씩 찾아줬음, 어짜피 많아도 1022개라 시간 차이도 안날 듯
'''
from itertools import combinations

N = int(input())

result = []
for i in range(1, 11):
	for j in combinations(range(10), i): # 이런 표현도 가능하다고 알아두면 좋을 듯
		num = ''.join(list(map(str, reversed(list(j)))))
		result.append(int(num))

result.sort() # 경우의 수 다 구하더라도 정렬은 상상 못했을 것 같음
if N >= len(result):
	print(-1)
else:
	print(result[N])

'''