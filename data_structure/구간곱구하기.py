import sys
ssr = sys.stdin.readline

n, m, k = map(int, input().split())

tree = [0]*4*n
numArray = [0]*n

def build(node, start, end):
    if start == end:
        # 리프 노드라면 원소를 저장한다.
        tree[node] = numArray[start]
        return
    mid = (start + end) // 2
    # 왼쪽 자식으로 재귀
    build(node*2, start, mid)
    # 오른쪽 자식으로 재귀
    build(node*2+1, mid+1, end)
    # 내부 노드라면 자식 노드의 곱을 저장한다.
    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007
    return

def query(node, start, end, left, right):
    if right < start or end < left:
        # 노드가 지정된 범위 밖에 있는 경우
        return 1
    if left <= start and end <= right:
        # 노드가 지정된 범위 안에 있는 경우
        return tree[node]
    # 노드가 지정된 범위 일부에 있는 경우
    mid = (start + end)//2
    left_child = query(node*2, start, mid, left, right)
    right_child = query(node*2+1, mid+1, end, left, right)

    return (left_child * right_child) % 1000000007


def update(node, start, end, index, val):
    if start == end:
        # 리프 노드라면 배열 값을 변경한다.
        tree[node] = val
        return
	
    mid = (start + end) // 2
    # index가 포함된 구간을 가진 자식 노드로 재귀한다.
    if start <= index and index <= mid:
        update(2*node, start, mid, index, val)
    else:
        update(2*node+1, mid+1, end, index, val)
    # 내부 노드라면 두 자식 노드의 합을 저장한다.
    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007
    return


for i in range(n):
    numArray[i]=int(ssr())
build(1, 0, n-1)

for i in range(m+k):
    a, b, c = map(int, ssr().split())
    if a==1:
        update(1, 0, n-1, b-1, c)
    elif a==2:
        print(query(1, 0, n-1, b-1, c-1))
    