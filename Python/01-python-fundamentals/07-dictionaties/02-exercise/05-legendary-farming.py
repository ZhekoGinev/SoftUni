from collections import defaultdict

legendaries = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
junk = defaultdict(int)
is_found = False
legendary_item = ""

while True:
    materials = input().lower().split()
    mats = [i for i in materials if not i.isdigit()]
    quantity = [int(i) for i in materials if i.isdigit()]

    for k, v in zip(mats, quantity):
        if k in legendaries:
            legendaries[k] += v
        else:
            junk[k] += v

        if legendaries["shards"] >= 250:
            legendary_item = "Shadowmourne"
            legendaries["shards"] -= 250
            is_found = True
            break
        if legendaries["fragments"] >= 250:
            legendary_item = "Valanyr"
            legendaries["fragments"] -= 250
            is_found = True
            break
        if legendaries["motes"] >= 250:
            legendary_item = "Dragonwrath"
            legendaries["motes"] -= 250
            is_found = True
            break
    if is_found:
        break

print(f"{legendary_item} obtained!")
print(f"shards: {legendaries['shards']}")
print(f"fragments: {legendaries['fragments']}")
print(f"motes: {legendaries['motes']}")
for item, value in junk.items():
    print(f"{item}: {junk[item]}")
