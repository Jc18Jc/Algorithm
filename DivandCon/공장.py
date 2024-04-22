import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

N=int(input())
array = list(map(int, input().split()))
array2 = list(map(int, input().split()))

d = dict()
for i in range(N):
    d[array2[i]]=i

for i in range(N):
    array[i]=d[array[i]]

def mergeSort(s, e):
    global answer
    if s==e:
        return
    mid=(s+e)//2 
    mergeSort(s, mid)
    mergeSort(mid+1, e)
    tmp = [0 for _ in range(e-s+1)]
    k=0
    a, b = s, mid+1
    while a<=mid and b<=e:
        if array[a] < array[b]:
            tmp[k]=array[a]
            a+=1
        else:
            tmp[k]=array[b]
            b+=1
            answer+=mid+1-a
        k+=1
    if b <= e:
        tmp[k:]=array[b:e+1]
    else:
        tmp[k:]=array[a:mid+1]
    array[s:e+1]=tmp

answer=0
mergeSort(0, N-1)
print(answer)


### 코드리뷰 ###
# 나는 합병 정렬 이용, 정석 풀이는 세그먼트 트리(팬웍 트리)
'''
import sys
input = sys.stdin.readline

def locate(m, idx):
    acc_num = 0
    k = idx
    while k > 0:
        acc_num += fenwick_tree[k]
        k -= k & -k 

    k = idx
    while k <= n:
        fenwick_tree[k] += 1 
        k += k & -k 
    return m - acc_num
    
n = int(input())
fenwick_tree = [0]*(n+1)
loc = {}
count = 0
for i, a in enumerate(map(int, input().rstrip().split())):
    loc[a] = i+1
    
for i, b in enumerate(map(int, input().rstrip().split())):
    count += locate(i, loc[b])
    
print(count)
'''