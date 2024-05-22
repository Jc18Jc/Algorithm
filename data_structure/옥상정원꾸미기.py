import sys
N = int(input())
array = list(int(sys.stdin.readline()) for _ in range(N))
stc=[]
answer=0
for i in range(N):
    num = array[i]
    while stc and stc[-1] <= num:
        stc.pop()
    answer+=len(stc)
    stc.append(num)
print(answer)