# Leçon 3 : Analyse de fichiers CSV (jeu de données sur les changements de température)

Ce dossier contient les ressources techniques de la leçon 3, qui porte sur l'analyse de fichiers CSV à partir d'un jeu de données sur les changements de température au Canada.

## Informations sur l'ensemble de données
* **Source :** Environnement et Changement climatique Canada (2025)
* **Nom de l'ensemble de données :** Changements de la température au Canada
* **URL original :** [Portail du gouvernement ouvert](https://open.canada.ca/data/en/dataset/8b01db78-b825-4d38-a66c-1a1712c382ee)
* **Page de l'indicateur :** [Changements de la température - ECCC](https://www.canada.ca/fr/environnement-changement-climatique/services/indicateurs-environnementaux/changements-temperature.html)
* **Période de référence :** 1948 à 2024
* **Base de référence :** Moyenne de 1961-1990

## Fichiers
* `notebook.ipynb` : Le cahier Jupyter pour les étudiants.
* `data_en.csv` : Fichier CSV nettoyé en anglais.
* `data_fr.csv` : Une version nettoyée du fichier CSV officiel d'Environnement Canada.

## Notes sur le nettoyage des données
Les fichiers CSV de ce dossier ont été modifiés pour une utilisation en classe :
1. **Nettoyage de l'en-tête :** Les en-têtes descriptifs et les lignes vides en haut du fichier ont été supprimés.
2. **Standardisation des colonnes :**
   * Anglais : `Year`, `Temperature departure (degree Celsius)`, `Warmest year ranking`
   * Français : `Année`, `Écart de températures (degrés Celsius)`, `Classement des années les plus chaudes`
3. **Relocalisation des notes de bas de page :** Les notes de bas de page et les citations ont été déplacées dans ce README.

## Notes de bas de page originales
* **Écart de température :** L'écart de température est la différence entre la température moyenne pour une année donnée et la température moyenne de la période de référence (1961 à 1990).
* **Rang :** "1" indique l'année la plus chaude enregistrée depuis 1948. 2024 et 2010 sont à égalité pour l'année la plus chaude.
* **Citation :** Environnement et Changement climatique Canada (2025) Indicateurs environnementaux canadiens : Changements de la température au Canada.
