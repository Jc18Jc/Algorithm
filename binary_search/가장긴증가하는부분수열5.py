import sys
ssr = sys.stdin.readline
from bisect import bisect_right, bisect_left

n = int(ssr())

array=list(map(int, ssr().split()))
an=[]


class linked:
    def __init__(self, value):
        self.left=None
        self.value=value

linkedArray=[]

index=-1
for i in range(0, n):
    t = bisect_left(an, array[i])
    if index < t:
        an.append(array[i])
        index+=1
        linkedArray.append(None)
    else:
        an[t]=array[i]
    l=linked(array[i])
    if t>0:
        l.left=linkedArray[t-1]
    linkedArray[t]=l


print(index+1)
answer=[0 for _ in range(index+1)]
tmp=index
l=linkedArray[index]
while l.left:
    answer[tmp]=l.value
    tmp-=1
    l=l.left
answer[0]=l.value
print(*answer)
    
