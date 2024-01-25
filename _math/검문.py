import sys
ssr = sys.stdin.readline

n=int(ssr())
numArray = [0 for _ in range(n)]

for i in range(n):
    numArray[i]=int(ssr())
numArray.sort()

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a!=0 and b!=0:
        a=a%b
        if a < b:
            a, b = b, a
    return a

result=numArray[1]-numArray[0]

for i in range(2, n):
    result = gcd(result, numArray[i]-numArray[i-1])
answer=set()
for i in range(2, int(result**0.5)+1):
    if result%i==0:
        answer.add(i)
        answer.add(result//i)
answer = list(answer)
answer.sort()
answer.append(result)
print(*answer)