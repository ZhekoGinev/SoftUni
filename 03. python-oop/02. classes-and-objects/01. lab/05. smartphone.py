class Smartphone:
    def __init__(self, memory: int) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int):
        if self.is_on and self.memory - app_memory >= 0:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif not self.is_on and self.memory - app_memory >= 0:
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
