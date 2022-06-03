number = int(input())


def loading_bar(number):
    loading_bar = ["."] * 10
    number_of_bars = number // 10
    for _ in range(number_of_bars):
        loading_bar.pop()
        loading_bar.insert(0, "%")
    loading = "".join(loading_bar)
    if number < 100:
        return f"{number}% [{loading}]\nStill loading..."
    else:
        return f"100% Complete!\n[{loading}]"


print(loading_bar(number))
