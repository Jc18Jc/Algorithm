t = int(input())

for _ in range(t):
    s, e = map(int, input().split())
    num = e-s
    if num == 1:
        print(1)
        continue
    if num == 2:
        print(2)
        continue
    num-=2
    i = 0
    p = 2
    o = False
    count=1
    while i + p < num:
        i+=p
        if o:
            p+=1
            o=False
        else:
            o=True
        count+=1
    print(count+2)