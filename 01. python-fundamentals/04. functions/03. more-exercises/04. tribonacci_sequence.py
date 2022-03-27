n = int(input())
tribonacci_sequence = []
cache = {}  # for memoization


def tribonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        return cache[n]


for number in range(1, n+1):
    tribonacci_sequence.append(tribonacci(number))

formatted_output = ' '.join([str(i) for i in tribonacci_sequence])
print(formatted_output)
