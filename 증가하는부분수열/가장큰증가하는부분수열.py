n=int(input())
array = list(map(int, input().split()))

array2 = [0 for _ in range(n)]

for i in range(n):
    tmp = 0
    for j in range(i):
        if tmp < array2[j] and array[i] > array[j]:
            tmp = array2[j]
    array2[i]=tmp+array[i]

print(max(array2))