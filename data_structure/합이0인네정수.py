import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D = [0]*n, [0]*n, [0]*n, [0]*n
for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, input().split())

answer = 0
d =  dict()

for i in A:
    for j in B:
        if i+j in d:
            d[i+j]+=1
        else:
            d[i+j]=1

for i in C:
    for j in D:
        if -(i+j) in d:
            answer+=d[-(i+j)]

print(answer)


### 코드리뷰 ###
'''
import sys
input = sys.stdin.readline

# 투포인터/정렬/이분탐색으로 풂, 속도가 많이 빨라짐, 그래도 python3 제출은 실패, 내 첫번째 제출이랑 비슷한 원린데?
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ab, cd = [], [] # 배열이 4개라 a+b, c+d로 투포인터 접근
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()
i, j = 0, len(cd) - 1
result = 0
while i < len(ab) and j >= 0:
    if ab[i] + cd[j] == 0:
        nexti, nextj = i + 1, j - 1
        while nexti < len(ab) and ab[i] == ab[nexti]: 
            nexti += 1
        while nextj >= 0 and cd[j] == cd[nextj]: 
            nextj -= 1
        
        result += (nexti - i) * (j - nextj) # 같은 것이 있는만큼 result에 더해줌, 0을 맞췄을 때 i와 j 중 무엇을 늘리고 줄일지 몰라서 필요
        i, j = nexti, nextj

    elif ab[i] + cd[j] > 0:
        j -= 1
    else:
        i += 1

print(result)
'''