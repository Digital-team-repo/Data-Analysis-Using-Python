# Analyse de données avec Python

Ce dépôt a été conçu à des fins éducatives.

## Liens de lancement des carnets

- Leçon 2 : Introduction à l’analyse des données
  - Voir le carnet : <https://github.com/Digital-team-repo/Data-Analysis-Using-Python/blob/main/2-data-analysis-intro/notebook_fr.ipynb>
  - Ouvrir dans Colab : <https://colab.research.google.com/github/Digital-team-repo/Data-Analysis-Using-Python/blob/main/2-data-analysis-intro/notebook_fr.ipynb>
  - Ouvrir dans Callysto : <https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDigital-team-repo%2FData-Analysis-Using-Python&branch=main&subPath=2-data-analysis-intro/notebook_fr.ipynb>

- Leçon 3 : Fondements des carnets Jupyter
  - Voir le carnet de démonstration : <https://github.com/Digital-team-repo/Data-Analysis-Using-Python/blob/main/3-jupyter-foundations/demo-notebook_fr.ipynb>
  - Ouvrir le carnet de démonstration dans Colab : <https://colab.research.google.com/github/Digital-team-repo/Data-Analysis-Using-Python/blob/main/3-jupyter-foundations/demo-notebook_fr.ipynb>
  - Ouvrir le carnet de démonstration dans Callysto : <https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDigital-team-repo%2FData-Analysis-Using-Python&branch=main&subPath=3-jupyter-foundations/demo-notebook_fr.ipynb>
  - Voir le carnet de travail : <https://github.com/Digital-team-repo/Data-Analysis-Using-Python/blob/main/3-jupyter-foundations/assignment-notebook_fr.ipynb>
  - Ouvrir le carnet de travail dans Colab : <https://colab.research.google.com/github/Digital-team-repo/Data-Analysis-Using-Python/blob/main/3-jupyter-foundations/assignment-notebook_fr.ipynb>
  - Ouvrir le carnet de travail dans Callysto : <https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDigital-team-repo%2FData-Analysis-Using-Python&branch=main&subPath=3-jupyter-foundations/assignment-notebook_fr.ipynb>
  - Voir l’exemple de la soirée arcade : <https://github.com/Digital-team-repo/Data-Analysis-Using-Python/blob/main/3-jupyter-foundations/examples/arcade-leaderboard-notebook_fr.ipynb>
  - Ouvrir l’exemple de la soirée arcade dans Colab : <https://colab.research.google.com/github/Digital-team-repo/Data-Analysis-Using-Python/blob/main/3-jupyter-foundations/examples/arcade-leaderboard-notebook_fr.ipynb>
  - Ouvrir l’exemple de la soirée arcade dans Callysto : <https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDigital-team-repo%2FData-Analysis-Using-Python&branch=main&subPath=3-jupyter-foundations/examples/arcade-leaderboard-notebook_fr.ipynb>

- Leçon 4 : Importation de fichiers CSV
  - Voir le carnet : <https://github.com/Digital-team-repo/Data-Analysis-Using-Python/blob/main/4-csv-analysis/notebook_fr.ipynb>
  - Ouvrir dans Colab : <https://colab.research.google.com/github/Digital-team-repo/Data-Analysis-Using-Python/blob/main/4-csv-analysis/notebook_fr.ipynb>
  - Ouvrir dans Callysto : <https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDigital-team-repo%2FData-Analysis-Using-Python&branch=main&subPath=4-csv-analysis/notebook_fr.ipynb>

- Leçon 5 : Analyse de fichiers Excel
  - Voir le carnet : <https://github.com/Digital-team-repo/Data-Analysis-Using-Python/blob/main/5-excel-analysis/notebook_fr.ipynb>
  - Ouvrir dans Colab : <https://colab.research.google.com/github/Digital-team-repo/Data-Analysis-Using-Python/blob/main/5-excel-analysis/notebook_fr.ipynb>
  - Ouvrir dans Callysto : <https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDigital-team-repo%2FData-Analysis-Using-Python&branch=main&subPath=5-excel-analysis/notebook_fr.ipynb>

- Leçon 6 : Épuration des données
  - Voir le carnet : <https://github.com/Digital-team-repo/Data-Analysis-Using-Python/blob/main/6-data-cleaning/notebook_fr.ipynb>
  - Ouvrir dans Colab : <https://colab.research.google.com/github/Digital-team-repo/Data-Analysis-Using-Python/blob/main/6-data-cleaning/notebook_fr.ipynb>
  - Ouvrir dans Callysto : <https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDigital-team-repo%2FData-Analysis-Using-Python&branch=main&subPath=6-data-cleaning/notebook_fr.ipynb>

## Exécuter les carnets localement

Le fichier `requirements.txt` de ce dossier contient les bibliothèques Python nécessaires pour exécuter les carnets en français.

### Installer les bibliothèques sous Windows

Ouvrez PowerShell dans le dossier `OSC-repo`, puis exécutez :

```powershell
python -m pip install -r .\requirements.txt
```

### Installer les bibliothèques sous macOS

Ouvrez Terminal dans le dossier `OSC-repo`, puis exécutez :

```bash
python3 -m pip install -r ./requirements.txt
```

### Ouvrir un carnet dans VS Code

1. Installez les extensions **Python** et **Jupyter** pour VS Code.
2. Ouvrez le dossier `OSC-repo` dans VS Code.
3. Ouvrez le fichier `.ipynb` en français que vous souhaitez utiliser.
4. Sélectionnez **Kernel** ou **Select Kernel** dans la barre d’outils du carnet.
5. Choisissez l’environnement Python dans lequel vous avez installé `requirements.txt`.
6. Exécutez les cellules du carnet dans l’ordre.

### Facultatif : utiliser JupyterLab

JupyterLab est inclus dans `requirements.txt`, mais il n’est pas obligatoire si vous utilisez VS Code ou un autre éditeur compatible avec les carnets.

Sous Windows, ouvrez PowerShell dans le dossier `OSC-repo`, puis exécutez :

```powershell
python -m jupyter lab
```

Sous macOS, ouvrez Terminal dans le dossier `OSC-repo`, puis exécutez :

```bash
python3 -m jupyter lab
```
