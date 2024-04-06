import sys

def build(node, start, end):
    if start == end:
        tree[node] = 1 if start < n else 0
        return
    mid = (start + end) // 2
    build(node*2, start, mid)
    build(node*2+1, mid+1, end)
    tree[node] = tree[node*2] + tree[node*2+1]
    return

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end)//2
    left_child = query(node*2, start, mid, left, right)
    right_child = query(node*2+1, mid+1, end, left, right)
    return left_child + right_child

def update(node, start, end, index, val):
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    if start <= index and index <= mid:
        update(2*node, start, mid, index, val)
    else:
        update(2*node+1, mid+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]
    return

for _ in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, sys.stdin.readline().split()))
    tree = [0]*4*(n+m)
    numIndex = [n-i-1 for i in range(n)]
    build(1, 0, n+m-1)
    for j in range(m):
        tmp=array[j]-1
        print(query(1, 0, n+m-1, numIndex[tmp]+1, n+j), end=' ')
        update(1, 0, n+m-1, numIndex[tmp], 0)
        update(1, 0, n+m-1, n+j, 1)
        numIndex[tmp]=n+j
    print()