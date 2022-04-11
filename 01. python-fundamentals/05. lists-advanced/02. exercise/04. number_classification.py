numbers = [int(num) for num in input().split(", ")]

positive = ', '.join([str(i) for i in numbers if i >= 0])
negative = ', '.join([str(i) for i in numbers if i < 0])
even = ', '.join([str(i) for i in numbers if i % 2 == 0])
odd = ', '.join([str(i) for i in numbers if i % 2 != 0])


print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
