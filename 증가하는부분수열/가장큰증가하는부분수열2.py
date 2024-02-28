# 도무지 시간이 안줄어서 최악의 경우를 하나씩 제거하는 방법으로 해결
import sys
input = sys.stdin.readline
from bisect import bisect_left

n=int(input())
array = list(map(int, input().split()))
array2 = []

i=0
while i < n:
    index = bisect_left(array2, array[i], key=lambda m: m[0])
    tmp = array[i]
    if index != 0:
        tmp += array2[index-1][1]
    j = index
    while j < len(array2):
        if array2[j][1] > tmp:
            break
        j+=1
    if j == index:
        if j == len(array2):
            array2.append([array[i], tmp])
        elif j == 0:
            k = i
            tmpArray = [[array[i], tmp]]
            while k+1 < n and array[k+1] < array[k]:
                tmpArray.append([array[k+1], array[k+1]])
                k+=1
            tmpArray.reverse()
            array2 = tmpArray + array2
            i+=(k-i)
        elif array[i] != array2[j][0]:
            array2.insert(j, [array[i], tmp])
    elif j-1 == index:
        array2[index]=[array[i], tmp]
    else:
        array2 = array2[:index]+[[array[i], tmp]]+array2[j:]
    i+=1

print(array2[-1][1])