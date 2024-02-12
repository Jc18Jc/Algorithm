n=int(input())

array = [0 for _ in range(n+1)]
array[1]=1
array2 =[0 for _ in range(n+1)]
array2[1]=1

for i in range(2, n+1):
    array[i]=array[i-1]*2+1

for i in range(2, n+1):
    array2[i]=array[i-2]+array2[i-2]+3


print(array2[n])

def rec(num, cur, aim):
    if num==0:
        return
    if num==1:
        print(cur, aim)
        return
    if aim == 'A':
        if cur == 'B':
            rec(num-1, cur, 'C')
            print(cur, aim)
            rec(num-1, 'C', aim)
        elif cur == 'C':
            rec(num-1, cur, 'B')
            print(cur, aim)
            rec(num-1, 'B', aim)
    elif aim == 'B':
        if cur == 'A':
            rec(num-1, cur, 'C')
            print(cur, aim)
            rec(num-1, 'C', aim)
        elif cur == 'C':
            rec(num-1, cur, 'A')
            print(cur, aim)
            rec(num-1, 'A', aim)
    elif aim == 'C':
        if cur == 'A':
            rec(num-1, cur, 'B')
            print(cur, aim)
            rec(num-1, 'B', aim)
        elif cur == 'B':
            rec(num-1, cur, 'A')
            print(cur, aim)
            rec(num-1, 'A', aim)
    elif aim=='D':
        if cur=='A':
            rec(num-2, cur, 'C')
            print(cur, 'B')
            print(cur, aim)
            print('B', aim)
            rec(num-2, 'C', aim)
        if cur=='B':
            rec(num-2, cur, 'C')
            print(cur, 'A')
            print(cur, aim)
            print('A', aim)
            rec(num-2, 'C', aim)
        if cur=='C':
            rec(num-2, cur, 'B')
            print(cur, 'A')
            print(cur, aim)
            print('A', aim)
            rec(num-2, 'B', aim)

rec(n, 'A', 'D')