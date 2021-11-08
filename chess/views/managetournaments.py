"""Object view"""


class ManageTournament:
    """
    Cette classe permet l'affichage de l'écran de gestion des tournois.
    """
    def home(self):
        print("Menu de gestion des tournois")
        print("1. Création de tournoi")
        print("2. Liste des tournois")
        print("3. Tournois en cours")
        print("4. Supprimer un tournoi")
        print("Retour / Accueil")
        return input("Quel est votre choix ?")
