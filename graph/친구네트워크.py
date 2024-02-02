import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10**5)

t = int(ssr())

parents=None
num=None

def find(name):
    if name in parents:
        f = find(parents[name])
        parents[name] = f
        return f
    else:
        return name

def merge(name1, name2):
    name3 = find(name1)
    name4 = find(name2)
    if name3==name4:
        print(num[name4])
        return
    else:
        parents[name3]=name4
        if name4 in num:
            if name3 in num:
                num[name4]+=num[name3]
            else:
                num[name4]+=1
        else:
            if name3 in num:
                num[name4]=num[name3]+1
            else:
                num[name4]=2
        print(num[name4])

for _ in range(t):
    parents = dict()
    num=dict()
    n = int(ssr())
    for _ in range(n):
        name1, name2 = ssr().strip().split()
        merge(name1, name2)