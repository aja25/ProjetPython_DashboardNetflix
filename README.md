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
        <li><a href="#prerequis">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#Exécution du Projet">Exécution du Projet</a></li>
      </ul>
    </li>
    <li>
      <a href="#Guide du Développeur">Guide du Développeur</a></li>
      <ul>
        <li><a href="#Nettoyage des Données">Nettoyage des Données</a></li>
        <li>
          <a href="#dashboard">Tableau de Bord</a>
            <ul>
              <li><a href="#Interface Utilisateur">Interface Utilisateur</a></li>
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
### Prerequis

Vous devez installer des packages pour éxecuter le projet.
Le moyen le plus simple est d'éxecuter la ligne de commande suivante.

* Install prerequis
  ```sh
  python -m pip install -r requirements.txt
  ```

Pour obtenir le projet, vous devez le cloner avec la commande suivante :

* Cloner le dépôt git
  ```sh
  [git clone (https://github.com/aja25/ProjetPython_DashboardNetflix.git)]

### Installation

Mais si vous voulez les installer une à une, vous pouvez les télécharger avec ces commandes.

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


### Executer le projet
S'il n'ya aucune erreur, vous pouvez éxecuter le projet avec la commande suivante: 
 ```sh
  python main.py
  ```
Dashboard est présent à l'url : http://127.0.0.1:80/

<p align="right">(<a href="#top">back to top</a>)</p>


## Guide du Développeur

Ce projet est divisé en deux parties principales :
*data.py
*dashboard.py

### Nettoyage des Données

Le fichier `data.py` est responsable du téléchargement et du nettoyage initial des données. Le processus commence par le téléchargement du jeu de données depuis Kaggle. Une fois le jeu de données téléchargé, il est lu et nettoyé pour s'assurer qu'il est formaté correctement et prêt à être utilisé dans le tableau de bord. Cette étape inclut le remplissage des valeurs manquantes, la correction des types de données et l'extraction des informations pertinentes pour l'analyse. Le nettoyage des données est une étape cruciale pour garantir l'exactitude des informations affichées dans le tableau de bord.

### Tableau de Bord

Le fichier `dashboard.py` gère la logique et la présentation du tableau de bord interactif. Le tableau de bord est construit en utilisant Dash et Plotly, offrant une interface utilisateur dynamique et des visualisations interactives. Il est structuré de la manière suivante :

#### Interface Utilisateur (Frontend)

L'interface utilisateur est conçue pour être intuitive et facile à utiliser. Elle est organisée en onglets, chacun affichant différents types de visualisations (graphiques en ligne, camemberts, cartes choroplèthes, etc.). Les utilisateurs peuvent interagir avec les visualisations en utilisant divers contrôles comme des listes déroulantes et des boutons radio pour filtrer et affiner les données affichées.

#### Logique de l'Application (Backend)

Le backend est l'endroit où la magie opère pour récupérer, traiter et visualiser les données. Il utilise les données nettoyées fournies par `data.py` et les transforme en visualisations interactives. Le backend gère également les interactions de l'utilisateur, en répondant dynamiquement aux entrées et en ajustant les visualisations en conséquence. Cette partie du code est essentielle pour assurer que le tableau de bord ne se contente pas d'afficher des données, mais fournisse une expérience interactive et informative à l'utilisateur.

###  Modifier/Ajouter du code
Pour modifier une figure, il suffit d'aller dans le fichier où elle se trouve (dashboard.py) et la modifier directement. Pour ajouter une figure, il faut, si besoin, créer une fonction de tri/nettoyage dans data_processing.py, puis selon si elle contient une carte ou non la créer dans maps.py ou graphs.py. Pour l'afficher, il faudra :

* Si elle doit apparaitre lors de l'initialisation du dashboard, l'ajouter comme paramètre dans la fonction create_dashboard que l'on modifiera dans le fichier dashboard.py. Dans cette fonction, vous pouvez créer de nouveaux onglets pour afficher de nouvelles figures, ou l'ajouter à la suite d'autres figures dans des onglets déjà existants.

### Ajout Supplémentaire 

"app.run_server(debug=True, port=80)" cette ligne de code se trouve dans le fichier dashboard.py, et nous avons ajouter le port=80.
