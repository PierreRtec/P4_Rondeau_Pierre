"""Cette classe permet le controle de la creation de joueurs"""

from chess.views.createplayer import CreatePlayer
from chess.models.players import Player

class CreatePlayerC:

    def __init__(self, data):
        self.data = data

    def add_player(self, player):
        return Player.add_player(player)
        
    def call(self):
        code_return = 2
        createplayer_view = CreatePlayer()
        while code_return in (1,2):
            player = createplayer_view.home(code_return)
            player_obj = Player(**player)
            code_return = self.add_player(player_obj)
        createplayer_view.home(code_return)
        return "manageplayer"

        # test