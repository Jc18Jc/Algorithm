N, r, c = map(int, input().split())
def dnv(n, answer):
    global r, c
    if n == -1:
        return answer
    p = 2**n
    if r >= p:
        answer+=p*p*2
        r-=p
    if c >= p:
        answer+=p*p
        c-=p
    return dnv(n-1, answer)

print(dnv(N-1, 0))


### 코드리뷰 ###
'''
N, r, c = map(int, input().split())

ans = 0

while N != 0: # 내것보다 가독성 좋은 듯, 원리는 같음

	N -= 1

	# 1사분면
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0

	# 2사분면
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
        
	# 3사분면    
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
        
	# 4사분면    
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)
'''