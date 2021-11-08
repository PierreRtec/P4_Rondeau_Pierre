"""Object view"""


class ManageRound:
    """
    Cette classe permet l'affichage de l'écran de gestion des tours.
    """
    def __init__(self, oround):
        self.oround = oround

    def make_round(self):

        winners = []
        for match in self.oround.roundd:
            print("Match entre deux personnes\n 1:{}/2:{}/3:Égalité=".format(*match))
            winner = input("Qui gagne ?")
            winners.append((match, winner))
        return winners

    def m_elo(self, players, tournament):

        dict_elo = {}

        for player in players:
            print(
                "nom : {}, score : {}, elo : {}".format(
                    player.name, tournament.scores[player.name], player.elo
                )
            )

        for player in players:
            print("nom : {}".format(player.name))
            new_elo = input("nouveau elo :")
            dict_elo[player.name] = int(new_elo)
        return dict_elo

    def display(self):

        if len(self.oround.rmatchs) == 4:
            print("Tournoi terminé")
        print(self.oround)
