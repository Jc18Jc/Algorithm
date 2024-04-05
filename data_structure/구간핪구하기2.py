import sys
ssr = sys.stdin.readline

n, m, k = map(int, input().split())

tree = [0]*4*n
numArray = [0]*n
lazy = [0]*4*n

def build(node, start, end):
    if start == end:
        tree[node] = numArray[start]
        return
    mid = (start + end) // 2
    build(node*2, start, mid)
    build(node*2+1, mid+1, end)
    tree[node] = (tree[node*2] + tree[node*2+1])
    return

def query(node, start, end, left, right):
    mid = (start + end)//2
    updateLazy(node, start, end, mid)
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    left_child = query(node*2, start, mid, left, right)
    right_child = query(node*2+1, mid+1, end, left, right)
    return left_child + right_child

def update(node, start, end, left, right, val):
    mid = (start+end)//2
    if left <= start and right >= end:
        lazy[node]+=(end-start+1)*val
    updateLazy(node, start, end, mid)
    if (left <= start and right >= end) or right < start or end < left:
        return
    update(2*node, start, mid, left, right, val)
    update(2*node+1, mid+1, end, left, right, val)
    tree[node] = tree[node*2] + tree[node*2+1]
    return

def updateLazy(node, start, end, mid):
    tree[node]+=lazy[node]
    if start != end:
        lazy[2*node]+=(lazy[node]//(end-start+1))*(mid-start+1)
        lazy[2*node+1]+=(lazy[node]//(end-start+1))*(end-mid)
    lazy[node]=0

for i in range(n):
    numArray[i]=int(ssr())
build(1, 0, n-1)

for i in range(m+k):
    l = list(map(int, ssr().split()))
    if len(l)==3:
        _,b,c = l
        print(query(1, 0, n-1, b-1, c-1))
    else:
        _,b,c,d=l
        update(1, 0, n-1, b-1, c-1, d)

### 코드리뷰 ###
# 구조는 비슷한데 디테일 부분에서 차이가 조금 있네
'''
seg = [0 for _ in range(4040404)]
lazy = [0 for _ in range(4040404)]
 
def init(x, s, e):
    if s == e:
        seg[x] = a[s - 1]
        return seg[x]
    m = s + e >> 1 # 오 ,, mid를 이렇게 쓰는구나 좋은데 ?
    seg[x] = init(x * 2, s, m) + init(x * 2 + 1, m + 1, e)
    return seg[x]
 
def update(x, l, r, s, e, dif):
    updateLazy(x, s, e)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        seg[x] += (e - s + 1) * dif
        if s != e:
            lazy[x * 2] += dif # 아아 lazy에 값 전체를 저장하는게 아니고 dif 하나만 저장해뒀다가 곱해서 더해주는구나, 훨씬 짧아지겠다
            lazy[x * 2 + 1] += dif
        return
    m = s + e >> 1
    update(x * 2, l, r, s, m, dif)
    update(x * 2 + 1, l, r, m + 1, e, dif)
    seg[x] = seg[x * 2] + seg[x * 2 + 1]
 
def updateLazy(x, s, e):
    if lazy[x]:
        seg[x] += (e - s + 1) * lazy[x]
        if s != e:
            lazy[x * 2] += lazy[x]
            lazy[x * 2 + 1] += lazy[x]
        lazy[x] = 0
 
def getSum(x, l, r, s, e):
    updateLazy(x, s, e)
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return seg[x]
    m = s + e >> 1
    return getSum(x * 2, l, r, s, m) + getSum(x * 2 + 1, l, r, m + 1, e)
 
n, q1, q2 = mip()
a = []
for i in range(n):
    a.append(ip()) # ip나 lmip 진짜로 있는건 아니지? ㅋㅋ 선언부를 안보여준거겠지
 
init(1, 1, n)
 
for i in range(q1 + q2):
    q = lmip()
    if q[0] == 1:
        update(1, q[1], q[2], 1, n, q[3])
    else:
        print(getSum(1, q[1], q[2], 1, n))

'''