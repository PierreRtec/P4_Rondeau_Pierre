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