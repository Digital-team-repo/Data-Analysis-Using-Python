# Annexe : Importer des données à partir d'une feuille Google

L’importation de données à partir d’une feuille Google est semblable à l’importation d’un fichier CSV en ligne. La principale différence est qu’il faut modifier l’adresse URL de Google Sheets afin que l’onglet sélectionné soit fourni sous forme de données CSV.

## CSV ou feuille Google

Pour un fichier CSV, les données sont déjà au format CSV et l’adresse URL du fichier peut être utilisée directement.

Pour une feuille Google, remplacez la fin de l’adresse URL de partage :

```text
/edit#gid=0
```

par :

```text
/export?format=csv
```

L’adresse URL complète suit ce modèle :

```text
https://docs.google.com/spreadsheets/d/SHEET_ID/export?format=csv
```

`SHEET_ID` identifie le fichier tableur. Cette adresse exporte l’onglet par défaut, soit le premier onglet. Ajoutez `&gid=TAB_ID` seulement pour importer un autre onglet. Le `TAB_ID` est le nombre affiché après `gid=` dans l’adresse URL de Google Sheets.

La modification importante est `format=csv`. Elle demande à Google Sheets d’envoyer l’onglet sous forme de données CSV. Une fois l’adresse URL modifiée, les données peuvent être chargées avec le même processus `pd.read_csv(data_url)` que pour un fichier CSV en ligne.

## Conditions importantes

Le droit d’accès en lecture de la feuille de calcul doit être public afin que le notebook puisse récupérer l’exportation CSV. Ne publiez pas de renseignements personnels ou permettant d’identifier des élèves.

Pour faciliter le travail des débutants, placez les noms des colonnes dans la première ligne de la feuille. Après l’importation, vérifiez que les noms de colonnes et les lignes attendus apparaissent avant de commencer l’analyse.

## Résumé du processus

**Feuille Google → modifier l’adresse URL pour inclure `format=csv` → importer comme CSV → inspecter les données**
