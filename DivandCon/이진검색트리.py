# 분할정복 겸 재귀, 자료구조
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

array=[]

while True:
    try:
        array.append(int(input()))
    except:
        break

def dnc(s, e):
    if s > e:
        return
    i=s
    while i < e and array[i+1] < array[s]:
        i+=1
    dnc(s+1, i)
    dnc(i+1, e)
    print(array[s])
dnc(0, len(array)-1)

# 리뷰한 코드 방법 참고해서 짜 본 코드, 오히려 시간 더 걸림,, 무슨 차이지 ?
# def dnc(a):
#     if len(a) == 0:
#         return
#     tmp=0
#     for i in range(len(a)-1):
#         if a[i+1] > a[0]:
#             tmp=i
#             break
#     dnc(a[1:tmp+1])
#     dnc(a[tmp+1:len(a)])
#     print(a[0])
# dnc(array)


### 코드리뷰 ###
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

# 배열 형태로 넘기는 방식을 채택, 굳이 배열로 넘기는건 효율측면에서 별로일 듯, 왜 내 것보다 속도가 잘 나오지 ? 진짜 모름
# 배열로 구현해봤는데 시간 더 걸림, 어느 요소 차이지? 참고로 while보다 for이 효율 좋은 것도 맞음
def solution(A): 
    if len(A) == 0: # s > e 를 의미
        return
    tempL, tempR = [], []
    mid = A[0]
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:  # 이 else는 어느 if랑 매칭이지 ?, 브레이크에 안 걸렸다는 의민가? 새로운 문법 확인
        tempL = A[1:]
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)
'''