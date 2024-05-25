import sys

x, y = map(int, sys.stdin.readline().split())

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

days = 0

for i in range(1, x):
    days += month[i]

days += y

print(day[days % 7])