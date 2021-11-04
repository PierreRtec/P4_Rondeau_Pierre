from chess.models.players import Player
from chess.models.tournaments import Tournament

# from chess.controllers import *
from chess.controllers.listplayers_c import ListPlayersC
from chess.controllers.createplayer_c import CreatePlayerC
from chess.controllers.deleteplayer_c import DeletePlayerC
from chess.controllers.homepage_c import HomepageC
from chess.controllers.manageplayer_c import ManagePlayerC
from chess.controllers.createtournament_c import CreateTournamentC
from chess.controllers.managetournaments_c import ManageTournamentC
from chess.controllers.listtournaments_c import ListTournamentsC
from chess.controllers.deletetournament_c import DeleteTournamentC
from chess.controllers.manageround_c import ManageRoundC


menu_principal = {
    "homepage": HomepageC,
    "manageplayer": ManagePlayerC,
    "managetournament": ManageTournamentC,
    "createplayer": CreatePlayerC,
    "listplayers": ListPlayersC,
    "deleteplayer": DeletePlayerC,
    "createtournament": CreateTournamentC,
    "listtournaments": ListTournamentsC,
    "deletetournament": DeleteTournamentC,
    "tourn_cours": ManageRoundC,
}


class ChessProgram:
    def __init__(self):
        self.data = {}
        Player.load_player()
        Tournament.load_tournament()

    # c'est ce qu'il faut save (regarder si obj pas déjà présent) self.data du load fichier sérialisé

    def main(self):

        activ_view = "homepage"
        while activ_view != "exit":
            # quand exit proposer de sauvegarder
            # try bloc logique
            # try:
            activ_controller = menu_principal.get(activ_view)
            activ_view = activ_controller(self.data).call()


# sauvegarder le self.data serialiser

# except Exception as my_exception:
# print(my_exception)
# activ_view = "homepage"


if __name__ == "__main__":
    chess_program = ChessProgram()
    chess_program.main()
