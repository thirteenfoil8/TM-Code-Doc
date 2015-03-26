####################
Introduction
####################

------------------------------------------------------------------
Approche personnelle par rapport à l'application dans le séminaire
------------------------------------------------------------------

Suite à la lecture des sujets de travail de maturité, je me suis senti particulièrement intéressé par le sujet de l'informatique. 
En effet, depuis mon plus jeune âge, le monde de l'informatique et de la technologie font partie intégrante de ma vie. De plus, 
le sujet de ce travail de maturité étant *Conception d'une plateforme de e-learning* concernant surtout les mathématiques a joué un rôle 
important dans mon choix car les mathématiques sont un domaine complexe et très intéressant. De ce fait, ce travail de maturité était parfait pour moi 
en ce qui concerne ma curiosité et mon envie d'en apprendre plus sur l'informatique.
 
Une des premières choses qu'un élève du secondaire II apprend lors de ses cours de mathématiques est l'algèbre de base. C'est pourquoi j'ai choisi
la partie du site Web concernant le *développement d'une application de création d'exercices de factorisation et de développement*.
Les objectifs de base pour qu'une application de ce type puisse fonctionner sont bien évidemment qu'un professeur puisse créer un exercice et 
qu'un élève puisse le résoudre en sachant si sa résolution est juste ou fausse. Relativement à ce dernier point, la méthode la plus simple est de 
permettre au professeur de créer un corrigé de l'exercice que l'élève pourra voir par la suite. 
Pour arriver à un tel résultat, la méthode la plus simple est d'utiliser un framework possédant un système de base de données et d'une partie s'occupant des 
requêtes de l'utilisateur. Pour cela, le framework Django écrit sous le language de programmation Python est idéal car il possède tous les points précédemment 
cités.

--------------------------------------
Le but de l'application
--------------------------------------

Voici la documentation de l'application ``Exercice`` présente sur le site `suivant <https://webmath-thirteenfoil8.c9.io/exercises/>`_ [#f1]_ . Celle-ci permet de
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