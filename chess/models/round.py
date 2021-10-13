from chess.models.players import Player



class Round:
    
    def __init__(self, players):

        self.players = players
        self.rounds = []
        self.players.sort(key = lambda player: player.elo)
        for player in self.players:
            player.score = 0
        # MAJ
        self.rmatchs = []

    def __str__(self):

        all_match = self.oround.rmatchs
        name_str = "liste des matchs : \n"
        for player_one, player_two, result in all_match:
            name_str += "{} vs {}".format(player_one, player_two)
            if result == 1:
                name_str += "{} gagne".format(player_one)
            elif result == 2:
                name_str += "{} gagne".format(player_two)
            else:
                name_str += "égalité"
        return name_str

    def gen_match(self):
        
        nb_joueur = len(self.players)
        players_list_1 = self.players[:nb_joueur // 2]
        players_list_2 = self.players[nb_joueur // 2:]
        self.roundd = zip(players_list_1, players_list_2)

    def set_scores(self, winners):

        for match,winner in winners:
            if winner == "1":
                match[0].score += 1
            elif winner == "2":
                match[1].score += 1
            else:
                match[0].score =+ 0.5
                match[1].score =+ 0.5
            self.rmatch.append((match[0].name,match[1].name,winner))