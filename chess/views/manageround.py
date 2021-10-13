"""Object view"""


class ManageRound:

    def __init__(self, oround):
        self.oround = oround

    def make_round(self):

        winners = []
        for match in self.oround.roundd:
            print("Match entre deux personnes\n 1:{}/2:{}/3:Égalité=".format(*match))
            winner = input("Qui gagne ?")
            winners.append((match, winner))
        return winners

    def m_elo(self, players):
        
        dict_elo = {}
        
        for player in players:
            print("nom : {}, score : {}, elo : {}".format(player.name,player.score, player.elo))

        for player in players:
            print("nom : {}".format(player.name))
            new_elo = input("nouveau elo :")