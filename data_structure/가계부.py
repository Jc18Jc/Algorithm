import sys
sys.setrecursionlimit(10**5)

def init(node, left, right):
    if left == right:
        seg[node] = nums[left]
        return seg[node]

    mid = (left + right) // 2
    seg[node] = init(node * 2, left, mid) + init(node * 2 + 1, mid + 1, right)
    return seg[node]

def query(node, left, right, start, end):
    if start <= left and end >= right:
        return seg[node]
    elif start > right or end < left:
        return 0
    else:
        mid = (left + right) // 2
        return query(node * 2, left, mid, start, end) + query(
            node * 2 + 1, mid + 1, right, start, end
        )

def update(node, left, right, idx, value):
    if idx < left or idx > right:
        return 0
    if left == idx and right == idx:
        seg[node] += value
        return seg[node]
    
    mid = (left + right) // 2

    if mid >= idx:
        seg[node] = seg[node * 2 + 1] + update(node * 2, left, mid, idx, value)
    else:
        seg[node] = seg[node * 2] + update(node * 2 + 1, mid + 1, right, idx, value)

    return seg[node]

n, q = map(int, sys.stdin.readline().split())
nums = [0] * (n + 1)
seg = [0] * (4 * n)
init(1, 1, n)

for i in range(q):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, 1, n, b, c)
    elif a == 2:
        tmp = query(1, 1, n, b, c)
        print(tmp)