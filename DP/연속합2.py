import sys
N=int(input())
array=list(map(int, sys.stdin.readline().split()))
answer = 0

num = 0
num2 = 0
for i in range(N):
    if array[i] >= 0:
        num+=array[i]
        num2+=array[i]
    else:
        answer = max(answer, num2)
        if num2+array[i] <= 0:
            num2=0
        else:
            num2+=array[i]
        num2 = max(num, num2)
        if num+array[i] <= 0:
            num=0
        else:
            num+=array[i]
answer=max(answer, num, num2)
print(answer if answer != 0 else max(array))