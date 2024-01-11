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

3. Fonction `afficher_nom_trois_lettres(str) -> str`
   - Affiche lun texte en utilisant uniquement les trois premières lettres.
   - Exemple d'entrée : Nom du fichier (.. Espagne, France).
   - Exemple de sortie : mot abrégé (ESP, FRA).

4. Fonction `enregistrer_fichier("donnees, fichier.ext") -> fichier.ext`
   - Enregistre les données dans un fichier.
   - Exemple d'entrée : données triées (.. France, Espagne, Argentine).
   - Exemple de sortie : FIFA_1998.txt à jour.

**Niveau 2 - Calculs Statistiques**

1. Fonction `melanger_lignes(donnee) -> list`
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Liste des lignes triées au hasard.

2. Fonction `calculer_points(fichier: str) -> dict`
   - Calcule le nombre de points pour chaque équipe en fonction des victoires et des matchs nuls.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Dictionnaire des équipes et de leurs points.

3. Fonction `calculer_difference_buts(fichier: str) -> dict`
   - Calcule la différence de buts pour chaque équipe.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Dictionnaire des équipes et de leur différence de buts.

**Niveau 3 - Classement et Qualifications**

1. Fonction `supprimer_colonne(fichier: str, nom_colonne: str) -> list`
   - Supprime la colonne spécifiée du fichier txt.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt"), nom de la colonne (ex. "Position").
   - Exemple de sortie : Liste des lignes du fichier après suppression de la colonne.

2. Fonction `trier_par_nom_equipe("donnees") -> list`
   - Trier la liste des équipes par nom.
   - Exemple d'entrée : Nom du fichier (.. France, Espagne, Argentine).
   - Exemple de sortie : la liste des équipes triée par nom abrégé (ARG, ESP, FRA).

3. Fonction `trier_equipes_par_position(donnees) -> list`
   - Trie les équipes par position.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Liste des équipes triées par position.


## Fonctions d'Analyse Statistique :

1. **Histogramme des Points par Équipe**
   - Fonction : `afficher_histogramme_points(data: list) -> None`
   - Affiche un histogramme des points par équipe pour une visualisation rapide des performances.

2. **Podium des Équipes (Top 3)**
   - Fonction : `afficher_podium(data: list) -> None`
   - Affiche le podium, c'est-à-dire les trois meilleures équipes en fonction de leurs points.

3. **Top N Équipes**
   - Fonction : `afficher_top_n(data: list, n: int) -> None`
   - Affiche les meilleures équipes en fonction de leurs points, où N est le nombre d'équipes à afficher.

4. **Équipes Relégables (3 Dernières)**
   - Fonction : `afficher_relegables(data: list) -> None`
   - Affiche les équipes relégables, soit les trois dernières en fonction de leurs points.

5. **Calcul des Ratios**
   - Fonction : `calculer_ratios(data: list) -> dict`
   - Calcule les ratios (but pour/but contre) pour chaque équipe.

6. **Meilleures Attaques**
   - Fonction : `afficher_meilleures_attaques(data: list, n: int) -> None`
   - Affiche les meilleures équipes en termes de buts marqués, où N est le nombre d'équipes à afficher.

7. **Meilleures Défenses**
   - Fonction : `afficher_meilleures_defenses(data: list, n: int) -> None`
   - Affiche les meilleures équipes en termes de buts encaissés, où N est le nombre d'équipes à afficher.

8. **Pires Attaques**
   - Fonction : `afficher_pires_attaques(data: list, n: int) -> None`
   - Affiche les équipes avec les moins de buts marqués, où N est le nombre d'équipes à afficher.

9. **Pires Défenses**
   - Fonction : `afficher_pires_defenses(data: list, n: int) -> None`
   - Affiche les équipes avec le plus de buts encaissés, où N est le nombre d'équipes à afficher.



## Fonctions d'Analyse Historique :

1. **Meilleure Attaque de Tous les Temps**
   - Fonction : `meilleure_attaque_tous_temps(data: list) -> str`
   - Identifie l'équipe avec la meilleure attaque de tous les temps.

2. **Meilleure Défense de Tous les Temps**
   - Fonction : `meilleure_defense_tous_temps(data: list) -> str`
   - Identifie l'équipe avec la meilleure défense de tous les temps.

3. **Pire Attaque de Tous les Temps**
   - Fonction : `pire_attaque_tous_temps(data: list) -> str`
   - Identifie l'équipe avec la pire attaque de tous les temps.

