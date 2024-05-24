import sys
N=int(input())
MAX_VALUE=1000000
array = list(int(sys.stdin.readline()) for _ in range(N))
answer = [0, 1] + [i+1 for i in range(2, MAX_VALUE+1)]
isPrime = [True for _ in range(MAX_VALUE+1)]

def eratos():
    for i in range(2, MAX_VALUE//2):
        if isPrime[i]:
            j=2
            while i*j <= MAX_VALUE:
                isPrime[i*j]=False
                j+=1

eratos()

for i in range(2, MAX_VALUE+1):
    answer[i]=answer