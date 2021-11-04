"""Object view"""

from chess.models.tournaments import Tournament


class ListTournaments:
    def __init__(self, data):
        self.data = data

    def home(self):
        print("Liste des tournois :")
        for tournament in Tournament.listtournaments():
            print(tournament)
        return "managetournament"

    def select_tournament(self):
        print("Choisir le numéro du tournoi : ")
        for index, tournament in enumerate(Tournament.listtournaments()):
            print(index, tournament)
        position_tourn = input("Position du tournoi :")
        return position_tourn
