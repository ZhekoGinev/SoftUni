year = int(input())
for i in range(year+1, year*101):
    numstring = str(i)
    if len(set(numstring)) == len(str(year)):
        print(i)
        break
