N, k = map(int, input().split())

o = 1
m = 9

while k > o*m:
  k -= o*m
  o+=1
  m*=10

l = (k-1)//o
digit = (k-1)%o

number = (m//9)+l
strNumber = str(number)

print(strNumber[digit] if number <= N else -1)