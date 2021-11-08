from chess.views.listplayers import ListPlayers
from chess.models.tournaments import Tournament


class CreateTournament:
    """
    Cette classe permet l'affichage de l'écran de la création d'un tounoi.
    """

    def __init__(self, data):
        self.data = data

    def tournament_properties(self):
        tournament = {}
        for tourn_prop, tournament_chr in Tournament.prop_tournaments():
            value = input(
                "Entrez les informations suivantes : {}\n".format(tourn_prop)
            )
            if tournament_chr:
                while not tournament_chr(value):
                    value = input(
                        "Saisie incorrecte"
                        "\n Entrez les informations suivantes: {}\n".format(
                            tourn_prop
                        )
                    )
            tournament[tourn_prop] = value
        listplayers = []
        while len(listplayers) != 8:
            print("Liste des joueurs parmi ceux proposés :")
            listplayers_view = ListPlayers(self.data)
            choice = listplayers_view.select_player()
            listplayers.append(choice)
        tournament["listplayers"] = listplayers
        return tournament

    def home(self, code_return):
        tournament = {}
        if code_return in (1, 2):
            if code_return == 2:
                print("Bienvenue dans la page de création de tournois")
            else:
                print(
                    "Un tournois du même nom existe déjà"
                    "\n Entrez un autre nom"
                    )
            tournament = self.tournament_properties()
        else:
            print("Tournois bien ajouté")
        return tournament
