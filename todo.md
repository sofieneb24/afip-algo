## Analyse des Données de la Coupe du Monde de la FIFA

### Contraintes de la Mission

- Toutes les fonctions et structures de données doivent être créées à partir de zéro, en utilisant uniquement les types de données et structures de base du langage, sans recourir à des fonctions ou méthodes avancées du langage.
- Aucune utilisation de fonctions de recherche ou de tri intégrées. Les opérations de recherche, de tri, d'ajout et de suppression doivent être implémentées manuellement.


### Tâches à Réaliser

**Niveau 1 - Opérations de Base**

1. Fonction `charger_donnees(fichier: str) -> list`
   - Récupérer les données depuis un fichier.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Liste des lignes du fichier après récupération des données contenus dans le fichier d'entré.
  
2. Fonction `supprimer_entete(fichier: str) -> list`
   - Supprime la première ligne (en-tête) du fichier txt.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Liste des lignes du fichier après suppression de l'en-tête.

3. Fonction `supprimer_colonne(fichier: str, nom_colonne: str) -> list`
   - Supprime la colonne spécifiée du fichier txt.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt"), nom de la colonne (ex. "Position").
   - Exemple de sortie : Liste des lignes du fichier après suppression de la colonne.

4. Fonction `lignes_aleatoires(fichier: str, nombre_lignes: int) -> list`
   - Mélanger les lignes au hasard du fichier txt.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt"), nombre de lignes (ex. 5).
   - Exemple de sortie : Liste des lignes sélectionnées au hasard.

5. Fonction `afficher_equipe_trois_lettres(fichier: str) -> list`
   - Affiche le nom de l'équipe en utilisant uniquement les trois premières lettres du nom.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Liste des noms d'équipe abrégés.


### Note

Cette mission permettra de renforcer vos compétences en programmation Python, en algorithmie et en analyse de données, tout en vous plongeant dans l'excitation d'un des événements sportifs les plus importants au monde. Bonne chance !
