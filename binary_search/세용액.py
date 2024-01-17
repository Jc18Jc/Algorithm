import sys
ssr=sys.stdin.readline

n=int(ssr())

array = list(map(int, ssr().split()))

array.sort()

answerLeft = 0
answerRight = n-1
answerMiddle = 1
answerSum = array[0]+array[1]+array[n-1]

flag=False

for i in range(n-2):
    left=i+1
    right=n-1
    while left < right:
        tmp = array[i]+array[left]+array[right]
        if abs(answerSum) > abs(tmp):
            answerLeft=i
            answerMiddle=left
            answerRight=right
            answerSum=tmp
        if tmp == 0:
            flag=True
            break
        if tmp > 0:
            right-=1
        elif tmp < 0:
            left+=1
    if flag:
        break

print(array[answerLeft], array[answerMiddle], array[answerRight])