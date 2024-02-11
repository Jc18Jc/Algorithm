n = int(input())
k = int(input())

s = 1
e = n * n
ans = 0
while s <= e:
    mid = (s+e)//2
    total = 0
    for i in range(1, n+1):
        if i > mid:
            break
        tmp = mid//i
        if tmp > n:
            tmp=n
        total += tmp
    if total < k:
        s=mid+1
    elif total >= k:
        ans=mid
        e=mid-1
print(ans)


### 코드리뷰 ###
'''
N, K = int(input()), int(input()) # 오,, 새로운 방법
start, end = 1, K     # end를 n*n으로 잡았는데 당연하게도 k가 더 효율적일듯, 시간 996->840 변화

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        # k가 작은데 n이 큰 경우 브레이크가 없어서 조금 비효율적일 수도 ..?
        # 아니 ,직접 해보니까 오히려 빠름 if 검사하는게 줄어서 그런가 ? 최악의 케이스는 사실 k도 큰 경우라서 차라리 없는게 나은듯 ..
        temp += min(mid//i, N) # 나는 mid//i를 따로 변수로 두고 n보다 크면 n으로~ 복잡하게 했는데 이런 방법도 있네, 근데 시간이 엄청 늘어남, 이건 왜지
    
    if temp >= K: #이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
'''