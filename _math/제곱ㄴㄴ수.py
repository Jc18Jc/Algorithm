min, max = map(int, input().split())

n=int(max**0.5)

prime = [True for _ in range(n+1)]
p = []
def eratos():
    for i in range(2, n+1):
        if prime[i]:
            p.append(i)
            j=2
            while i*j <= n:
                prime[i*j]=False
                j+=1

eratos()
result = [True for _ in range(max-min+1)]
for item in p:
    d=item**2
    if min%d == 0:
        num2 = min
    else:
        num2 = d*((min//d)+1)
    while num2 <= max:
        result[num2-min]=False
        num2+=d
count=0
for item in result:
    if item:
        count+=1
print(count)