# In objects.py
class Lineup:
    def __init__(self):
        self.players = {}

    def add_player(self, player):
        self.players[player.full_name] = player

    def remove_player(self, name):
        if name in self.players:
            del self.players[name]

    def get_player(self, name):
        return self.players.get(name, None)

    def move_player(self, old_name, new_name):
        self.players[new_name] = self.players.pop(old_name, None)

    def __iter__(self):
        return iter(self.players.values())

    def __len__(self):
        return len(self.players)


class Player:
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def batting_average(self):
        if self.at_bats > 0:
            return round(self.hits / self.at_bats, 3)
        return 0.0