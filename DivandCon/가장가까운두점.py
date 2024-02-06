import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
array.sort()

def calDist(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def dnC(si, ei):
    p1 = array[si]
    p2 = array[si+1]
    if ei - si == 2:
        p3 = array[si+2]
        return min(calDist(p1, p2), calDist(p2, p3), calDist(p1, p3))
    elif ei - si == 1:
        return calDist(p1,p2)
    midi = (si+ei)//2
    minD = min(dnC(si, midi),dnC(midi+1, ei))
    pList = []
    for i in range(midi, si-1, -1):
        if (array[midi][0]-array[i][0])**2 >= minD:
            break
        pList.append(array[i])
    for i in range(midi+1, ei+1):
        if (array[midi][0]-array[i][0])**2 >= minD:
            break
        pList.append(array[i])
    pList.sort(key = lambda x:x[1])
    for i in range(len(pList)-1):
        for j in range(i+1, len(pList)):
            if (pList[j][1]-pList[i][1])**2 >= minD:
                break
            minD = min(calDist(pList[i], pList[j]), minD)
    return minD
    
print(dnC(0, n-1))


### 코드 리뷰 ###
# 블로그 코드 대신 나의 두 개 코드 비교
# 블로그 코드는 위와 거의 일치
'''
import sys
input = sys.stdin.readline
n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
array.sort()

def calDist(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def dnC(si, ei):
    p1 = array[si]
    p2 = array[si+1]
    if ei - si == 2:
        p3 = array[si+2]
        return min(calDist(p1, p2), calDist(p2, p3), calDist(p1, p3))
    elif ei - si == 1:
        return calDist(p1,p2)
    midi = (si+ei)//2
    minD = min(dnC(si, midi),dnC(midi+1, ei))
    leftPList = [] # 여기부터 차이, 기존의 코드가 범위에 포함되는 모든 점들을 한 리스트에 넣었다면 나는 왼쪽 오른쪽을 분리함
    rightPList = [] # 왼쪽 내의 혹은 오른쪽 내의 점들끼리는 이미 가장 작은 점을 반환했음, 그래서 왼쪽 오른쪽 나눠서 불필요한 비교를 제외
    for i in range(midi, si-1, -1):  # 왼쪽 오른쪽 나눠서 리스트에 담아야해서 코드 줄 수는 길어지고 더러워지긴 함
        if (array[midi][0]-array[i][0])**2 >= minD:
            break
        leftPList.append(array[i])
    for i in range(midi+1, ei+1):
        if (array[midi][0]-array[i][0])**2 >= minD:
            break
        rightPList.append(array[i])
    leftPList.sort(key=lambda x:x[1])
    rightPList.sort(key=lambda x:x[1])
    rsi = 0 # 왼쪽 점마다 모든 오른쪽 점들을 비교할 수 없으므로 오른쪽 점 중 가장 처음 시작할 인덱스를 저장
    for i in range(len(leftPList)):
        if rsi >= len(rightPList): break
        flag=0 
        while len(rightPList) > rsi:    # 시작할 인덱스를 업데이트
            if leftPList[i][1] < rightPList[rsi][1] and (leftPList[i][1]-rightPList[rsi][1])**2 >= minD: # 가능한 y값을 초과 한 경우
                flag=1
                break
            if (leftPList[i][1]-rightPList[rsi][1])**2 < minD:  # 가능한 y값 안에 들어왔을 경우
                break
            rsi+=1 # 가능한 y값 안에 들어오기 전
        if flag:
            continue
        for j in range(rsi, len(rightPList)):
            if (leftPList[i][1]-rightPList[j][1])**2 >= minD:
                break
            minD = min(calDist(leftPList[i], rightPList[j]), minD)
    return minD
    
print(dnC(0, n-1))

'''