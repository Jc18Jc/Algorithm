n=int(input())

put = [True for _ in range(n)]
check = [[True for _ in range(n)] for _ in range(n)]

count = 0

def bt(num):
    global count
    if num == n:
        count += 1
        return
    for i in range(n):
        if put[i] and check[num][i]:
            put[i]=False
            l=[]
            for j in range(1, n-num):
                if i-j > -1 and check[num+j][i-j]:
                    check[num+j][i-j]=False
                    l.append((num+j, i-j))
                if i+j < n and check[num+j][i+j]:
                    check[num+j][i+j]=False
                    l.append((num+j, i+j))
            bt(num+1)
            put[i]=True
            for item in l:
                check[item[0]][item[1]]=True
            
bt(0)
print(count)