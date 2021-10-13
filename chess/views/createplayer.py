"""
Object view
"""

from chess.models.players import Player

class CreatePlayer:

    """
     Cette méthode permet de y
    """

    def player_properties(self):
        player = {}
        for player_prop in Player.my_properties():
            value = input('Entrez les informations suivantes: {}\n'.format(player_prop))
            player[player_prop] = value
        return player

    def home(self, code_return):
        player = {}
        if code_return in (1,2):
            if code_return == 2:
                print("Bienvenue dans la page de création de joueurs")    
            else:
                print("Un joueur du même nom existe déjà, entrez un autre nom")
            player = self.player_properties()
        else:
            print("Joueur bien ajouté")
        return player