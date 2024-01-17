import sys
ssr = sys.stdin.readline

caseNum = int(ssr())

for _ in range(caseNum):
    n = int(ssr())
    nums = [list(map(int, ssr().split())) for _ in range(2)]

    if n != 1:
        nums[0][1] += nums[1][0]
        nums[1][1] += nums[0][0]

        for i in range(2, n):
            nums[0][i] += max(nums[1][i-1], nums[1][i-2])
            nums[1][i] += max(nums[0][i-1], nums[0][i-2])

    print(max(nums[0][n-1], nums[1][n-1]))