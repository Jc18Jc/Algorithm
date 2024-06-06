def max_plums(T, W, drops):
    dp = [[[0] * 3 for _ in range(W + 1)] for _ in range(T + 1)]
    if drops[0] == 1:
        dp[1][0][1] = 1
    else:
        dp[1][1][2] = 1
    for t in range(2, T + 1):
        for w in range(W + 1):
            if drops[t - 1] == 1:
                dp[t][w][1] = dp[t - 1][w][1] + 1
                if w > 0:
                    dp[t][w][1] = max(dp[t][w][1], dp[t - 1][w - 1][2] + 1)
                dp[t][w][2] = dp[t - 1][w][2]
                if w > 0:
                    dp[t][w][2] = max(dp[t][w][2], dp[t - 1][w - 1][1])
            else:
                dp[t][w][2] = dp[t - 1][w][2] + 1
                if w > 0:
                    dp[t][w][2] = max(dp[t][w][2], dp[t - 1][w - 1][1] + 1)
                dp[t][w][1] = dp[t - 1][w][1]
                if w > 0:
                    dp[t][w][1] = max(dp[t][w][1], dp[t - 1][w - 1][2])
    
    max_plums = 0
    for w in range(W + 1):
        max_plums = max(max_plums, dp[T][w][1], dp[T][w][2])
    return max_plums

T, W = map(int, input().split())
drops = list(int(input()) for _ in range(T))
print(max_plums(T, W, drops))
