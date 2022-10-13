"""
HENRY HARRISON
23 SEPTEMBRE 2022
CODE: DEVINETTE DE CHIFFRE

"""
import random
boucle_jeu = True
while boucle_jeu:
    nombre = random.randint(0, 100)

    nb_essai = 0

    print("J'ai choisi un nombre entre 0 et 100.")
    print("a vous de le deviner!")

    boucle_essai = True
    while boucle_essai:
        nb_essai = nb_essai + 1
        if nb_essai == 100:
            boucle_essai = False
            print("le nombre etait",nombre,"tu est pas tres bon si ton nombre d'essai etait 100")
        print("essai numero", nb_essai)

        chiffre_joueur = int(input("Entrez votre numero choisi:  "))

        if chiffre_joueur < nombre:
            print("ton nombre est trop petit",nombre)


        if chiffre_joueur > nombre:
            print("ton nombre est trop grand")


        if chiffre_joueur == nombre:
            print("bonne reponse")
            print()
            replay = input("voulez vous rejouer? oui ou non?  ")
            if replay == "non":
                boucle_jeu = False
                boucle_essai = False



