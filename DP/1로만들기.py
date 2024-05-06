from collections import deque
n=int(input())

d=deque()
d.append((n, 0))
visited = [False for _ in range(n+1)]
while d:
    num, c=d.popleft()
    if num == 1:
        print(c)
        break
    if num == 0:
        continue
    if num%3 == 0 and not visited[num//3]:
        d.append((num//3, c+1))
        visited[num//3] = True
    if num%2 == 0 and not visited[num//2]:
        d.append((num//2, c+1))
        visited[num//2] = True
    if not visited[num-1]:
        d.append((num-1, c+1))
        visited[num-1]=True