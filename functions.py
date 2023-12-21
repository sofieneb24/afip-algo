
import os
import random

# Charge les données à partir d'un fichier.

def load_data(fileName):
    print(open(fileName).read())

# Supprime la première ligne (en-tête) du fichier txt.
        
def supprimer_entete(fileName):
    with open(fileName) as file:
        lines = file.readlines()[1:]
        for line in lines:
            print(line.rstrip())

# Afficher uniquement les trois premières lettres.
            
def trois_lettres(fileName):
    with open(fileName) as file:
        for line in file.readlines()[1:]:
            team_name = line.split(',')[1][:3]
            print(team_name)

# Enregistrer les données dans un fichier.
            
            

# Melanger les lignes.
            
def melange_lignes(fileName):
    with open(fileName, 'r') as file:
        lignes = file.readlines()
        random.shuffle(lignes)
        print(''.join(lignes))
