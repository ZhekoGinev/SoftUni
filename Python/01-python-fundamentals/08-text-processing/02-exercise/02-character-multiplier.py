str1, str2 = input().split()
total = 0

str1 = [ord(n) for n in str1]
str2 = [ord(m) for m in str2]

shorter = len(str1) if len(str1) <= len(str2) else len(str2)
longer = str1 if len(str1) > len(str2) else str2

for _ in range(shorter):
    total += str1.pop(0) * str2.pop(0)

if longer:
    total += sum(longer)

print(total)
