from chess.views.manageplayer import ManagePlayer


class ManagePlayerC:
    """
    Cette classe permet le controle la liste des tournois.
    """

    def __init__(self, data):
        self.data = data

    def call(self):
        manageplayer_view = ManagePlayer()
        choice = manageplayer_view.home()
        if choice == "1":
            return "createplayer"
        elif choice == "2":
            return "listplayers"
        elif choice == "3":
            return "deleteplayer"
        return "homepage"
