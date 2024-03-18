roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
exc = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

roman2 = []
for r in roman.keys():
    roman2.append((roman[r], r))
for r in exc.keys():
    roman2.append((exc[r], r))
roman2.sort(reverse=True)

num1 = input()
num2 = input()

total = 0
i = 0
while i < len(num1):
    if i < len(num1) - 1 and roman[num1[i]] < roman[num1[i + 1]]:
        tmp = num1[i] + num1[i + 1]
        total += exc[tmp]
        i += 2
    else:
        total += roman[num1[i]]
        i += 1

i = 0
while i < len(num2):
    if i < len(num2) - 1 and roman[num2[i]] < roman[num2[i + 1]]:
        tmp = num2[i] + num2[i + 1]
        total += exc[tmp]
        i += 2
    else:
        total += roman[num2[i]]
        i += 1

print(total)

total_str = []
for i in range(len(roman2)):
    t = total // roman2[i][0]
    for _ in range(t):
        total_str.append(roman2[i][1])
        total -= roman2[i][0]

print(''.join(total_str))