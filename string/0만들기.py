import sys
ssr = sys.stdin.readline

n = int(ssr())

def dfs(num, des, sign, exp, realexp):  
    realexp+=sign+str(num)
    if sign=='':
        exp+=' '+str(num)
    else:
        exp+=sign+str(num)
    hap=eval(realexp)
    if num==des:
        if hap==0:
            print(exp)
        return
    dfs(num+1, des, '', exp, realexp)
    dfs(num+1, des, '+', exp, realexp)
    dfs(num+1, des, '-', exp, realexp)
    
        

for _ in range(n):
    m=int(ssr())
    dfs(2, m, '', '1', '1')
    dfs(2, m, '+', '1', '1')
    dfs(2, m, '-', '1', '1')
    print()
