import sys
ssr = sys.stdin.readline

L, C = map(int, ssr().split())
array = list(ssr().strip().split())

array.sort()
mo=['a', 'e', 'i', 'o', 'u']

def dfs(k, mcheck, jcheck, l):
    if len(l)==L and mcheck and jcheck>=2:
        for i in range(L):
            print(l[i], end='')
        print()
        return
    if len(l)==L:
        return
    if k >= C:
        return
    if array[k] in mo:
        dfs(k+1, True, jcheck, l+[array[k]])
    else:
        dfs(k+1, mcheck, jcheck+1, l+[array[k]])
    dfs(k+1, mcheck, jcheck, l)

dfs(0, False, 0, [])