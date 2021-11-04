from chess.views.manageround import ManageRound
from chess.models.round import Round
from chess.views.listtournaments import ListTournaments
from chess.models.tournaments import Tournament
from chess.models.players import Player


class ManageRoundC:
    """
    Cette classe permet la gestion des rounds et des matchs entre le joueurs.
    """

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
            # boucle choix du tour jusqu'à 4 tours
            while choice not in ("o", "n"):
                choice = input("Lancer un nouveau tour ?")
            if choice == "o":
                if len(self.tournament.rounds) == 0:
                    oround.gen_firstmatch()  # gen_firstmatch ou gen_match (à faire en plus)
                    winners = round_view.make_round()
                    oround.set_scores(winners, self.tournament)
                else:
                    nb_joueur = len(self.tournament.players)
                    oround.gen_nm()
                    winners = round_view.make_round()
                    oround.set_scores(winners, self.tournament)
                self.tournament.rounds.append(oround.serialize_round())
                Tournament.save_all_tournaments()
        # si les 4 tours sont joués, alors on attribue un elo
        # le classement peut être mesuré par palier de niveau du joeur : 1000, 1600, 2000, 2400, 2500, 2800
        # débutant, joueur de club, expert, maître international, grand-maître international, champion du monde d'échecs
        # l'utilisateur de l'application décide du elo de chaque joueurs à la fin d'un tournoi et peut revenir à tout moment dessus
        if len(self.tournament.rounds) == 4:
            elo = round_view.m_elo(self.tournament.players, self.tournament)
            for player in self.tournament.players:
                player.elo = int(elo[player.name])
            Player.save_all_players()
        return "managetournament"
