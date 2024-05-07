def dfs(num):
    if num==0:
        return 1
    t=0
    for num2 in [num-1, num-2, num-3]:
        if num2>-1:
            t+=dfs(num2)
    return t
for _ in range(int(input())):
    print(dfs(int(input())))