from collections import defaultdict
t=int(input())
n=int(input())
array1 = list(map(int, input().split()))
m=int(input())
array2 = list(map(int, input().split()))

hapDict1 = defaultdict(int)
for i in range(n):
    hap=0
    for j in range(i, n):
        hap+=array1[j]
        hapDict1[hap]+=1
answer = 0
for i in range(m):
    hap=0
    for j in range(i, m):
        hap+=array2[j]
        answer += hapDict1[t-hap]
print(answer)


### 코드리뷰 ###
'''
t = int(stdin.readline())
n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
B = list(map(int, stdin.readline().split()))

Asum = {}
for i in range(n):
    for j in range(i, n):
        k = sum(A[i:j + 1]) # sum이나 배열 슬라이싱도 자원소모가 심해서 나처럼 하나씩 더해주는게 훨씬 좋을 듯
        if k in Asum: # 나는 defaultdict로 이 부분 줄임
            Asum[k] += 1
        else:
            Asum[k] = 1

Bsum = {} # 나도 이렇게 B까지 defalutdict로 구했다가 메모리 초과나서 즉각 answer에 더해주는 식으로 바꿨는데, defaultdict와 dict의 차인가 .. ? 
for i in range(m):
    for j in range(i, m):
        k = sum(B[i:j + 1])
        if k in Bsum:
            Bsum[k] += 1
        else:
            Bsum[k] = 1

res = 0

for key in Asum.keys():
    if (t - key) in Bsum:
        res += Bsum[t - key] * Asum[key]

print(res)
'''