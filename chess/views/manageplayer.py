"""Object view"""


class ManagePlayer:
    """
    Cette classe permet l'affichage de l'écran de gestion des joueurs.
    """

    def home(self):
        print("Menu de gestion des joueurs")
        print("1. Create Player")
        print("2. Liste des joueurs")
        print("3. Delete Player")
        print("Retour / Accueil")
        return input("Quel est votre choix ?")
