a, b= map(int, input().split())
ta, tb = a, b
while True:
    a, b = max(a, b), min(a, b)
    if a%b==0:
        print(b)
        break
    a = a%b
print((ta*tb)//b)