####################
Introduction
####################

------------------------------------------------------------------
Approche personnelle par rapport à l'application dans le séminaire
------------------------------------------------------------------

Suite à la lecture des sujets de travail de maturité, je me suis senti particulièrement intéressé et attiré par le sujet du *Développement d'une plateforme Web d'e-learning*.
En effet, depuis mon plus jeune âge, le monde de l'informatique et de la technologie font partie intégrante de ma vie. De plus, les mathématiques cultivent
ma curiosité et me fascinent. De ce fait, ce travail de maturité était parfait pour moi.
 
Une des premières choses qu'un élève du secondaire II apprend lors de ses cours de mathématiques est l'algèbre de base. C'est pourquoi j'ai choisi
la partie du site Web concernant l'*application d'exercices interactifs sur les polynômes du premier et deuxième degré*.
L'objectif de base pour qu'une application de ce type puisse fonctionner est bien évidemment qu'un professeur crée un exercice afin 
qu'un élève le résolve en sachant si sa résolution est correcte ou non. C'est à l'aide de la création de corrigés d'exercices que l'élève pourra se perfectionner.
Pour arriver à ce résultat, la méthode la plus simple est d'utiliser un framework possédant un système de stockage et d'une partie s'occupant des 
requêtes de l'utilisateur. Le framework Django écrit sous le language de programmation Python est idéal pour cette tâche

--------------------------------------
Le but de l'application
--------------------------------------

Voici la documentation de l'application ``exercises`` présente sur le site `suivant <https://webmath-thirteenfoil8.c9.io/exercises/>`_ [#f1]_ . Celle-ci permet d'utiliser
la partie création ainsi que la partie résolution des exercices de manière complète et détaillée. Cette application servira par la suite au
professeur à réaliser un exercice de factorisation ou de développemennt puis de le mettre en ligne. Il suffira de donner le lien de
l'exercice à l'élève pour qu'il puisse le résoudre. 

Cette application consiste en premier lieu à avoir un support internet sur lequel un élève du Collège du Sud pourra s'entraîner en prévision de ses examens ou alors tout simplement
pour perfectionner ses capacités en mathématiques dans le domaine de la factorisation et dans celui du calcul. Celle-ci permet au professeur d'adapter son exercice
aux besoins de ses élèves. Cette application aide également l'élève à connaître ses lacunes et s'améliorer.
Django permet de stocker les données créées par les professeurs dans une base de données et de récupérer celles-ci pour en faire des pages Web.
C'est exactement ce dont on a besoin pour cette application car le professeur crée un exercice et la partie backend très développée de Django
s'occupe de créer la page web contenant les données entrées précédemment.

--------------------------------------
La collaboration dans le projet
--------------------------------------

Pour ce qui est de la collaboration avec les autres applications du projet, il faudrait au minimum que les fonctionnalités suivantes soient disponibles:

* La collaboration avec le dashboard élève:

  * L'élève doit pouvoir ajouter les liens des exercices qu'il a trouvé compliqués.
  
  * Il doit avoir un Feedback des exercices. 
  
  * Il doit pouvoir mettre les liens des exercices à faire pour les devoirs ou autres dans un dossier.

* La collaboration avec le dashboard professeur :

  * Le professeur doit pouvoir faire des dossiers avec les exercices qu'il a créés. 
  
  * Il doit également pouvoir prendre des exercices d'autres professeurs pour les intégrer dans un dossier.

* La collaboration avec les cours:

  * Un cours doit contenir les liens des exercices qui sont en rapport avec celui-ci.

* La collaboration avec les quiz:

  * Il faudrait mettre en relation un exercice ou bien un groupe d'exercices avec un ou plusieurs quiz ayant le même but pédagogique.


--------------------------------------
Intégration de l'application 
--------------------------------------

L'intégration de cette application au reste du projet ne devrait normalement pas poser de problème. La manière la plus simple de faire correspondre les exercices à des cours est
d'utiliser les liens des exercices pour pouvoir y accéder.

.. rubric::
    
.. [#f1] Le lien de la page d'accueil: https://webmath-thirteenfoil8.c9.io/exercises/