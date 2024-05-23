import sys

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    answer=(num+1)*(num//2)
    if num%2: answer+=(num//2)+1
    for i in range(1, num//2+1):
        answer+=i*((num//i)-1)
    print(answer)