n, k = map(int, input().split())
if n-k-1 <= k and n-k-1 != 1:
    print('A and B win')
else:
    print('C win')