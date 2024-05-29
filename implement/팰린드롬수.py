while True:
    num = input()
    if num == '0':
        break
    for i in range(len(num)//2+1):
        if num[i]!=num[len(num)-1-i]:
            print('no')
            break
    else:
        print('yes')