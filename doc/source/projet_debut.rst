####################
Introduction
####################

--------------------------------------
Le but de l'application
--------------------------------------

Voici la documentation de l'application ``Exercice`` présente sur le site [#f1]_ `suivant <https://webmath-thirteenfoil8.c9.io/exercises/>`_ . Celle-ci permet de
pouvoir utiliser la partie création ainsi que la partie résolution des exercices de manière complète et détaillée. Cette application servira par la suite à un 
professeur de pouvoir créer un exercice de factorisation ou de développemennt et de pouvoir le mettre en ligne. Il suffira de donner le lien de
l'exercice à l'élève pour qu'il puisse le résoudre. 

Cette application consiste en premier lieu à avoir un support internet sur lequel un élève du Collège du Sud pourra s'entraîner en prévision de ses examens ou alors tout simplement
pour perfectionner ses capacités en mathématique dans le domaine de la factorisation et dans celui du calcul. Elle est essentielle au projet pour que les professeurs puissent
créer des exercices selon le besoin de leurs élèves et pour pouvoir analyser les erreurs que les élèves font par rapport à ceux-ci. Cela permet aussi à un élève de savoir où sont
ses difficultés et de savoir quelles sont les thèmes qu'il doit travailler. Django permet de stocker les données créées par les
professeurs dans une base de données et de récupérer celles-ci pour en faire des pages. C'est exactement ce dont on a besoin pour cette application car le 
professeur crée un exercice et la partie backend très développée de Django s'occupe de créer la page web contenant les données entrées précédemment.

--------------------------------------
La collaboration dans le projet
--------------------------------------

Pour ce qui est de la collaboration avec les autres applications du projet, il faudrait au minimum que les fonctionnalités suivantes soit disponible:

* La collaboration avec le dashboard élève:

    * L'élève doit pouvoir ajouter les liens des exercices qu'il a trouvé compliqués.
    
    * Il doit pouvoir avoir un Feedback des exercices. 
    
    * Il doit pouvoir mettre les liens des exercices à faire pour les devoirs ou autres dans un dossier.

* La collaboration avec le dashboard professeur :
    
    * Le professeur doit pouvoir faire des dossiers avec les exercices qu'il a créés. 
    
    * Il doit également pouvoir prendre des exercices d'autres professeurs pour les intégrer dans un dossier.

* La collaboration avec les cours:

    * Un cours doit pouvoir contenir les liens des exercices qui sont en rapport avec celui-ci.

* La collaboration avec les quiz:
    
    * Il faudrait pouvoir mettre en relation un exercice ou bien un groupe d'exercices avec un ou plusieurs quiz ayant le même but pédagogique.


--------------------------------------
Intégration de l'application 
--------------------------------------

L'intégration de cette application au reste du projet ne devrait normalement pas poser trop de problèmes. La manière la plus simple de faire correspondre les exercices à des cours est
d'utiliser les liens des exercices pour pouvoir y accéder.

.. rubric::
    
.. [#f1] Le lien de la page d'accueil: https://webmath-thirteenfoil8.c9.io/exercises/