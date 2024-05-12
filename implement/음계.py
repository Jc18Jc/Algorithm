# 음계
import sys

melody = list(map(int, sys.stdin.readline().split()))

isAscending = False
isdescending = False

for i in range(7):
    if melody[i] <melody[i+1]:
        isAscending = True
        continue
    else:
        isAscending = False
        break

for i in range(7):
    if melody[i] >melody[i+1]:
        isdescending = True
        continue
    else:
        isdescending = False
        break

if(isAscending):
    exit(print("ascending"))

if(isdescending):
    exit(print("descending"))

print("mixed")