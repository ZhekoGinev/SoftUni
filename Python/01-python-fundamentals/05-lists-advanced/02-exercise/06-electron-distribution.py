number_of_electrons = int(input())
shell = []

for e in range(1, number_of_electrons + 1):
    max_electrons = 2 * e**2
    if number_of_electrons >= max_electrons:
        shell.append(max_electrons)
        number_of_electrons -= max_electrons
        if number_of_electrons == 0:
            break
    else:
        shell.append(number_of_electrons)
        break

print(shell)
