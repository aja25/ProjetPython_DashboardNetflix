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
[(https://www.kaggle.com/datasets/shivamb/netflix-shows/data)](https://www.kaggle.com/datasets/shivamb/netflix-shows)

Ce jeu de données combine des sources de données de Netflix tels que le titre, les directeurs, les acteurs qui ont travaillés sur le projet.
Notez qu'il n'existe pas d'API officielle Netflix.


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
### Prerequisites

You need to install packages to run project.
The simpler way is to run the following code.

* Install prerequisites
  ```sh
  python -m pip install -r requirements.txt
  ```

Pour obtenir le projet, vous devez le cloner avec la commande suivante :

* Cloner le dépôt git
  ```sh
  [git clone (https://github.com/aja25/ProjetPython_DashboardNetflix.git)]

### Installation

But if you want to install separately you can install one by one like follow.

1. Pandas
  ```sh
  pip install pandas
  ```
2. Numpy
  ```sh
  pip install numpy
  ```
3. Dash
  ```sh
  pip install dash
  ```
4. Plotly
  ```sh
  pip install plotly
  ```
5. Kaggle
  ```sh
  pip install kaggle
  ```


### Run project
If no error appear, you can run the project by execute the command follow : 
 ```sh
  python main.py
  ```
Dashboard is present on url : http://127.0.0.1:80/

<p align="right">(<a href="#top">back to top</a>)</p>


### Developer's guide 
There is two main parts for the code  :
. data.py
. dashboard.py




