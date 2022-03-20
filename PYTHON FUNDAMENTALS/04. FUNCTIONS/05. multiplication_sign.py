x = int(input())
y = int(input())
z = int(input())

number_of_minuses = 0

for i in (x, y, z):
    if i < 0:
        number_of_minuses += 1

if 0 in (x, y, z):
    print("zero")
elif number_of_minuses % 2 == 0:
    print("positive")
else:
    print("negative")
