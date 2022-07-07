from collections import defaultdict

companies = defaultdict(list)

while True:
    data = input()
    if data == "End":
        break

    company, employee_id = data.split(" -> ")
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company, ids in companies.items():
    print(company)
    for id in ids:
        print(f"-- {id}")