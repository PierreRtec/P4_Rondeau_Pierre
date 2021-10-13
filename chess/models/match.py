class Match:
    
    """
    Cette classe s'occupe du lancement des matchs.
    """

    # Chaque matchs = une paire de joueurs + résultats pour chacuns des joueurs 


    def __init__(self, first_player, second_player):
        self.players = [first_player, second_player]
        self.scores = [None, None]


# Stockage données des matchs sous deux listes 
# Liste 1 et 2 contiennent = référence instance joueur + un score 
# match multiples stockés sur liste instance du tour