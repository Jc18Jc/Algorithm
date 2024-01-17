firstNum=input()
firstN=len(firstNum)
firstNum=int(firstNum)
array = [0 for _ in range(10)]

def fun(num, n):
    if n < 1:
        return
    d=10**(n-1)
    t=num//d
    p=(d//10)*(n-1)*t
    for i in range(10):
        array[i]+=p
    for i in range(t):
        array[i]+=d
    array[t]+=(num%d)+1
    fun(num%d, n-1)

fun(firstNum, firstN)

d=10**(firstN-1)
while d > 0:
    array[0]-=d
    d=d//10

print(*array)