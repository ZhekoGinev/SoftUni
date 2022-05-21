import requests, sys

username = input('Моля въведете github username:  ')

url = f"https://api.github.com/users/{username}"

url_repos = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)
data = response.json()
status = response.status_code

if status != 200:
    print(f"Не е намерен акаунт с име {username}")
    sys.exit()

get_repos = requests.get(url_repos)
repos = get_repos.json()

months = {
    '01': 'Януари',
    '02': 'Февруари',
    '03': 'Март',
    '04': 'Април',
    '05': 'Май',
    '06': 'Юни',
    '07': 'Юли',
    '08': 'Август',
    '09': 'Септември',
    '10': 'Октомври',
    '11': 'Ноември',
    '12': 'Декември',
}

# date created
date = data['created_at'][:10]
date_year, date_month, date_day = date.split('-')

# repos
public_repos_url = []
if len(repos) > 0:
    for url in repos:
        public_repos_url.append(url['html_url'])
    public_repos_url = '\n'.join(public_repos_url)
else:
    public_repos_url = None

name = username if data['name'] == None else data['name']

print()
print(f"Информация за {name}:\n")
print(f"({data['html_url']})\n")
print(f"Акаунтът е създаден на {date_day} {months[date_month]} {date_year}\n")
print(f"""Има {data['public_repos']} публични хранилища:

{public_repos_url}""")