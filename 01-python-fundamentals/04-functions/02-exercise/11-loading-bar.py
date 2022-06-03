number = int(input())


def loading_bar(number):
    loading_bar = ["."] * 10
    number_of_bars = number // 10
    for _ in range(number_of_bars):
        loading_bar.pop()
        loading_bar.insert(0, "%")
    loading_bar = "".join(loading_bar)
    if number < 100:
        return f"{number}% [{loading_bar}]\nStill loading..."
    else:
        return f"100% Complete!\n[{loading_bar}]"


print(loading_bar(number))
