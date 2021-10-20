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
        if len(oround.rmatchs) < 4:
            choice = ""
            while choice not in ("o","n"):
                choice = input("Lancer un nouveau tour ?")

            if choice == "o":
                if len(oround.rmatchs) == 0:
                    oround.gen_match()
                    winners = round_view.make_round()
                    oround.set_scores(winners)
                else:
                    self.tournament.players.sort(key = lambda player: player.score) # regarder tri par elo en cas d'égalité sur le score
                    nb_joueur = len(self.tournament.players)
                    oround.gen_match()
                    # rmatchs = [] check si on le fait dans le modele
                    winners = round_view.make_round()
                    oround.set_scores(winners)
                Player.save_all_players()
                self.tournament.rounds = oround.serialize_round()
                Tournament.save_all_tournaments()
        if len(oround.rmatchs) == 4:
            
            # oround.rounds.append(rmatchs)
            elo = round_view.m_elo(self.tournament.players) # parti du if
            for player in self.tournament.players:
                player.elo = int(elo[player.name])
            Player.save_all_players()
            
        return "managetournament"