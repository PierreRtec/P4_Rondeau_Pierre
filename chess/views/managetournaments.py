"""Object view"""

class ManageTournament:

    def home(self):

        print("Menu de gestion des tournois")
        print("1. Création de tournoi")
        print("2. Liste des tournois")
        print("3. Supprimer un tournoi")
        print("Retour / Accueil")
        return input("Quel est votre choix ?")