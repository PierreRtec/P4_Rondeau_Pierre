
"""Suit les tournois et les matchs"""




from chess.models.tournaments import Tournament


class Checker:
    
    def __init__(self, data):
        self.data = data

    def home(self):
        
        print("Liste des tournois en cours :")
        for tournament in Tournament.listtournaments():
            if len(tournament.rounds) < 4:
                    print(tournament)