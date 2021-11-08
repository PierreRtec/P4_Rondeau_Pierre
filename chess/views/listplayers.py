from chess.models.players import Player


class ListPlayers:
    """
    Cette classe permet l'affichage de l'écran de liste des joueurs.
    """

    def __init__(self, data):
        self.data = data

    def home(self):
        print("Liste des joueurs :")
        for player in Player.listplayers():
            print(player)
        return "manageplayer"

    def select_player(self):
        select_method = input(
            "Indiquez la méthode de selection : a) Par nom | b) Par position"
        )
        if select_method == "b":
            print("1. Selectionnez un joueur")
            for index, player in enumerate(Player.listplayers()):
                print(index, player)
            position = input("Position du joueur à sélectionner :")
            return position, select_method
        else:
            print("1. Selectionnez un joueur")
            for player in Player.listplayers():
                print(player)
            nom_du_joueur = input("Nom du joueur")
            return nom_du_joueur, select_method
