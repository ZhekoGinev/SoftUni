centuries = int(input())

YEARS_PER_CENTURY = 100
DAYS_PER_YEAR = 365.2422
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60

years = YEARS_PER_CENTURY * centuries
days = int(DAYS_PER_YEAR * years)
hours = days * HOURS_PER_DAY
minutes = hours * MINUTES_PER_HOUR

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
