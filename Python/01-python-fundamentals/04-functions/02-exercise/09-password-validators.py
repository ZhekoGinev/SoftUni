password = input()


# validators
def validate_length(password: str):
    if 6 <= len(password) <= 10:
        return True
    else:
        return "Password must be between 6 and 10 characters"


def validate_alphanumeric(password: str):
    if password.isalnum():
        return True
    else:
        return "Password must consist only of letters and digits"


def validate_digits(password: str):
    digit_count = 0
    for i in password:
        if i.isdigit():
            digit_count += 1

    if digit_count >= 2:
        return True
    else:
        return "Password must have at least 2 digits"


def validate_password(password):
    validators = (validate_length(password),
                  validate_alphanumeric(password),
                  validate_digits(password))
    errors = [v for v in validators if v != True]

    if validate_length(password) == True \
            and validate_alphanumeric(password) == True \
            and validate_digits(password) == True:
        print("Password is valid")
    else:
        for i in errors:
            print(i)


validate_password(password)
