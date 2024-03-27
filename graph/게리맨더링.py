from itertools import combinations
N=int(input())
people = [0]+list(map(int, input().split()))
E = [[] for _ in range(N+1)]
for i in range(1,N+1):
    _, *a = list(map(int, input().split()))
    E[i]=a

def check(combs):
    first=[]
    second=[]
    for j in range(1, N+1):
        if j in combs:
            stc=[j]
            first.append(j)
            firstTotal=people[j]
            while stc:
                v=stc.pop()
                for node in E[v]:
                    if node not in first and node in combs:
                        stc.append(node)
                        first.append(node)
                        firstTotal+=people[node]
            break
    for j in range(1,N+1):
        if j not in combs:
            stc=[j]
            second.append(j)
            secondTotal = people[j]
            while stc:
                v=stc.pop()
                for node in E[v]:
                    if node not in second and node not in combs:
                        stc.append(node)
                        second.append(node)
                        secondTotal+=people[node]
            break
    if len(second)+len(first) == N:
        return abs(firstTotal-secondTotal)
    return 10000

def gm():
    nums = range(1, N+1)
    answer = 10000
    for i in range(1, N):
        for combs in combinations(nums, i):
            answer = min(answer, check(combs))
    return answer

def main():
    visited = [False for _ in range(N+1)]
    l=[]
    for i in range(1, N+1):
        if not visited[i]:
            stc = [i]
            visited[i]=True
            tmp = people[i]
            while stc:
                v=stc.pop()
                for node in E[v]:
                    if not visited[node]:
                        visited[node]=True
                        stc.append(node)
                        tmp+=people[node]
            l.append(tmp)
    if len(l) == 1:
        print(gm())
    elif len(l) == 2:
        print(abs(l[0]-l[1]))
    else:
        print(-1)

main()


### 코드리뷰 ###
'''
from itertools import combinations
n = int(input())
arr = tuple(map(int, input().split()))
aa = sum(arr)
d = {}
for i in range(1, n+1):
    _, *a = map(int, input().split()) # *a는 길이를 알 수 없는 인자가 들어올 때 받을 수 있음, 굿
    d[i] = set(a)
def func(l):
    q = [l.pop()]
    while q:
        _q = []
        for qq in q:
            for dd in d[qq]:
                if dd in l:
                    _q.append(dd)
                    l.remove(dd)
        q = _q
    if l: return False
    return True
ans = 987654321
for i in range(1, n // 2 + 1): # 아 N까지가 아니고 절반까지만 해도 되는구나 맞네
    for comb in combinations(range(1, n+1), i):
        _comb = list(comb)
        if func(_comb) and func([i for i in range(1, n+1) if i not in comb]):
            ans = min(ans, abs(sum([arr[i-1] for i in range(1, n+1) if i not in comb]) - sum([arr[i-1] for i in comb])))
if ans > 99999:
    print(-1)
else:
    print(ans)
'''
### 수정코드 ###
'''
from itertools import combinations
N=int(input())
people = [0]+list(map(int, input().split()))
E = [[] for _ in range(N+1)]
for i in range(1,N+1):
    _, *a = list(map(int, input().split()))
    E[i]=a

def check(combs):
    first=combs
    second=[i for i in range(1, N+1) if i not in combs]
    count=2
    s=first.pop()
    stc=[s]
    firstTotal=people[s]
    while stc:
        v=stc.pop()
        for node in E[v]:
            if node in first:
                stc.append(node)
                firstTotal+=people[node]
                first.remove(node)
                count+=1
    s=second.pop()
    stc=[s]
    secondTotal = people[s]
    while stc:
        v=stc.pop()
        for node in E[v]:
            if node in second:
                stc.append(node)
                secondTotal+=people[node]
                second.remove(node)
                count+=1
    if count == N:
        return abs(firstTotal-secondTotal)
    return 10000

def gm():
    nums = range(1, N+1)
    answer = 10000
    for i in range(1, N):
        for combs in combinations(nums, i):
            answer = min(answer, check(list(combs)))
    print(answer if answer != 10000 else -1)

gm()
'''