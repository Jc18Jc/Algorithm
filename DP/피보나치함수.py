def fibonacci(num):
    if array[num]:
        return array[num]
    a=fibonacci(num-1)
    b=fibonacci(num-2)
    array[num]=[a[0]+b[0], a[1]+b[1]]
    return array[num]


array = [None for _ in range(41)]
array[0] = [1, 0]
array[1] = [0, 1]

for _ in range(int(input())):
    n = int(input())
    print(*fibonacci(n))