N=int(input())
for i in range(1, N):
    num = sum(list(map(int, list(str(i)))))+i
    if num==N:
        print(i)
        break
else:
    print(0)