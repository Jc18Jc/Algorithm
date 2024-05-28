import sys
sys.setrecursionlimit(10**5)

def init(node, left, right):
    if left == right:
        seg[node] = nums[left]
        return seg[node]
    mid = (left + right) // 2
    seg[node] = init(node * 2, left, mid) * init(node * 2 + 1, mid + 1, right)
    return seg[node]

def query(node, left, right, start, end):
    if start <= left and end >= right:
        return seg[node]
    elif start > right or end < left:
        return 1
    else:
        mid = (left + right) // 2
        return query(node * 2, left, mid, start, end) * query(
            node * 2 + 1, mid + 1, right, start, end
        )
    
def update(node, left, right, idx, value):
    if idx < left or idx > right:
        return 1
    if left == idx and right == idx:
        seg[node] = value
        return seg[node]
    mid = (left + right) // 2
    if mid >= idx:
        seg[node] = seg[node * 2 + 1] * update(node * 2, left, mid, idx, value)
    else:
        seg[node] = seg[node * 2] * update(node * 2 + 1, mid + 1, right, idx, value)
    return seg[node]


while True:
    try:
        N, K = map(int, input().split())
        nums = [0] + list(map(int, sys.stdin.readline().split()))
        for i in range(1, N + 1):
            if nums[i] < 0:
                nums[i] = -1
            elif nums[i] > 0:
                nums[i] = 1
        seg = [0] * (4 * N)
        init(1, 1, N)

        for _ in range(K):
            t, x, y = sys.stdin.readline().rstrip().split()
            if t == "C":
                if int(y) < 0:
                    y = -1
                elif int(y) > 0:
                    y = 1
                else:
                    y = 0
                update(1, 1, N, int(x), y)
            elif t == "P":
                tmp = query(1, 1, N, int(x), int(y))
                if tmp < 0:
                    print('-', end='')
                elif tmp > 0:
                    print('+', end='')
                else:
                    print('0', end='')
        print()
    except:
        break