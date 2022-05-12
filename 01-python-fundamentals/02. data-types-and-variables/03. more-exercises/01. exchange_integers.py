a = int(input())
b = int(input())

print("Before:")
print(f"a = {a}\nb = {b}")

a, b = b, a

print(f"After:")
print(f"a = {a}\nb = {b}")
