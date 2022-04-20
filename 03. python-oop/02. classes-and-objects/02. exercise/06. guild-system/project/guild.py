from project.player import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players = []
    
    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
    
    def kick_player(self, player_name: str):
        player: Player
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."
        
                 
                
    def guild_info(self):
        info = f"Guild: {self.name}\n"
        info += '\n'.join([player.player_info() for player in self.players])
        return info
