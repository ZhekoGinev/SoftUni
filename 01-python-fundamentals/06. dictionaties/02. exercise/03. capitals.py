countries = dict(zip(input().split(", "), input().split(", ")))

for country, capitol in countries.items():
    print(f"{country} -> {capitol}")
