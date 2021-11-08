from chess.models.tournaments import Tournament


class DeleteTournament:
    """
    Cette classe permet l'affichage de l'écran de suppression d'un tournoi.
    """

    def __init__(self, data):
        self.data = data

    def home(self):
        print("Bienvenue dans la page de suppression de tournois")
        print("1. Selectionnez un tournoi à supprimer")
        for index, tournament in enumerate(Tournament().listtournaments()):
            print(index, tournament)
        return input("ID du tournoi à supprimer :")
