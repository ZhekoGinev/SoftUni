nums = sorted([int(i) for i in input().split()], reverse=True)
avg = sum(nums) / len(nums)
result = [n for n in nums if n > avg][:5]

if len(nums) > 1 and len(set(nums)) > 1:
    print(*result, sep=" ")
else:
    print("No")
