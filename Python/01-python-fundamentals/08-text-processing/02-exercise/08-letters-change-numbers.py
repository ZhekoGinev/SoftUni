data = input().split()
res = 0


# return position in the alphabet
def position_alpha(letter: str):
    if letter.isupper():
        result = ord(letter) - 64
    elif letter.islower():
        result = ord(letter) - 96
    return result


for element in data:
    lead_letter = element[0]
    trail_letter = element[-1]
    element = int(element[1:-1])

    if lead_letter.isupper():
        element /= position_alpha(lead_letter)
    elif lead_letter.islower():
        element *= position_alpha(lead_letter)
    
    if trail_letter.isupper():
        element -= position_alpha(trail_letter)
    elif trail_letter.islower():
        element += position_alpha(trail_letter)
    
    res += element

print(f"{res:.2f}")