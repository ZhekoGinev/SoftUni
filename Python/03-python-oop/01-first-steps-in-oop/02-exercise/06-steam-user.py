class SteamUser:
    def __init__(self, username: str, games: list) -> None:
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        return f"{game} is not in library"

    def buy_game(self, game_name):
        if game_name not in self.games:
            self.games.append(game_name)
            return f"{self.username} bought {game_name}"
        return f"{game_name} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
