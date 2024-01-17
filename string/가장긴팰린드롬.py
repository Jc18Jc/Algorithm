import sys
ssr = sys.stdin.readline

s1 = list(ssr().strip())
s = '#'.join(s1)
s = '#'+s+'#'

n = len(s)
r, p = -1, -1
res = [0 for _ in range(n)]
count=0

for i in range(1, n):
    if i > r:
        p, r = i, i
        while r < n and 2*p >= r and s[r] == s[2*p-r]: r+=1
        r-=1
        res[i]=r-i
    else:
        j=2*p-i
        if res[j] > r-i:
            res[i] = r-i
        elif res[j] == r-i:
            p= i
            while r < n and 2*p >= r and s[r] == s[2*p-r]: r+=1
            r-=1
            res[i]=r-i
        else:
            res[i]=res[j]
    count += ((res[i]-1)//2)+1

print(count)