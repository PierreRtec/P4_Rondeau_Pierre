from chess.views.listtournaments import ListTournaments


class ListTournamentsC:
    """
    Cette classe permet le controle la liste des tournois.
    """

    def __init__(self, data):
        self.data = data

    def call(self):
        listtournaments_view = ListTournaments(self.data)
        choice = listtournaments_view.home()
        return "managetournament"
