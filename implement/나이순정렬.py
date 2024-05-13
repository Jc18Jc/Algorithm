import sys
N=int(input())
name = [None for _ in range(N)]
array = [None for _ in range(N)]
for i in range(N):
    a, b = sys.stdin.readline().split()
    array[i], name[i] = [int(a), i], b
array.sort()
for i in range(N):
    print(str(array[i][0]), name[array[i][1]])