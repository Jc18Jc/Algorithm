# 브론즈
while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    print('No' if a <= b else 'Yes')ㄴ