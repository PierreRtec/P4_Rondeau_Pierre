"""Cette classe permet le controle la page de gestion des tournois"""

from chess.views.managetournaments import ManageTournament

class ManageTournamentC:

    def __init__(self, data):
        self.data = data

    def call(self):

        managetournaments_view = ManageTournament()
        choice = managetournaments_view.home()
        if choice == "1":
            return "createtournament"
        elif choice == "2":
            return "listtournaments"
        elif choice == "3":
            return "checker"
        elif choice == "4":
            return "deletetournament"
        return "homepage"