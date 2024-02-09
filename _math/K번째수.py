# 풀 예정

n = int(input())
k = int(input())

array = []
for i in range(1, 101):
    for j in range(1, 101):
        array.append(i*j)

array.sort()

pre=1
count=0
for i in range(500):
    if pre==array[i]:
       count+=1
    else:
        print(pre,'=',count)
        pre=array[i]
        count=1