N, S = map(int, input().split())
array = list(map(int, input().split()))

def binarySearch(start, end):
    if start==end:
        return [0, array[start]]
    mid = (start+end)//2
    l1 = binarySearch(start, mid)
    l2 = binarySearch(mid+1, end)
    l = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            l.append(l1[i]+l2[j])
    return l

if N==1:
    exit(print(1 if array[0]==S else 0))
l1, l2 = binarySearch(0, N//2), binarySearch(N//2+1, N-1)
l1.sort(); l2.sort()
answer, left, right = 0, 0, len(l2)-1
while left < len(l1) and right > -1:
    if l1[left] + l2[right] == S:
        tleft, tright = left, right
        left+=1
        right-=1
        while left < len(l1) and l1[left-1]==l1[left]:
            left+=1
        while right > -1 and l2[right]==l2[right+1]:
            right-=1
        answer += (left-tleft)*(tright-right)
    elif l1[left]+l2[right] > S: right-=1
    else: left+=1
print(answer if S!=0 else answer-1)


### 코드리뷰 ###
'''
import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

# 같은 원소 개수를 세는 좋은 코드,, bisect left와 right로 개수 세 볼 생각은 못했네
# 막상 적용해보니 시간 차이는 없음, 코드 길이도, 근데 가독성 자체는 좋아진 듯
def getNum(arr, find):
    return bisect_right(arr, find) - bisect_left(arr, find)
    
# 사실상 내 binarySearch 함수와 같은데 훨씬 보기 좋고 짧음, combination이 항상 나쁜건 아니네 담부터 활용해보자
# 막상 적용해보니 시간은 더 마이너스긴 하네 ,, ㅎ,, 시간이 빡빡할 때는 내 방법이 맞긴 할 듯
def getSum(arr, sumArr): 
    for i in range(1, len(arr) + 1):
        for a in combinations(arr, i):
            sumArr.append(sum(a))
    sumArr.sort()

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = arr[:n//2], arr[n//2:]
leftSum, rightSum = [], []

getSum(left, leftSum)
getSum(right, rightSum)
ans = 0
for l in leftSum:
    find = s - l
    ans += getNum(rightSum, find)

ans += getNum(leftSum, s)
ans += getNum(rightSum, s)

print(ans)

'''

### 적용 해본 코드 ###
'''
from bisect import bisect_left, bisect_right
from itertools import combinations

N, S = map(int, input().split())
array = list(map(int, input().split()))

def getNum(arr, find):
    return bisect_right(arr, find) - bisect_left(arr, find)

def getSum(arr):
    sumArr=[0]
    for i in range(1, len(arr) + 1):
        for a in combinations(arr, i):
            sumArr.append(sum(a))
    sumArr.sort()
    return sumArr

if N==1:
    exit(print(1 if array[0]==S else 0))
l1, l2 = getSum(array[:N//2+1]), getSum(array[N//2+1:]
answer, left, right = 0, 0, len(l2)-1
while left < len(l1) and right > -1:
    if l1[left] + l2[right] == S:
        gn1, gn2 = getNum(l1, l1[left]), getNum(l2, l2[right])
        answer+=gn1*gn2
        left, right = left+gn1, right-gn2
    elif l1[left]+l2[right] > S: right-=1
    else: left+=1
print(answer if S!=0 else answer-1)
'''