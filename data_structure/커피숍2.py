import sys
ssr = sys.stdin.readline

n, m = map(int, input().split())

tree = [0]*4*n

def build(node, start, end):
    if start == end:
        tree[node] = numArray[start]
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

numArray = list(map(int, input().split()))
build(1, 0, n-1)

for i in range(m):
    a, b, c, d = map(int, ssr().split())
    a, b = min(a, b), max(a, b)
    print(query(1, 0, n-1, a-1, b-1))
    update(1, 0, n-1, c-1, d)