n=int(input())
array = [[' ' for _ in range(2*n-1)] for _ in range(n)]
s2='* *'
s3='*****'
def rec(m, i, j):
    if m > 3:
        rec(m//2, i, j)
        rec(m//2, i+m//2, j-m//2)
        rec(m//2, i+m//2, j+m//2)
        return
    array[i][j]='*'
    array[i+1][j-1:j+2]=s2
    array[i+2][j-2:j+3]=s3

rec(n, 0, n-1)
for i in range(n):
    print(''.join(array[i])) # 원래 i,j로 다 출력했는데 시간초과 나와서 join함, 출력에서 시간 많이 쓸 때는 좋은 방법인 듯

### 코드리뷰 ###
'''
# 거의 똑같음
import sys
input = sys.stdin.readline

n = int(input())

stars = [[' ']*2*n for _ in range(n)]

def recursion(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"
    
    else:
        newSize = size//2
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)

recursion(0, n - 1, n)
for star in stars:
    print("".join(star))
'''