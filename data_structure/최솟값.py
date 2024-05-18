import sys
ssr = sys.stdin.readline

n, m = map(int, input().split())

tree1 = [0]*4*n
tree2 = [0]*4*n
numArray = [0]*n

def build2(node, start, end):
    if start == end:
        # 리프 노드라면 원소를 저장한다.
        tree2[node] = numArray[start]
        return
    mid = (start + end) // 2
    # 왼쪽 자식으로 재귀
    build2(node*2, start, mid)
    # 오른쪽 자식으로 재귀
    build2(node*2+1, mid+1, end)
    # 내부 노드라면 자식 노드 중 작은 값을 저장한다.
    tree2[node] = tree2[node*2] if tree2[node*2] < tree2[node*2+1] else tree2[node*2+1]
    return

def query2(node, start, end, left, right):
    if right < start or end < left:
        # 노드가 지정된 범위 밖에 있는 경우
        return 1000000000
    if left <= start and end <= right:
        # 노드가 지정된 범위 안에 있는 경우
        return tree2[node]
    # 노드가 지정된 범위 일부에 있는 경우
    mid = (start + end)//2
    left_child = query2(node*2, start, mid, left, right)
    right_child = query2(node*2+1, mid+1, end, left, right)

    return left_child if left_child < right_child else right_child

for i in range(n):
    numArray[i]=int(ssr())
build2(1, 0, n-1)

for i in range(m):
    a, b = map(int, ssr().split())
    print(query2(1, 0, n-1, a-1, b-1))