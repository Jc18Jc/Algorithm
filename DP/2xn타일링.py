n=int(input())
array=[0 for _ in range(1001)]
array[1]=1
array[2]=2
for i in range(3, n+1):
    array[i]=array[i-2]+array[i-1]
print(array[n]%10007)