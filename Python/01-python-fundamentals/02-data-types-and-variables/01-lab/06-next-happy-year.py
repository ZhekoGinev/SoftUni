year = int(input())
n = year

while True:
    n += 1
    numstring = str(n)
    if len(set(str(n))) == len(str(year)):
        print(n)
        break
