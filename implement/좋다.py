n=int(input())

array = list(map(int, input().split()))
array.sort()
count = 0

for i in range(n):
    start=0
    end=n-1
    num=array[i]
    while start < end:
        if start==i:
            start+=1
            continue
        if end==i:
            end-=1
            continue
        tmp = array[start]+array[end]
        if tmp==num:
            count+=1
            break
        if tmp > num:
            end-=1
        elif tmp < num:
            start+=1
    
print(count)

### 코드리뷰 ###
'''
import sys

if __name__ == '__main__': # 인터프리터로 실행했을 때만 동작하라는 의미, 다른 곳에서 임포트 되어 사용되면 동작 안함, 코테에서 쓸 일은 없을 듯
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    ans = 0

    for i in range(N):
        tmp = arr[:i] + arr[i + 1:] # 매번 배열을 이렇게 만들어주는구나, 자기 자신 제외하는 코드가 필요없어지긴 할 듯
        left, right = 0, len(tmp) - 1
        while left < right:
            t = tmp[left] + tmp[right]
            if t == arr[i]:
                ans += 1
                break
            if t < arr[i]: left += 1 # t 를 증가시켜야 하므로 left 증가
            else: right -= 1 # t 를 감소시켜야 하므로 right 감소
    print(ans)
'''