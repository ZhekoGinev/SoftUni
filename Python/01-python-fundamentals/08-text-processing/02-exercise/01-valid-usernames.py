# ▄▄█████████████████████████████─
# ▀▀▀───▀█▄▀▄▀████▀──▀█▄▀▄▀████▀──
# ────────▀█▄█▄█▀──────▀█▄█▄█▀────
# deal with it

print(
    "\n".join(
                [
    username.replace("hhh", "-").replace("uuu", "_")
    for username in input().split(", ")
    if 3 <= len(username) <= 16
    and username.replace("-", "hhh").replace("_", "uuu").isalnum()
                ]
            )
    )
