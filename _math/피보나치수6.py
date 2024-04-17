import sys
sys.setrecursionlimit(10**5)
n=int(input())
M=1000000007

def mul(A, B):
    a = (A[0][0]*B[0][0]+A[0][1]*B[1][0])%M
    b = (A[0][0]*B[0][1]+A[0][1]*B[1][1])%M
    c = (A[1][0]*B[0][0]+A[1][1]*B[1][0])%M
    d = (A[1][0]*B[0][1]+A[1][1]*B[1][1])%M
    return [[a,b], [c,d]]

def dnc(num):
    if num == 1:
        return [[1, 1], [1, 0]]
    A = dnc(num//2)
    if num%2:
        return mul(mul(A, A), [[1, 1], [1, 0]])
    return mul(A, A)
print(dnc(n)[0][1])


### 코드리뷰 ###
# 처음에는 피보나치3처럼 피사노 주기를 이용해 풀려고 했음, 나눠 떨어지지 않아 블로그 참고해 풂
# 내 처음 방식은 dnc((num+1)//2), dnc(num//2)였는데 시간 초과나서 코드도 참고,,
# 같은 분할 정복인데 그림 그려서 생각해보면 해당 방식이 훨씬 좋음, 중복 계산이 아예 없음
'''
import sys # 입력은 하나라 굳이
input = sys.stdin.readline

n = int(input())
p = 1000000007

def mul(A, B): # 보다보니 다른 문제에서 한 제곱 함수를 가져온 듯 ??
    n = len(A) # len 코드도 굳이 있어야하나 싶음 어짜피 2*2 행렬인건 고정인데, 그리고 전역변수 n도 있어서 위험한 코드
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n): # 차원이 커졌을 때 이런 점화식 써야할 듯, 직접 한 두번 쓰면 알 수 있을 듯
                e += A[row][i] * B[i][col]
            Z[row][col] = e % p
    return Z

def square(A, k):
    if k == 1:
        for x in range(len(A)): # 이게 필요한 코드인가 ?? .. 필요 없는거 맞네, 어짜피 [[1,1],[1,0]]일텐데
            for y in range(len(A)):
                A[x][y] %= p
        return A
    
    tmp = square(A, k//2)
    if k % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])
'''