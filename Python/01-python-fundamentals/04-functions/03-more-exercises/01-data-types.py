data_type = input()
value = input()


def data_fn(type, value):
    if type == "int":
        return int(value) * 2
    elif type == "real":
        return f"{(float(value) * 1.5):.2f}"
    elif type == "string":
        return f"${value}$"


print(data_fn(data_type, value))
