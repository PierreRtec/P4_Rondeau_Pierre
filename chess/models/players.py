from tinydb import TinyDB
from datetime import datetime


def valid_dob(test):
    try:
        datetime.strptime(test, "%d/%m/%Y")
    except Exception:
        return False
    return True


class Player:
    """
    Cette classe va s'occuper de gérer tous les joueurs.
    Si ils participent ou non à un tournoi.
    """

    __db = TinyDB("players.json", sort_keys=True, indent=4, separators=(",", ": "))
    __db = __db.table("players")
    # une seule liste pour tous les players
    players = []

    def __init__(self, **kwargs):
        for property, prop_control in self.my_properties():
            setattr(self, property, kwargs.get(property, ""))

    def __str__(self):
        return self.name

    @classmethod
    def my_properties(self):
        # gestion des propriétés d'un joueur
        return (
            ("name", None),
            ("first_name", None),
            ("birthday", valid_dob),
            ("sex", None),
            ("elo", None),
        )

    @classmethod
    def listplayers(self, needsort=False):
        if needsort:
            new_list = [player for player in self.players]
            new_list.sort(key=lambda player: player.elo)
            return new_list
        return self.players

    @classmethod
    def add_player(self, player):
        exist = False
        for player_check in Player.listplayers():
            if player_check.name == player.name:
                exist = True
                break
        if not exist:
            self.players.append(player)
            self.save_all_players()
            return 0
        return 1

    @classmethod
    def delete_player(self, choice, del_method):
        if del_method == "b":
            del self.players[int(choice)]
        else:
            for index, player in enumerate(Player.listplayers()):
                if player.name == choice:
                    del self.players[index]
                    break
        self.save_all_players()

    @classmethod
    def cp_convert(self, choice, select_method):
        if select_method == "b":
            return self.players[int(choice)]
        else:
            for index, player in enumerate(Player.listplayers()):
                if player.name == choice:
                    return self.players[index]

    @classmethod
    def save_all_players(self):
        players_db = self.__db
        players_db.truncate()
        serialized_players = []
        for player in self.players:
            serialized_players.append(player.serialize_player())
        players_db.insert_multiple(serialized_players)

    def serialize_player(self):
        data = {}
        for property, prop_control in self.my_properties():
            data[property] = getattr(self, property)
        return data

    @classmethod
    def load_player(self):
        serialized_players_list = self.__db.all()
        self.players = [Player(**data) for data in serialized_players_list]

    @classmethod
    def pickle(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
