import sys
ssr = sys.stdin.readline

n, k = map(int, ssr().split())

array = []

for _ in range(n):
    a, b = map(int, ssr().split())
    array.append(b-a)

array.sort()

if array[k-1] <= 0:
    print(0)
else:
    print(array[k-1])