4. **Pire Défense de Tous les Temps**
   - Fonction : `pire_defense_tous_temps(data: list) -> str`
   - Identifie l'équipe avec la pire défense de tous les temps.

5. **Meilleure Équipe de Tous les Temps**
   - Fonction : `meilleure_equipe_tous_temps(data: list) -> str`
   - Identifie l'équipe considérée comme la meilleure de tous les temps.

6. **Meilleur Ratio de Tous les Temps**
   - Fonction : `meilleur_ratio_tous_temps(data: list) -> str`
   - Identifie l'équipe avec le meilleur ratio (but pour/but contre) de tous les temps.

7. **Équipe qui a Participé le Plus**
   - Fonction : `equipe_plus_participee(data: list) -> str`
   - Identifie l'équipe qui a participé au plus grand nombre de Coupes du Monde.

8. **Équipe qui a Participé le Moins**
   - Fonction : `equipe_moins_participee(data: list) -> str`
   - Identifie l'équipe qui a participé au moins de Coupes du Monde.

9. **Équipe avec le Plus de Victoires en Finale**
   - Fonction : `equipe_plus_victoires_finale(data: list) -> str`
   - Identifie l'équipe qui a remporté le plus grand nombre de titres de champion du monde.

10. **Meilleurs Vice-Champions du Monde**
    - Fonction : `meilleurs_vice_champions(data: list, n: int) -> list`
    - Identifie les équipes qui ont été les meilleurs vice-champions, où N est le nombre d'équipes à afficher.

11. **Meilleurs Troisièmes**
    - Fonction : `meilleurs_troisiemes(data: list, n: int) -> list`
    - Identifie les équipes qui ont été les meilleurs troisièmes, où N est le nombre d'équipes à afficher.


## Visualisations Graphiques

### Histogramme des Points

**Fonction :** `afficher_histogramme_points(data) -> None`

Affiche un histogramme des points marqués par chaque équipe.

### Diagramme en Camembert des Top N Équipes

**Fonction :** `afficher_camembert_top_n(data, n) -> None`

Affiche un diagramme en camembert des meilleures équipes (Top N) en fonction des points.

### Diagramme en Secteurs des Attaques et Défenses

**Fonction :** `afficher_diagramme_secteurs(data) -> None`

Affiche un diagramme en secteurs illustrant les performances d'attaque et de défense des équipes.

### Graphique des Top 3 au Fil des Années

**Fonction :** `afficher_graphique_top_3_annees(data) -> None`

Affiche un graphique montrant l'évolution des trois meilleures équipes au fil des années.

### Heatmap des Performances

**Fonction :** `afficher_heatmap(data) -> None`

Affiche une heatmap des performances des équipes dans différentes catégories.


### Visualisation par Pays

#### Carte des Performances

**Fonction :** `afficher_carte_performances(data) -> None`

Affiche une carte géographique avec des codes couleur pour représenter les performances des équipes par pays.

#### Diagramme en Barres par Pays

**Fonction :** `afficher_diagramme_barres_pays(data) -> None`

Affiche un diagramme en barres représentant les performances des différents pays.

### Comparaisons Temporelles

#### Graphique des Évolutions de Points

**Fonction :** `afficher_evolution_points(data) -> None`

Affiche un graphique montrant l'évolution des points des équipes au fil des années.

#### Graphique des Évolutions de Buts Marqués/Encaissés

**Fonction :** `afficher_evolution_buts(data) -> None`

Affiche un graphique montrant l'évolution du nombre de buts marqués et encaissés par les équipes au fil des années.

### Analyses Comparatives

#### Radar Chart des Performances

**Fonction :** `afficher_radar_chart(data) -> None`

Affiche un radar chart comparant les performances des équipes dans différentes catégories.

#### Graphique en Aire des Performances Globales

**Fonction :** `afficher_graphique_aire_global(data) -> None`

Affiche un graphique en aire représentant les performances globales des équipes.

### N'hésitez pas à ajouter d'autres fonctionnalités spécifiques aux données que vous avez pour rendre l'analyse encore plus riche !


   


### Note

Cette mission permettra de renforcer vos compétences en programmation, en algorithmie et en analyse de données, tout en vous plongeant dans l'excitation d'un des événements sportifs les plus importants au monde. Bonne chance !
