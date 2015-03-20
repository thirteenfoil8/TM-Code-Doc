####################
L'application exercice, c'est quoi ?
####################

--------------------------------------
Introduction
--------------------------------------

Voici la documentation de l'application ``Exercice`` présente sur le site `suivant <https://webmath-thirteenfoil8.c9.io/exercises/>`_ . Celle-ci vous premettra de
pouvoir utiliser la partie création ainsi que la partie résolution des exercices de manière complète et détaillée. Cette application servira par la suite à un 
professeur de pouvoir créer un exercice ( principalement de factorisation ou bien de calcul) et de pouvoir le mettre en ligne. Il suffira de donner le lien de
l'exercice à l'élève pour qu'il puisse le résoudre. 

Cette application consiste en premier lieu à avoir un support internet sur lequel un élève du Csud pourrait s'entraîner en prévision de ses examens ou alors tout simplement
pour perfectionner ses capacités en mathématique dans le domaine de la factorisation et dans celui du calcul. Elle est essentielle au projet pour que les professeurs puissent
créer des exercices selon le besoin de leur élève et pour pouvoir analyser les erreurs que les élèves font par rapport à ceux-ci. Cela permet aussi à un élève de savoir où sont
ses difficultés et de savoir quelles sont les thèmes qu'il doit travailler. Django permet de pouvoir stocker les données créées par les
professeurs dans une base de données et de pouvoir récupérer celle-ci pour en faire des pages. Cela est exactement ce dont nous avons besoin pour cette application car le 
professeur en question créé un exercice et la partie backend très développée de Django s'occupe de créer la page web contenant les données entrées précédemment.

--------------------------------------
La collaboration dans le projet
--------------------------------------

Pour ce qui est de la collaboration avec les autres applications du projet, il faudrait au minimum que les fonctionnalités suivantes soit disponible:

* La collaboration avec le dashboard élève:

    * L'élève doit pouvoir ajouter les liens des exercices qu'il a trouvé compliqués.
    
    * Il doit pouvoir avoir un Feedback des exercices qu'il a déjà fait.
    
    * Il doit pouvoir mettre les liens des exercices à faire pour les devoirs ou autres dans un dossier.

* La collaboration avec le dashboard professeur :
    
    * Le professeur doit pouvoir faire des dossiers avec les exercices qu'il a créés. 
    
    * Il doit également pouvoir prendre des exercices d'autres professeurs pour les intégrer dans un dossier.

* La collaboration avec les cours:

    * Un cours doit pouvoir contenir les liens des exercices qui sont en rapport avec ceux-ci.
    
    * Il faudrait pouvoir faire un dossier dans le cours avec les corrigés des exercices faisant partis de celui-ci.

* La collaboration avec les quiz:
    
    * Il faudrait pouvoir mettre en relation un exercice ou bien un groupe d'exercices avec un ou plusieurs quiz ayant le même but pédagogique.


--------------------------------------
Intégration de l'application 
--------------------------------------

L'intégration de cette application au reste du projet ne devrait normalement pas poser trop de problèmes. La manière la plus simple de faire correspondre les exercices à des cours ou autres est
d'utiliser les liens des exercices pour pouvoir y accéder.
    


--------------------------------------
Le template de base du site
--------------------------------------
Pour ce qui est du Frontend, suite à une mise en commun avec Benoît Léo, le créateur de l'application quiz, nous nous sommes mis d'accord pour utiliser le même 
template de base bootstrap ce trouvant `ici <http://startbootstrap.com/template-overviews/shop-item/>`_ .

Pour ce qui est de la barre latéral se trouvant à gauche des pages du site, il a fallu mettre des liens vers les différents template. Ceci se fait non pas en recopiant le lien
de la page web directement mais en utilisant une commande django simple qui permet, si il y a un changement d'url par la suite dans le fichier urls.py de faire automatiquement le changement 
pour éviter les erreurs de redirection. 

le code est le suivant :

.. code-block:: python

    <div class="list-group">
        <a href="{% url 'exercises:index' %}" class="list-group-item {% block active-home %}
        active{% endblock %}">Accueil</a>
        <a href="{% url 'exercises:find' %}" class="list-group-item {% block active-reso %}
        {% endblock %}">Résoudre un exercice</a>
        <a href="{% url 'exercises:create' %}" class="list-group-item {% block active-create %}
        {% endblock %}">Création d'exercice</a>
    </div>
    
Comme vous pouvez le constater, un block {% block active %} a été ajouté à chaque lien. Ceci permet d'activer la classe "list-group-item" dans la page actuel.

-------------------------------------
Les modèles 
-------------------------------------

Les modèles de l'application Exercice ne sont pas très nombreux. Ils servent surtout à la création et à la résolution des exercices. ( A compléter)