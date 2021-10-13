"""Cette classe permet le controle de la creation de tournois"""

from chess.views.createtournament import CreateTournament
from chess.models.tournaments import Tournament
from chess.models.players import Player
from chess.controllers.manageround_c import ManageRoundC


class CreateTournamentC:

    def __init__(self, data):
        self.data = data

    def add_tournament(self, tournament):
        Tournament.add_tournament(tournament)

    def call(self):
        code_return = 2
        createtournament_view = CreateTournament(self.data)
        while code_return in (1,2):
            tournament = createtournament_view.home(code_return)
            players = []
            for choice,select_method in tournament["listplayers"]:
                player = Player.cp_convert(choice, select_method)
                players.append(player)
            del tournament["listplayers"]
            tournament["players"]=players
            tournament_obj = Tournament(**tournament)
            code_return = self.add_tournament(tournament_obj)
        createtournament_view.home(code_return)
        # manageround_c = ManageRoundC(tournament_obj)            
        return "managetournament"