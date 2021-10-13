from chess.views.manageround import ManageRound
from chess.models.round import Round

class ManageRoundC:

    def __init__(self, tournament):
        self.tournament = tournament

    def call(self):
    
        oround = Round(self.tournament.players)
        round_view = ManageRound(oround)
        oround.gen_match()
        winners = round_view.make_round()
        oround.set_scores(winners)
   
        oround.rounds.append(rmatchs)

        while len(self.rounds) < 4:
            self.players.sort(key = lambda player: player.score) # regarder tri par elo en cas d'égalité sur le score
            nb_joueur = len(self.players)
            oround.gen_match()
            # rmatchs = [] check si on le fait dans le modele
            winners = round_view.make_round()
            oround.set_scores(winners)
            # oround.rounds.append(rmatchs)
        elo = round_view.m_elo(self.tournament.players)

        for player in self.tournament.players:
            player.elo = int(elo[player.name])
        Player.save_all_players()
        Tournament.save_all_tournaments()