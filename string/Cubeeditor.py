import sys
ssr = sys.stdin.readline

s=list(ssr().strip())
n=len(s)

check = [[True for _ in range(n)] for _ in range(n)]
'''
for i in range(n):
    for j in range(i+1, n):
        eq[i][j]=s[i]==s[j]
'''

answer=0
for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j] and check[i][j]:
            count=1
            check[i][j]=False
            tmpi=i+1
            tmpj=j+1
            while tmpi < n and tmpj < n:
                if s[tmpi] == s[tmpj] and check[tmpi][tmpj]:
                    check[tmpi][tmpj]=False
                    count+=1
                    tmpi+=1
                    tmpj+=1
                else: break
            answer = answer if answer > count else count

print(answer)
                
            