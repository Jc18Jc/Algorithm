n, k = map(int, input().split())
import fractions

m=1000000007
ap = 1
bp = 1
cp = 1
dp = 1

def fact(a):
    result = 1
    for i in range(2, a+1):
        result*=i
        result%=m
    return result

d = fact(k)
for i in range(n):
    dp*=d
    dp%=m

cp = fact(n*k)

for i in range(k, n+k):
    bp*=fact(i)
    bp%=m
    

ap=fact(n*k)
for i in range(2, n):
    ap*=fact(i)
    ap%=m

a=ap*dp
b=bp*cp

Irr = fractions.Fraction(a, b)
a=Irr.numerator
b=Irr.denominator

m2= m-2
tmp = 1
while m2 > 0:
    if m2%2 == 1:
        tmp*=b
        tmp%=m
    b*=b
    b%=m
    m2=m2//2

ans = (a*tmp)%m
print(ans)