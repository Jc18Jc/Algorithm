# inversion count 사용
import sys
n=int(input())
array = list(map(int, sys.stdin.readline().split()))
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
            
### 코드리뷰 ###
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 0
def merge_sort(start, end):
    global answer, arr
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        temp = []
        x, y = start, mid + 1
        while x <= mid and y <= end:
            if arr[x] <= arr[y]:
                temp.append(arr[x])
                x += 1
            else:
                temp.append(arr[y])
                y += 1
                answer += (mid - x) + 1
        if x <= mid: # 굳이 while문 안돌리고 이렇게 남은거 한 번에 넣어도 괜찮네
            temp = temp + arr[x:mid + 1]
        if y <= end:
            temp = temp + arr[y:end + 1]
        for i in range(len(temp)):
            arr[start+i] = temp[i]

merge_sort(0, n-1)
print(answer)
'''