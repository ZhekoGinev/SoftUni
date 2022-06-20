n_snowballs = int(input())
balls = {}

for _ in range(n_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = int((weight / time) ** quality)

    balls[value] = [weight, time, quality]

result = sorted(balls.items(), key=lambda b: -b[0])[0]
v, w, t, q = result[0], result[1][0], result[1][1], result[1][2]
print(f"{w} : {t} = {v} ({q})")