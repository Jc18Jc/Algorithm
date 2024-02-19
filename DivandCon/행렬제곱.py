N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
matrixList = []

def power(array1, array2):
    tmp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j]+=array1[i][k]*array2[k][j]
            tmp[i][j]%=1000
    return tmp

basic = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N): basic[i][i]=1
matrixList.append(power(basic, matrix)) # 맨 처음 매트릭스의 원소가 1일 경우를 생각해 power 메소드에 기약함수랑 넣어서 모듈러 연산이 되게 함

i = 0
while 1<<(i+1) <= B:
    i+=1
    matrixList.append(power(matrixList[-1], matrixList[-1]))

mat = basic
while i > -1:
    if 1<<i <= B:
        mat = power(mat, matrixList[i])
        B-=1<<i
    i-=1

for i in range(N):
    print(*mat[i])


### 코드리뷰 ###
'''
def multi(a,b):
    X = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                X[i][j] += a[i][k]*b[k][j]
    return X

def square(x,n): # 나는 i를 줄여가면서 이진수 구하듯이 답을 찾았는데 완전 분할정복 함수 구현해도 됐겠구나
    if n == 1:
        return x
    temp = square(x,n//2)
    if n % 2 == 0 : # 오,, 짝수면 양 옆의 곱, 이건 생각 못했을 듯
        return multi(temp,temp) 
    else :  # 홀수면 양 옆과 하나의 곱
        return multi(multi(temp,temp),x)

import sys
N, B = map(int,sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = square(A,B)
for i in range(N): # 아예 마지막에 1000을 나눠주는구나 ? B가 매우 커서 원소가 말이 안되게 커지더라도 파이썬이라 상관이 없나보네
    for j in range(N):
        result[i][j] = result[i][j] %1000

for k in result:
    print(*k)
'''