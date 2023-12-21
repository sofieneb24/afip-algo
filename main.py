from functions import *

# Nom de fichier à charger
fileName = "FIFA_World_Cup/FIFA-2022.txt"

# Charge un fichier en lecture
file = open(fileName, "r")

# Charge les données à partir d'un fichier
data = load_data(fileName);

# Supprimer l'en-tête
supprimer_entete(fileName)

# Obtenir les trois premières lettres
trois_lettres(fileName)

# Mélanger les lignes
melange_lignes(fileName)

# Enregistrer les données dans un fichier.
