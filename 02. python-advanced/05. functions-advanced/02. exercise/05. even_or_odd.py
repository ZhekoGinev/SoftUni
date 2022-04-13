def even_odd(*args):
    data = list(args)
    command = data.pop()
    if command == "even":
        return [n for n in data if n % 2 == 0]
    elif command == "odd":
        return [n for n in data if n % 2 != 0]
