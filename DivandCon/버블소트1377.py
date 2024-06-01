# inversion count 사용
import sys
n=int(input())
array = list(int(sys.stdin.readline()) for _ in range(n))
inversionCount = 0

def div(s, e):
    if e-s > 0:
        mid = (s+e)//2
        div(s, mid)
        div(mid+1, e)
        merge(s, mid, mid+1, e)

def merge(s1, e1, s2, e2):
    global inversionCount
    s,e=s1,e2
    tmp = []
    while s1 <= e1 and s2 <= e2:
        if array[s1] <= array[s2]:
            tmp.append(array[s1])
            s1+=1
        else:
            tmp.append(array[s2])
            s2+=1
            inversionCount+=e1-s1+1
    if s1<=e1: s3, e3 = s1,e1
    else: s3, e3 = s2, e2
    while s3 <= e3:
        tmp.append(array[s3])
        s3+=1
    array[s:e+1] = tmp

div(0, n-1)
print(inversionCount)