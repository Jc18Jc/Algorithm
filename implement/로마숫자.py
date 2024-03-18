import sys
input = sys.stdin.readline

roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
exc = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

roman2 = []
for r in roman.keys():
    roman2.append((roman[r], r))
for r in exc.keys():
    roman2.append((exc[r], r))
roman2.sort(reverse=True)

caseNum = int(input())

for _ in range(caseNum):
    s = input().strip()

    if ord(s[0]) <= 57:
        ans = ""
        s = int(s)
        for r in roman2:
            if s >= r[0]:
                q = s // r[0]
                ans += r[1] * q
                s = s % r[0]
        print(ans)
    else:
        ans = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                tmp = s[i] + s[i + 1]
                ans += exc[tmp]
                i += 2
            else:
                ans += roman[s[i]]
                i += 1
        print(ans)