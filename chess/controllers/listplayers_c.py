"""Cette classe permet le controle la liste des joueurs"""

from chess.views.listplayers import ListPlayers

class ListPlayersC:

    def __init__(self, data):
        self.data = data

    def call(self):
        listplayers_view = ListPlayers(self.data)
        choice = listplayers_view.home()
        return "manageplayer"