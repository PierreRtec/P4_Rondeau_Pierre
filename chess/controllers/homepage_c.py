from chess.views.homepage import Homepage
from chess.models.players import Player

class HomepageC:
    """
    Cette classe permet le controle la page d'accueil.
    """

    def __init__(self, data):
        self.data = data

    def call(self):
        homepage_view = Homepage()
        choice = homepage_view.home()
        if choice == "1":
            return "manageplayer"
        elif choice == "2":
            return "managetournament"
        elif choice == "3":
            return "exit"