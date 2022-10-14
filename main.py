"""
HENRY HARRISON
23 SEPTEMBRE 2022
CODE: DEVINETTE DE CHIFFRE
TP2
"""

#importer la fonction random utiliser dans le code
import random

print("bienvenue dans mon jeu de devinette")
boucle_jeu = True
while boucle_jeu:

#defenir le nombrre dessai
    nb_essai = 0

#definir les borne du nombre a deviner
    nombre_minimum = int(input("Choisissez la borne minimale du jeu: "))
    nombre_maximum = int(input("Choisissez la borne maximale du jeu: "))
    nombre = random.randint(nombre_minimum, nombre_maximum)
    print("J'ai choisi un nombre entre",nombre_minimum,"et", nombre_maximum)
    print("a vous de le deviner!")

#boucle des essai
    boucle_essai = True
    while boucle_essai:
        nb_essai = nb_essai + 1

        print("essai numero", nb_essai)

        chiffre_joueur = int(input("Entrez votre numero choisi:  "))

#quand le chiffre deviner est plus petit que le nombre
        if chiffre_joueur < nombre:
            print("                         ")
            print("ton nombre est trop petit")

#quand le chiffre deviner est plus grand que le nombre
        if chiffre_joueur > nombre:
            print("                         ")
            print("ton nombre est trop grand")

#quand il a la bonne reponse
        if chiffre_joueur == nombre:
            print("                ")
            print("bonne reponse!!!")
            print("vous meriter toute mes felicitation!!!")
            replay = input("voulez vous rejouer, oui ou non?  ")
            if replay == "non":
                boucle_jeu = False
                boucle_essai = False
            if replay == "oui":
                boucle_essai = False




