def result_type(nums):
    if 0 in nums:
        return "zero"
    negatives = 0
    for n in nums:
        if n < 0:
            negatives += 1
    if negatives % 2 == 0:
        return "positive"
    else:
        return "negative"


numbers = [int(input()) for _ in range(3)]
print(result_type(numbers))


###### version 2 ######

# def result_type(nums):
#     if 0 in nums:
#         return "zero"
#     minuses = str(nums).count('-')
#     if minuses % 2 == 0:
#         return "positive"
#     else:
#         return "negative"


# numbers = [int(input()) for _ in range(3)]
# print(result_type(numbers))