from itertools import permutations

N, M, K = map(int, input().split())
array = list(map(int, input().split()))

answer = 10**10
for perm in permutations(array):
  count = 0
  result = 0
  last = 0
  i = 0
  while count < K:
    if last + perm[i] <= M:
      result+=perm[i]
      last+=perm[i]
    else:
      count+=1
      if count != K:
        last=perm[i]
        result+=perm[i]
    i = (i+1) % N
  answer = min(result, answer)
      
print(answer)