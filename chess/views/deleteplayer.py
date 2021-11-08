# from chess.models.players import Player
from chess.views.listplayers import ListPlayers


class DeletePlayer:
    """
    Cette classe permet l'affichage de l'écran de suppression d'un joueur.
    """

    def __init__(self, data):
        self.data = data

    def home(self):
        print("Bienvenue dans la page de suppression de joueur")
        listplayers_view = ListPlayers(self.data)
        choice = listplayers_view.select_player()
        return choice
