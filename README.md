# Projet de gestion de tournois d'échec avec algorithme Suisse
---
# Prérequis

- Python 3
- Environnement virtuel
- pipfile

## Comment installer l'environnement virtuel ?
Dans votre terminal :

* pip install pipenv
* pipenv shell
* pipenv install

### Pour plus de précisions : https://pypi.org/project/pipenv/
---

## Comment lancer le programme "chess" ?
Dans votre terminal :

* py -m chess
* _tappez le chiffre que vous voulez pour vous déplacer dans les menus_.
---

## Affichages & Menus d'utilisation de l'application

### I - Bienvenue dans la page d'accueil
1. Manage Player
2. Manage Tournament
3. Exit<br>
Quel est votre choix ?<br/>


### Quel est votre choix ?*1*
Menu de gestion des joueurs
1. Create Player
2. Liste des joueurs
3. Delete Player
Retour / Accueil<br>
Quel est votre choix ?<br/>


### II - Quel est votre choix ?*2*
Menu de gestion des tournois
1. Création de tournoi
2. Liste des tournois
3. Tournois en cours
4. Supprimer un tournoi<br>
Retour / Accueil<br/>
Quel est votre choix ?

##### Pour un aperçu des affichages avant le code, télécharger ce diapo : [Chess Program OC P4  Maquette 2.0](https://docs.google.com/presentation/d/1a-6vUmawzazSRycqUz_SB1P1LcgC3qgEoveW_9HPyxg/edit?usp=sharing)

### Pour la génération de rapports flake8, entrez dans le terminal :

+ pipenv install flake8
+ pipenv install flake8-html

créer un fichier qui s'appelle "setup.cfg"

mettre dedans : 

[flake8]
exclude =
	.git,
	env,
	__pycache__,
	ajout_liste_joueur.py,
	models/__pycache
	test.py

max-line-length = 119

#### COMMANDE création de rapport HTML >_

flake8 --format=html --htmldir=flake8-rapport

#### Pour plus de précisision sur la pep8, assurez-vous d'avoir le module "black" et entrez ceci dans votre terminal :

black chess

Cela exécutera le module sur notre application. Si l'application s'appelait chessprogr alors ce serait "black chessprogr".
