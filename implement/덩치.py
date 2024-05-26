N=int(input())
array = [list(map(int, input().split())) for _ in range(N)]
l = 1
level = [0] * N

for i in range(N):
    for j in range(N):
        if i != j and array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            l += 1
    level[i] = l
    l = 1

print(*level)