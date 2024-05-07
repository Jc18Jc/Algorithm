from collections import deque
M=int(input())
K=int(input())
can = list(map(int, input().split()))
array = [True] + [False for _ in range(2000)]

for i in can:
    array[i]=True

for i in range(1, 2001):
    if array[i]:
        continue
    for j in can:
        if i-j > 0 and not array[i-j]:
            array[i]=True
            break

if M <= 2000:
    exit(print(array[:M+1].count(False)))

pattern=[False for _ in range(2001)]

m = 1
for i in range(1, 2001):
    if 