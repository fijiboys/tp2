"""
HENRY HARRISON
23 SEPTEMBRE 2022
CODE: DEVINETTE DE CHIFFRE

"""
import random

nombre = random.randint(0, 100)

nb_essai = 0

print("J'ai choisi un nombre entre 0 et 100.")
print("a vous de le deviner!")

chiffre_joueur = int(input("Entrez votre essai:  "))

nb_essai = nb_essai + 1

if chiffre_joueur < nombre:
    print(nombre > chiffre_joueur)


