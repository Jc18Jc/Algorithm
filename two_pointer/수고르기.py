import sys
N, M = map(int, input().split())
array = list(int(sys.stdin.readline()) for _ in range(N))
array.sort()
l, r = 0, 0

answer=10**12
while r < N and l < N:
    dif = array[r]-array[l]
    if dif >= M:
        answer = answer if answer < dif else dif
        l+=1
        if r == l:
            r+=1
    else:
        r+=1

print(answer)

### 코드리뷰 ###
'''
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
left, right = 0, 0

result = int(2e9)
while left <= right and right < n:

    if arr[right]-arr[left] < m:
        right += 1
    else:
        result = min(result, arr[right]-arr[left]) # 만약 left right가 같은 경우는 M이 0인 케이스밖에 없고 그러면 left가 right를 역전하지만 끝내도 되는구나
        left += 1

print(result)
'''