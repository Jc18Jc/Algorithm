import sys
ssr = sys.stdin.readline

n = int(ssr())

array = list(map(int, ssr().split()))

left= 0
right= n-1
answerLeft=0
answerRight=n-1
answerSum=array[0]+array[n-1]

array.sort()

while left < right:
    s=array[left]+array[right]
    if abs(s) < abs(answerSum):
        answerSum=s
        answerLeft=left
        answerRight=right
    if s > 0:
        right-=1
    elif s < 0:
        left+=1
    else:
        break
print(array[answerLeft], array[answerRight])
        