import sys
input = sys.stdin.readline

N, K = map(int, input().split())
prod = []
robot = []
l=list(input().strip())

for i in range(N):
  if l[i]=='H':
    prod.append(i)
  else:
    robot.append(i)

pi = 0
ri = 0
answer = 0

while len(prod) != pi and len(robot) != ri:
  if robot[ri]-K<=prod[pi] and robot[ri]+K>=prod[pi]:
    answer+=1
    pi+=1
    ri+=1
  elif robot[ri]-K>prod[pi]:
    pi+=1
  elif robot[ri]+K<prod[pi]:
    ri+=1

print(answer)