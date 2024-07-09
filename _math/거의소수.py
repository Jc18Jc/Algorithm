s, e = map(int, input().split())
sqrte = int(e**0.5)+1
isPrime=[True for _ in range(sqrte)]

answer = 0
for i in range(2, sqrte):
  if isPrime[i]:
    j=2
    while i*j < sqrte:
      isPrime[i*j]=False
      j+=1
    power = i*i
    while power <= e:
      if power >= s:
        answer+=1
      power*=i
print(answer)