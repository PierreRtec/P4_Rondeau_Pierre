from tinydb import Query, TinyDB
from chess.models.players import Player


class Tournament:
    """
    Cette classe va s'occuper de gérer tous les tournois.
    """
    __db = TinyDB('tournaments.json', sort_keys=True, indent=4, separators=(',', ': '))
    __db = __db.table('tournaments')

    # une seule liste pour tous les tournois
    tournaments = []

    def __init__(self, **kwargs):
        for property in self.prop_tournaments():
            setattr(self, property, kwargs.get(property, ""))
        self.players = kwargs.get("players",[])
        self.rounds = kwargs.get("rounds",[])


    @classmethod
    def prop_tournaments(self):
        return ('nom', 'lieu', 'date', 'type de contrôle de temps', 'description')
    # contrôle de temps soit blitz / bullet / rapid 
    # temp del 'joueurs', 

    def __str__(self):
        name_str = "nom du tournoi : {}\n".format(self.nom)
        name_str+= "liste des joueurs du tournoi :\n"
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
        for property in self.prop_tournaments():
            data[property] = getattr(self, property)
        data["players"] = []
        for player in self.players:
            data["players"].append(player.name)
        data["rounds"] = self.rounds
        return data

    @classmethod
    def load_tournament(self):
        serialized_tournaments_list = self.__db.all()
        self.tournaments = []
        for tournament in serialized_tournaments_list:
            players = []
            for player_name in tournament["players"]:
                players.append(Player.pickle(player_name))
            tournament["players"]=players
            self.tournaments.append(Tournament(**tournament))