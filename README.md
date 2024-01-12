# ProjetPython_DashboardNetflix

<!-- LOGO DU PROJET -->
<br />
<div align="center">

  <h3 align="center">Tableau de Bord de Séries et Films en Python</h3>

</div>

<!-- TABLE DES MATIÈRES -->
<details>
  <summary>Table des Matières</summary>
  <ol>
    <li>
      <a href="#about-the-project">À propos du Projet</a>
      <ul>
        <li><a href="#built-with">Construit Avec</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Pour Commencer</a>
      <ul>
        <li><a href="#prerequisites">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#run project">Exécution du Projet</a></li>
      </ul>
    </li>
    <li>
      <a href="#developer_guide">Guide du Développeur</a></li>
      <ul>
        <li><a href="#data_cleaning">Nettoyage des Données</a></li>
        <li>
          <a href="#dashboard">Tableau de Bord</a>
            <ul>
              <li><a href="#frontend">Interface Utilisateur</a></li>
              <li><a href="#backend">Backend</a></li>
            </ul>
        </li>
      </ul>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- À PROPOS DU PROJET -->
## À propos du Projet

Il s'agit d'un projet de deuxième année d'études d'ingénierie.
Il s'est déroulé sur deux périodes : le mois d'octobre, ainsi que le mois de décembre.
L'objectif est de créer un tableau de bord interactif avec une carte et un histogramme.
Le jeu de données est disponible sur Kaggle :
[www.kaggle.com/ashishgup/netflix-rotten-tomatoes-metacritic-imdb.](https://www.kaggle.com/datasets/shivamb/netflix-shows)

Ce jeu de données combine des sources de données de Netflix, Rotten Tomatoes, IMBD, des affiches, des informations sur le box-office,
des bandes-annonces sur YouTube, et plus encore en utilisant une variété d'APIs.
Notez qu'il n'existe pas d'API officielle Netflix.

"Hidden Gem Score" est calculé en utilisant un faible nombre de critiques et une note élevée. Plus le nombre de critiques est faible et plus la note des utilisateurs est élevée, plus le score de gemme cachée est élevé.

Utilisez le `README.md` pour démarrer.

<p align="right">(<a href="#top">retour en haut</a>)</p>

### Construit Avec

Ce projet est écrit en Python 3.11.7 et utilise une liste de bibliothèques pour son initialisation.

* [Pandas.py](https://pandas.pydata.org)
* [Numpy.py](https://numpy.org)
* [Plotly-express.py](https://plotly.com/python/plotly-express/)
* [Dash.py](https://dash.plotly.com)
* [Os.py](https://docs.python.org/fr/3/library/os.html)
* [Kaggle.py](https://github.com/Kaggle/kaggle-api)

<p align="right">(<a href="#top">retour en haut</a>)</p>

<!-- POUR COMMENCER -->
## Pour Commencer

Pour obtenir le projet, vous devez le cloner avec la commande suivante :

* Cloner le dépôt git
  ```sh
  [git clone (https://github.com/aja25/ProjetPython_DashboardNetflix.git)]
