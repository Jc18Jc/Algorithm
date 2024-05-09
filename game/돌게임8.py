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

pl = 0
for i in range(1, 2001):
    tmp = array[1:i+1]
    k=1
    while k+i <= 2001:
        if array[k:k+i] == tmp:
            k+=i
        else:
            break
    else:
        pl=i
        break
for i in range(1, 23):
    print(i, array[i])
firstAnswer = array[:pl+1].count(False)
answer = (M//pl)*firstAnswer
answer+=array[:(M%pl)+1].count(False)
print(answer)