n = int(input())
full_list = []

for _ in range(n):
    full_list.append(int(input()))

command = input()

if command == "even":
    print(f"{[num for num in full_list if num % 2 == 0]}")
elif command == "odd":
    print(f"{[num for num in full_list if num % 2 != 0]}")
elif command == "positive":
    print(f"{[num for num in full_list if num >= 0]}")
elif command == "negative":
    print(f"{[num for num in full_list if num < 0]}")
