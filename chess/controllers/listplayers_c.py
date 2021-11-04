from chess.views.listplayers import ListPlayers


class ListPlayersC:
    """
    Cette classe permet le controle la liste des joueurs.
    """

    def __init__(self, data):
        self.data = data

    def call(self):
        listplayers_view = ListPlayers(self.data)
        choice = listplayers_view.home()
        if choice == listplayers_view.home():
            return "manageplayer"
