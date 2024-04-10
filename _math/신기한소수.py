N=int(input())

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num%i==0:
            return False
    return True

def bt(i, num):
    if not isPrime(num):
        return
    if i==N:
        print(num)
        return
    for j in range(1, 10):
        bt(i+1, num*10+j)

for i in range(10):
    bt(1, i)


### 코드리뷰 ###
# 에라토스테네스의 체로 풀다가 해결이 안돼서 블로그 참고함, 차라리 분류를 봤어도 풀었을 듯 ?
'''
import sys
input = sys.stdin.readline # 이건 필요할 때만 쓰자

n = int(input())

def checkPrimeNum(check_number):
    for i in range(2, int(check_number**0.5)+1): 
        if int(check_number) % i == 0: 
            return False
    return True

def dfs(num):
    if len(str(num))==n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if checkPrimeNum(temp) == True:
                dfs(temp)

# 이렇게 첫 숫자를 정해주는 것의 장점은 check할 때 0~1을 따로 안빼줘도 된다는 것 정도 ?
dfs(2)
dfs(3)
dfs(5)
dfs(7)

'''