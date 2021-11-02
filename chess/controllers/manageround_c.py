from chess.views.manageround import ManageRound
from chess.models.round import Round
from chess.views.listtournaments import ListTournaments
from chess.models.tournaments import Tournament
from chess.models.players import Player

class ManageRoundC:

    def __init__(self, data):

        self.data = data

    def call(self):
        
        tournament_list = ListTournaments(self.data)
        choice = tournament_list.select_tournament()
        self.tournament = Tournament.listtournaments()[int(choice)]
        oround = Round(self.tournament)
        round_view = ManageRound(oround)
        round_view.display()
        if len(self.tournament.rounds) < 4:
            choice = ""
            while choice not in ("o","n"):
                choice = input("Lancer un nouveau tour ?")

            if choice == "o":
                if len(self.tournament.rounds) == 0:
                    oround.gen_firstmatch() #gen_firstmatch ou gen_match (à faire en plus)
                    winners = round_view.make_round()
                    oround.set_scores(winners,self.tournament)
                else:
                    nb_joueur = len(self.tournament.players)
                    oround.gen_nm()
                    winners = round_view.make_round()
                    oround.set_scores(winners,self.tournament)
                print(oround.serialize_round())
                self.tournament.rounds.append(oround.serialize_round())
                Tournament.save_all_tournaments()
        if len(self.tournament.rounds) == 4:
            elo = round_view.m_elo(self.tournament.players,self.tournament) 
            for player in self.tournament.players:
                player.elo = int(elo[player.name])
            Player.save_all_players()
            
        return "managetournament"

        # test