data = [int(i) for i in input().split()]


def negative_positive(numbers: list):
    result = []
    positives = 0
    negatives = 0

    for num in numbers:
        if num > 0:
            positives += num
        else:
            negatives += num

    result.append(negatives)
    result.append(positives)
    if positives < abs(negatives):
        result.append("The negatives are stronger than the positives")
    else:
        result.append("The positives are stronger than the negatives")

    return '\n'.join([str(i) for i in result])


print(negative_positive(data))
