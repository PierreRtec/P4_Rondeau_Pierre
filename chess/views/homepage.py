
"""Object view"""


class Homepage:

    def home(self):
        # bienvenue n'est pas un choix
        print("Bienvenue dans la page d'accueil")
        print("1. Manage Player")
        print("2. Manage Tournament")
        print("3. Exit")
        return input("Quel est votre choix ?")