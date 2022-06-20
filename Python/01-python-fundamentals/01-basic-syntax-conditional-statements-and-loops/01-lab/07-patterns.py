size = int(input())
for i in range(1, size*2):
    print(i * "*" if i <= size else (size*2 - i) * "*")
