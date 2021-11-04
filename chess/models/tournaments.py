from tinydb import Query, TinyDB
from chess.models.players import Player
from datetime import datetime


def valid(testt):
    try:
        date = datetime.strptime(testt, "%d/%m/%Y")
    except:
        return False
    return True


def type_time_control(ttc):
    return ttc in ["blitz", "bullet", "rapid"]


class Tournament:
    """
    Cette classe va s'occuper de gérer tous les tournois.
    """

    __db = TinyDB("tournaments.json", sort_keys=True, indent=4, separators=(",", ": "))
    __db = __db.table("tournaments")
    # une seule liste pour tous les tournois
    tournaments = []

    def __init__(self, **kwargs):
        for property, prop_control in self.prop_tournaments():
            setattr(self, property, kwargs.get(property, ""))
        self.players = kwargs.get("players", [])
        self.rounds = kwargs.get("rounds", [])
        self.scores = kwargs.get("scores", {})

    @classmethod
    def prop_tournaments(self):
        # gestion des propriétés d'un tournoi
        return (
            ("nom", None),
            ("lieu", None),
            ("date", valid),
            ("type de contrôle de temps", type_time_control),
            ("description", None),
        )

    def __str__(self):
        name_str = "nom du tournoi : {}\n".format(self.nom)
        name_str += "liste des joueurs du tournoi :\n"
        for player in self.players:
            name_str += str(player)
        return name_str

    @classmethod
    def listtournaments(self):
        return self.tournaments

    @classmethod
    def add_tournament(self, tournament):
        exist = False
        for tournament_check in Tournament.listtournaments():
            if tournament_check.nom == tournament.nom:
                exist = True
                break
        if not exist:
            self.tournaments.append(tournament)
            self.save_all_tournaments()
            return 0
        return 1

    @classmethod
    def delete_tournament(self, choice):
        del self.tournaments[int(choice)]
        self.save_all_tournaments()

    @classmethod
    def save_all_tournaments(self):
        tournaments_db = self.__db
        tournaments_db.truncate()
        serialized_tournaments = []
        for tournament in self.tournaments:
            serialized_tournaments.append(tournament.serialize_tournament())
        tournaments_db.insert_multiple(serialized_tournaments)

    def serialize_tournament(self):
        data = {}
        for property, prop_control in self.prop_tournaments():
            data[property] = getattr(self, property)
        data["players"] = []
        for player in self.players:
            data["players"].append(player.name)
        data["rounds"] = self.rounds
        data["scores"] = self.scores
        return data

    @classmethod
    def load_tournament(self):
        serialized_tournaments_list = self.__db.all()
        self.tournaments = []
        for tournament in serialized_tournaments_list:
            players = []
            for player_name in tournament["players"]:
                players.append(Player.pickle(player_name))
            tournament["players"] = players
            self.tournaments.append(Tournament(**tournament))
