K, P, N = map(int, input().split())
T = 1000000007
p = P
for i in range(9):
  p *= P
  p %= T

def bin(num):
  if num == 0:
    return 1
  if num == 1:
    return p
  left = num//2
  right = num-left
  leftResult = bin(left)
  if left==right:
    return (leftResult*leftResult)%T
  else:
    return (leftResult*leftResult*p)%T
  
print((K*bin(N))%T)