from chess.views.deleteplayer import DeletePlayer
from chess.views.homepage import Homepage
from chess.views.manageplayer import ManagePlayer
from chess.views.managetournaments import ManageTournament
from chess.models.players import Player
from chess.models.tournaments import Tournament
from chess.views.createtournament import CreateTournament
from chess.views.listtournaments import ListTournaments
from chess.views.deletetournaments import DeleteTournament
from chess.controllers import *


menu_principal = {
    "homepage": HomepageC,
    "manageplayer": ManagePlayerC, 
    "managetournament" : ManageTournamentC,
    "createplayer" : CreatePlayerC,
    "listplayers" : ListPlayersC, 
    "deleteplayer" : DeletePlayerC,
    "createtournament" : CreateTournamentC,
    "listtournaments" : ListTournamentsC,
    "deletetournament" : DeleteTournamentC,
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
            #try:
            activ_controller = menu_principal.get(activ_view)
            activ_view = activ_controller(self.data).call()
# sauvegarder le self.data serialiser

            #except Exception as my_exception:
            #print(my_exception)
            #activ_view = "homepage"
                

if __name__ == "__main__":
    chess_program = ChessProgram()
    chess_program.main()