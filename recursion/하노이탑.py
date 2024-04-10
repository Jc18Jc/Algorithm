n=int(input())

i=0
count=0
while i < n:
    count=count*2+1
    i+=1
print(count)
if n > 20:
    exit()
def rec(num, cur, aim):
    if num == 1:
        print(cur, aim)
        return
    if cur == 1:
        if aim == 2:
            rec(num-1, cur, 3)
            print(cur, aim)
            rec(num-1, 3, aim)
        if aim == 3:
            rec(num-1, cur, 2)
            print(cur, aim)
            rec(num-1, 2, aim)
    if cur == 2:
        if aim == 1:
            rec(num-1, cur, 3)
            print(cur, aim)
            rec(num-1, 3, aim)
        if aim == 3:
            rec(num-1, cur, 1)
            print(cur, aim)
            rec(num-1, 1, aim)
    
    if cur == 3:
        if aim == 1:
            rec(num-1, cur, 2)
            print(cur, aim)
            rec(num-1, 2, aim)
        if aim == 2:
            rec(num-1, cur, 1)
            print(cur, aim)
            rec(num-1, 1, aim)

rec(n, 1, 3)