employee_satisfaction = input().split()
improvement_factor = int(input())

satisfaction = [int(i) * improvement_factor for i in employee_satisfaction]

total_count = len(satisfaction)
average_satisfaction = sum(satisfaction) / total_count

happy = [i for i in satisfaction if i >= average_satisfaction]
happy_count = len(happy)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
