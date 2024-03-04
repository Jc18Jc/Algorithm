import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
inorder, postorder =list(map(int, input().split())), list(map(int, input().split()))
indexList = [-1 for _ in range(n+1)]

for i in range(n):
    indexList[inorder[i]]=i

def dnc(sin, ein, start, end):
    if sin > ein or start > end:
        return
    print(postorder[end], end =' ')
    index = indexList[postorder[end]]
    if index-sin>0:
        dnc(sin, index-1, start, start+index-sin-1)
    if ein-index>0:
        dnc(index+1, ein, start+index-sin, end-1)

dnc(0, n-1, 0, n-1)

### 코드리뷰 ###
# 참고 전혀 안한 코드인데 아이디어부터 구현까지 거의 일치
'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def preorder(in_start, in_end, post_start, post_end):
    if(in_start > in_end) or (post_start > post_end):
        return

    parents = postorder[post_end]
    print(parents, end=" ")

    left = position[parents] - in_start
    right = in_end - position[parents]

    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i

preorder(0, n-1, 0, n-1)
'''