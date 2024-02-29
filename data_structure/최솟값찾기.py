import sys
input = sys.stdin.readline 
from collections import deque
N, L = map(int, input().split())
array = list(map(int, input().split()))
d=deque()
mNum = array[0]
mIndex = 0
for i in range(N):
    if mNum >= array[i]:
        mNum=array[i]
        mIndex=i
        d.clear()
    else:
        while d and d[-1][0]> array[i]:
            d.pop()
        d.append([array[i], i])
    if mIndex < i-L+1:
        v=d.popleft()
        mNum = v[0]
        mIndex = v[1]
    print(mNum, end=' ')


### 코드리뷰 ###
# 내껀 pypy만 통과했는데 이건 파이썬도 통과하는 모양
'''
import sys
from collections import deque
input = sys.stdin.readline
N, L = map(int,input().split())
num = list(map(int, input().split()))
temp = deque([])

for i in range(N):
    if temp and temp[0][0] <= i-L: # 따로 mNum이나 mIndex 안만들고 덱 안에서 다 처리했구나, 맨 앞이 제일 작은 것으로 유지
        temp.popleft()
    while len(temp) >= 1 and num[i] < temp[-1][1]:
        temp.pop()
    temp.append((i,num[i]))
    print(temp[0][1], end = " ")
'''
### 코드리뷰 후 코드 ###
# 이건 왜 시간 초과 날까, 오로지 데크에 넣을 때 튜플이 아닌 배열을 넣는 다는 것? 혹은 데크 값 존재 여부를 len 대신 데크 자체를 넣는 것 .. ?
# 확인 결과 튜플이 맞음, 얼마나 차이나는지는 모르겠는데 튜플이 빠르긴 한 듯, 앞으로 참고
'''
import sys
input = sys.stdin.readline 
from collections import deque
N, L = map(int, input().split())
array = list(map(int, input().split()))
d=deque([[10**10, -1]])
for i in range(N):
    if d[0][1] < i-L+1:
        d.popleft()
    while d and d[-1][0]> array[i]:
        d.pop()
    d.append([array[i], i])
    print(d[0][0], end=' ')
'''