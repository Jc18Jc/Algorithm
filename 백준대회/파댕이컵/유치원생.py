import sys
ssr = sys.stdin.readline

t = int(ssr())
n = int(ssr())
l = map(int, ssr().split())

if sum(l) >= t:
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')