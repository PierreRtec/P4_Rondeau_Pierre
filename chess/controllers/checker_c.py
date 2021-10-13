from chess.views.manageround import ManageRound
from chess.models.round import Round
from chess.views.managetournaments import ManageTournament
from chess.views.listtournaments import ListTournaments
from chess.views.listplayers import ListPlayers
from chess.views.checker import Checker


class CheckerC:

    def __init__(self,data):
        self.data = data
    
    def call(self):

        checker_view = Checker()
        return "checker"
