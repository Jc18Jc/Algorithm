import sys
input = sys.stdin.readline
from queue import PriorityQueue
N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

left = T[0]
right = T[0]*M
answer=0
while left <= right:
    mid = (left+right)//2
    tmp=0
    flag=False
    for i in range(N):
        tmp+=mid//T[i]
        if mid%T[i]==0:
            flag=True
        if tmp > M or T[i] > mid:
            break
    if tmp>=M and flag:
        answer=mid
    if tmp < M:
        left=mid+1
    else:
        right=mid-1

print(answer)


### 코드리뷰 ###
'''
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
time = []
for _ in range(N):
    time.append(int(input()))

left = min(time)
right = max(time) * K
result = float('inf')

while left <= right: # 그냥 딱 이분탐색만 했는데, 생각해보니 나처럼 굳이 flag 안써도 어짜피 최소값 찾아가니까 이게 맞는듯,,
    mid = (left + right) // 2
    total = 0
    for i in time:
        total += mid // i
    if total >= K:
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1
print(result)
'''

### 리뷰 이후 코드 ###
# 시간 1796->1200ms
'''
import sys
input = sys.stdin.readline
from queue import PriorityQueue
N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

left = T[0]
right = T[0]*M
answer=0
while left <= right:
    mid = (left+right)//2
    tmp=0
    for i in range(N):
        tmp+=mid//T[i]
        if tmp > M:
            break
    if tmp>=M:
        answer=mid
        right=mid-1
    elif tmp < M:
        left=mid+1

print(answer)
'''