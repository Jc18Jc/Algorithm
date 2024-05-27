import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

stack = []
count = [0 for _ in range(1000001)]
ans = [-1 for _ in range(n)]

for num in nums:
    count[num] += 1

for i in range(n):
    num = nums[i]
    while stack and stack[-1][0] < count[num]:
        _, idx = stack.pop()
        ans[idx] = num
    stack.append((count[num], i))

print(*ans)