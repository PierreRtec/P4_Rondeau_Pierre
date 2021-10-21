from chess.models.players import Player



class Round:
    
    def __init__(self, tournament):

        self.players = tournament.players
        self.rmatchs = []
        self.players.sort(key = lambda player: player.elo)
        for player in self.players:
            player.score = 0
     
    def __str__(self):

        all_match = self.rmatchs
        name_str = "liste des matchs : \n"
        for player_one, player_two, result in all_match:
            name_str += "{} vs {}\n".format(player_one, player_two)
            if result == 1:
                name_str += "{} gagne \n".format(player_one)
            elif result == 2:
                name_str += "{} gagne \n".format(player_two)
            else:
                name_str += " égalité \n"
        return name_str

    def gen_firstmatch(self):
        
        nb_joueur = len(self.players)
        players_list_1 = self.players[:nb_joueur // 2]
        players_list_2 = self.players[nb_joueur // 2:]
        self.roundd = zip(players_list_1, players_list_2)

    # def gen_nm(self):

        # players_g = self.players.sort(key = lambda player: player.score)
        # nb_joueur = len(self.players)
        # players_list_1 = players_g[:nb_joueur // 2]
        # players_list_2 = players_g[nb_joueur // 2:]
        # self.roundd = zip(players_list_1, players_list_2)
        # premier contre deuxième si pas jouer ensemble match précédent, ainsi de suite.
        # MVC puis fini. !!!!!

    def set_scores(self, winners):

        for match,winner in winners:
            if winner == "1":
                match[0].score += 1
            elif winner == "2":
                match[1].score += 1
            else:
                match[0].score =+ 0.5
                match[1].score =+ 0.5
            self.rmatchs.append((match[0].name,match[1].name,winner))

    
    def serialize_round(self):

        return self.rmatchs