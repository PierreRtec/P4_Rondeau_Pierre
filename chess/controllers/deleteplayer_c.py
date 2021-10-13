from chess.views.deleteplayer import DeletePlayer
from chess.models.players import Player


"""
Test
"""

class DeletePlayerC:

    def __init__(self, data):
        self.data = data

    def call(self):

        deleteplayer_view = DeletePlayer(self.data)
        choice,del_method = deleteplayer_view.home()
        # suppression user choice
        Player.delete_player(choice,del_method)
        return "manageplayer"