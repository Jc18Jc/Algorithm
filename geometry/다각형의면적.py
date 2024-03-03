import sys
input = sys.stdin.readline

n=int(input())
array = [list(map(int, input().split())) for _ in range(n)]

def vectorCross(p1, p2, p3):
    a1, b1 = p2[0]-p1[0], p2[1]-p1[1]
    a2, b2 = p3[0]-p2[0], p3[1]-p2[1]
    return a1*b2-a2*b1

answer = 0
for i in range(n-2):
    p1, p2, p3 = array[0],array[i+1], array[i+2]
    answer+=vectorCross(p1,p2,p3)
print('{:.1f}'.format(abs(answer)/2, 1)) # 오목할 경우를 생각해 외적 값을 다 더한 후 절대값, 각 값마다 절대값 취하면 오목할 때 틀림


### 코드리뷰 ###
# 다각형 면적을 구하는 신발끈 공식을 사용했다고 하는데 외적 이용한 공식은 맞는 듯
'''
import sys
input = sys.stdin.readline

x,y = [],[]
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a); y.append(b)
x.append(x[0]); y.append(y[0])

xr,yr = 0,0
for i in range(n):
    xr+=x[i]*y[i+1]
    yr+=y[i]*x[i+1]
    
print(round(abs((xr-yr)/2),1))
'''