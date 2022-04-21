# ideally the validators would have their own class
# but I decided to create them as staticmethods
# also I don't see any reason to use getter and setter
# methods but it's required by the description


class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.__username = self.username_validator(username)
        self.__password = self.password_validator(password)

    @staticmethod
    def username_validator(username):
        if 5 <= len(username) <= 15:
            return username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @staticmethod
    def password_validator(password):
        has_upper = False
        has_digit = False
        has_length = False
        if len(password) >= 8:
            has_length = True
        for ch in password:
            if ch.isupper():
                has_upper = True
            if ch.isdigit():
                has_digit = True
        if has_upper and has_digit and has_length:
            return password
        else:
            raise ValueError(
                "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
            )

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.get_username()}" and password: {"*" * len(self.get_password())}'
