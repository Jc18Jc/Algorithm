l = input()
left, right = 0, len(l)-1
while left < right:
    if l[left]!=l[right]:
        exit(print(0))
    left+=1
    right-=1
print(1)