from chess.models.players import Player



class Round:
    
    def __init__(self, tournament):

        self.tournament = tournament
        self.players = tournament.players
        self.rmatchs = []
        self.players.sort(key = lambda player: player.elo)

    def __str__(self):

        all_match = self.tournament.rounds.copy()
        name_str = "liste des matchs : \n"
        for round in all_match:
            for player_one, player_two, result in round:
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

    def gen_nm(self):

        self.players.sort(key = lambda player: self.tournament.scores[player.name])
        nb_joueur = len(self.players)
        players_list_1 = self.players[:nb_joueur // 2]
        players_list_2 = self.players[nb_joueur // 2:]
        self.roundd = zip(players_list_1, players_list_2)
        # premier contre deuxième si pas jouer ensemble match précédent, ainsi de suite. avec un if (avoir un le score avant)
        # MVC puis fini. !!!!!

    def set_scores(self, winners, tournament):

        for match,winner in winners:
            if winner == "1":
                tournament.scores[match[0].name]+=1
            elif winner == "2":
                tournament.scores[match[1].name]+=1
            else:
                tournament.scores[match[1].name]+=0.5
                tournament.scores[match[1].name]+=0.5
            self.rmatchs.append((match[0].name,match[1].name,winner))

    def serialize_round(self):

        return self.rmatchs