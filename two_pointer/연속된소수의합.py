n = int(input())

if n == 1:
    exit(print(0))

isPrime = [True for _ in range(n+1)]
prime = []

for i in range(2, n+1):
    if isPrime[i]:
        prime.append(i)
        j=2
        while j*i <= n:
            isPrime[i*j]=False
            j+=1

size = len(prime)

left = size-1
right = size-1
total = 0
count=0

while left > -1:
    total+=prime[left]
    if total == n:
        count+=1
        total-=prime[right]
        right-=1
    elif total > n:
        total-=prime[right]
        right-=1
    left-=1
    
print(count)



####  코드 리뷰 ####

'''
import math

N = int(input())

a = [False, False] + [True] * (N-1)  # for문을 2부터 시작해서 [False, False] 과정은 필요 없을 듯
prime_num = []

for i in range(2, N+1):
    if a[i]:
        prime_num.append(i)
        for j in range(2*i, N+1, i):  # while 대신 for 사용, j를 곱할 수가 아닌 곱해진 수로 두고 증가량을 i로 괜찮은 듯
            a[j] = False

answer = 0
start = 0
end = 0
# 끝부터 시작한 것과 반대로 처음부터 시작, start/end가 동일한 투포인터 구현은 같음
while end <= len(prime_num):
    temp_sum = sum(prime_num[start:end])  # sum으로 매번 구하는 것은 좋지 않을 듯, total로 누적하는 것이 좋아보임
    # end - start, 즉 한 배열의 길이 안에서 하나의 답만 나오는 것을 이해한 내가 더 시간복잡도 상 이익일 것 같으나 이게 보기엔 깔끔한 듯
    if temp_sum == N:
        answer += 1
        end += 1
    elif temp_sum < N:
        end += 1
    else:
        start += 1
    

print(answer)


'''