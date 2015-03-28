####################################
Documentation du développeur
####################################

Cette partie de la documentation est essentiellement destinée au développeur qui aimerait comprendre comment cette application fonctionne.
Tout ce qui concerne les modèles, les vues, les urls, les templates, ... est affiché ci-dessous. Le code est accompagné de quelques annotations mais celles-ci sont là 
que pour donner quelques précisions quant à celui-ci. Il est donc nécéssaire de connaître les languages de programmation et les frameworks suivant pour comprendre la documentation 
développeur: 

* Les languages de programmation:

  * `Python <https://docs.python.org/3/>`_ [#f1]_
  
  * `Html  <http://overapi.com/html/>`_ [#f2]_ 
  
  * `Css  <http://overapi.com/css/>`_ [#f3]_
  
  * `Javascript  <http://overapi.com/javascript/>`_ [#f4]_
    
* Les FrameWorks:

  * `Bootstrap  <http://getbootstrap.com/getting-started/>`_ [#f5]_ 
  
  * `jQuery  <http://overapi.com/jquery/>`_ [#f6]_ 
  
  * `Django  <https://docs.djangoproject.com/en/1.7/>`_ [#f7]_ 
  
  


.. raw:: latex

    \pagebreak

---------------------------------
Démarrage du projet depuis Cloud9
---------------------------------

L'utilisation de l'environnement Web `Cloud9 <https://c9.io/>`_ [#f8]_ est très utile. Cela permet de ne pas surcharger la machine sur laquelle on travaille et le code est accessible depuis nimporte quel 
ordinateur dans le mode possédant une connection internet.

Une fois sur Cloud9, il faut créer un *Workspace custom* en cliquant sur l'onglet *create new workspace*. 
Voici la série de commande à entrer pour pouvoir démarrer le projet :

.. code-block:: python

    #installer django
    sudo pip3 install django
    
    #installer pillow qui gère les images de l'application common
    sudo pip3 install pillow
    
    #cloner le dépôt git 
    git clone https://github.com/thirteenfoil8/TM-Code-Doc
    
    #Lancer le serveur
    python3 manange.py runserver $IP:$PORT


Il est a noté que le projet contenant l'entier des fichiers est sur un `dépôt <https://github.com/thirteenfoil8/TM-Code-Doc>`_ [#f9]_ GitHub. 
Une fois ces commandes entrées dans le ``bash``, l'entier du projet sera présent dans le *workspace*.




--------------------------------------
Les modèles
--------------------------------------

1. Les modèles de cette application sont les suivants:
    * ``Exercise``
        
        Ce modèle contient les informations relatives à un exercice en particulier. Il contient le nom du créateur : ``owner``, la date de création : ``created_on``, 
        le titre de l'exercice : ``title`` ( celui-ci ne possède que 4 choix présents dans le template ``create.html`` présent plus bas dans la documentation ), 
        l'équation que l'élève devra traîter : ``equation``, la difficulté de l'exercice : ``grade`` ( choisi entre 1 et 5 également dans ``create.html`` ), 
        et enfin la correction de l'exercice : ``correction``.
        La fonction ``def __str__(self)`` sert uniquement à rendre quelque chose de plus propre sur la `page <http://webmath-thirteenfoil8.c9.io/admin/>`_ [#f10]_ prévue pour les admins du site.
    
    * ``Exercise_done``
        
        Ce modèle contient les informations concernant une résolution à un exercice fait par un élève. Il contient le nom de l'élève : ``student``, la date à laquelle l'élève a fait l'exercice : 
        ``do_on``, l'exercice auquel la résolution fait référence : ``exercise_done`` et la résolution de l'élève : ``resolution``.
        La fonction ``def __str__(self)`` a le même but que pour la table ``Exercise```. Pour ce qui est de la fonction ``def get_lines(self):`` nous permet de retourner une liste avec chaque ligne 
        de la résolution de l'élève. Cette fonction sera utile dans le template ``done.html`` par la suite. 

2. La relation:

  .. figure:: figures/DiagrammeUML.png
    :align: center
    
    *Diagramme UML du modèle relationnel*


C'est deux modèles sont relié entre eux grâce à une ``ForeignKey`` qui est présente dans la table ``Exercise_done``. Cela signifie qu'un exercice peut posséder plusieurs résolution, 
mais qu'une résolution ne fait partie que d'un exercice.

.. raw:: latex

    \pagebreak

3. Le code:

    .. code-block:: python
        :linenos:
    
        from django.db import models
        from django.contrib.auth.models import User
        
        
        class Exercise(models.Model):
            
            owner = models.CharField(max_length=20)  # créateur
            created_on = models.DateTimeField(auto_now_add=True) # date de création
            title = models.CharField(max_length=30) # type d'exerciCe ( choisi
                                                    # dans create.html )
            equation = models.CharField(max_length=50) # Equation de l'exercice
            grade = models.CharField(max_length=60) # difficulté ( entre 1 et 5 )
            correction = models.CharField(max_length = 200) # corrigé de l'exercice
            def __str__(self):
                # recherche plus facile dans http://webmath-thirteenfoil8.c9.io/admin/
                return self.title + " " + self.owner + " " + str(self.pk) 
            
                
        class Exercise_done(models.Model): # Résolutions d'un exercice ( n...1 )
            student = models.CharField(max_length=20) # Etudiant résolvant l'équation
            do_on = models.DateTimeField(auto_now_add=True) # date de résolution
            exercise_done = models.ForeignKey(Exercise) # l'exercice auquel les
                                                        # résolutions seront liées
            resolution = models.CharField(max_length = 200) # la résolution
            
            def __str__(self):
                # recherche plus facile dans http://webmath-thirteenfoil8.c9.io/admin/
                return self.exercise_done.title + " " + self.exercise_done.owner/
                + str(self.exercise_done.pk) + " fait par: " + self.student 
                
            # retourne une liste avec chaque ligne de la résolution.
            def get_lines(self): 
                return self.resolution.split("\n")

4.  Utilisation:

    Pour ce qui est de l'utilisation, lorsque l'on enregistre un formulaire dans la base de données, le code est d'abord écrit grâce au méthode offert par Django, puis, 
    il est traduit en SQL.
    
    En premier lieu, il faut récupérer tous les objets déja existant grâce au code suivant:
    
    .. code-block:: python
    
        Exercise.objects.all()


    Ensuite, pour ce qui est de la création d'exercice, la méthode ``.save()`` de Django sert à enregister un objet et le traduire en SQL. 
    
    .. code-block:: python
        :linenos:
        
        # ici, on utilise un formulaire.
        if request.method == 'POST': 
            title = request.POST['type']
            equation = request.POST['equation']
            grade = request.POST['grade']
            correction = request.POST['correction']
            owner = request.user.username
            Exercise(title=title, owner=owner, equation=equation, grade=grade, \
            correction=correction).save() # On crée l'exercice




--------------------------------------
Les vues
--------------------------------------

Le concept des « vues » est la base de la logique responsable du traitement des requêtes des utilisateurs et le renvoi des réponses vers un template.
Toutes les vues en lien avec cette application se trouve dans ``MainProject/webmath/exercises/views.py``.
Par la suite, deux points seront assez récurrents:

1. L'appel ``@login_required``:
    Cette appel là permet de demander à l'utilisateur d'être connecté pour pouvoir aller sur la page en question.

2. L'appel ``@user_passes_test(is_teacher)``:
    Cette appel est plus strict et sert à préciser que seul un professeur peut se diriger vers la page.
    
Ces deux appels viennent des applications common et permission qui servent à gerer les authentifications et les permissions d'un utilisateur.

Les différents ``import`` à faire ainsi que la vue du template de base ``index.html`` sont les suivants :

.. code-block:: python
    :linenos:
    
    from django.shortcuts import render, HttpResponseRedirect, get_object_or_404,\
    HttpResponse
    from django.core.urlresolvers import reverse
    from exercises.models import *
    import json
    from common.models import Teacher, Student
    from common.auth_utils import *
    from django.contrib.auth.decorators import login_required, user_passes_test
    # Create your views here.
    def index(request):
        return render(request, 'exercises/index.html')
    
    # @login_required demande à l'utilisateur d'être connecté
    # @user_passes_test(is_teacher) restreint l'accès seulement au teachers 

......................................
La vue create
......................................

Pour ce qui est de la vue fonctionnant derrière ``create.html``, la difficulté se trouve surtout dans la sauvegarde des données.

En effet, il faut que chaque données entrées dans les balises du template ``create.html`` puissent être assignées et enregistrer plus tard dans la base de données. Les données seront appliquées à la table ``Exercices``. Ces données seront récupérées plus tard 
dans l'ensemble des vues de l'application.

Le code permettant de faire ça se trouve dans la vue ``create``.

.. code-block:: python
    :linenos:
    
    @login_required
    @user_passes_test(is_teacher)
    def create(request):
        # enregistre les données du formulaire dans la base de données si requête
        # POST sinon, retourne la page
        if request.method == 'POST': 
            title = request.POST['type']
            equation = request.POST['equation']
            grade = request.POST['grade']
            correction = request.POST['correction']
            owner = request.user.username # prendre l'username du user dans 
            #la table User de Django
            Exercise(title=title, owner=owner, equation=equation, grade=grade, \
            correction=correction).save()
            
            return HttpResponseRedirect(reverse("exercises:index"))
        else:
            return render(request, 'exercises/create.html')

Dans cette vue, la difficulté se trouve principalement dans l'enregistrement des données. A la ligne 4, la condition ``if`` permet de différencier si un enregistrement des 
données est nécéssaire et dans le cas contraire, c'est le template ``create.html`` qui sera affiché à l'utilisateur.
Dans le cas où un enregistrement des données est demandé par l'utilisateur, celles-ci sont assignées à différentes variables (``title``, ``equation``, ``grade``, ``correction``, 
``owner``) puis instanciées au modèle ``Exercise`` auquel on applique la fonction ``.save()`` qui sert à enregistrer les données dans la base de données SQL proposée par Django.

......................................
La vue find
......................................

La vue ``find`` utilise la fonction ``objects.all()`` qui permet d'assigner à ``latest_exercise_list`` une liste comportant tous les exercices appartenant à la table ``Exercise`` présents dans la base de données.
La fonction ``return`` retourne ici le template ``find.html`` mais également un dictionnaire possédant la variable ``latest_exercise_list``.

.. code-block:: python
    :linenos:

    @login_required
    def find(request):
        # Assigne les Querysets des objets exercise
        latest_exercise_list = Exercise.objects.all()
        return render(request, 'exercises/find.html', {"exercises_list" : \
        latest_exercise_list})

......................................
La vue resolve
......................................

La vue ``resolve`` permet d'afficher un exercice dans son template ``resolve.html``. La fonction ``get_object_or_404()`` assigne à la variable ``exercise`` toutes les données de l'objet ``n_exercise`` présent dans
la table ``Exercise``. Si celui-là est inexistant, la vue renvoie une erreur *404*. La fonction ``.save()`` est également présente dans ce template et instance la résolutions d'un élève en rapport avec 
l'exercice ``n_exercise`` dans la table ``Exercise_done``. 

Le return de la condition ``if`` permet de renvoyer l'utilisateur sur la page du corrigé de l'exercice ``n_exercise``.

.. code-block:: python
    :linenos:

    @login_required    
    def resolve(request, n_exercise):
        exercise = get_object_or_404(Exercise, id=n_exercise) # Assigne les Querysets
        # des objets exercise, 404 si inexistant
        
        # enregistre les données du formulaire dans la base de données si requête
        # POST sinon, retourne la page 
        if request.method == 'POST' :
            student = request.user.username
            resolution = request.POST['response']
            Exercise_done(exercise_done=exercise, resolution=resolution, \
            student=student).save() # sauvegarde des données dans la db
            
            return HttpResponseRedirect(reverse("exercises:correction", \
            args=[n_exercise]))
        else:
            return render(request, 'exercises/resolve.html', \
            {"exercise" : exercise, "id" : n_exercise})
    



......................................
La vue correction
......................................

L'utilisateur accède au template relatif à cette vue suite à l'envoi de son formulaire dans la vue ``resolve``.

Dans cette vue, on récupère le corrigé de l'exercice ``n_exercise`` dans la table ``Exercise`` puis on affecte cette valeur à la variable correction.
L'utilisateur entre les étapes de la résolution de l'exercice ligne par ligne. Du coup, on utilise la fonction ``split("\n") pour créer une liste contenant chaque ligne 
de la résolution. Cette liste est retournée dans le template grâce à la fonction ``locals()``.

.. code-block:: python
    :linenos:

    def correction(request, n_exercise):
        correction = get_object_or_404(Exercise, id=n_exercise)
        correction_line = correction.correction.split("\n")
        return render(request,'exercises/correction.html', locals())


.....................................
La vue done
.....................................

Cette vue permet à un professeur de voir toutes les résolutions des élèves présentes dans l'exercice ``n_exercise``. La fonction ``objects.filter()`` 
permet d'affecter à la variable ``exercises_done`` les valeurs de l'objet ``n_exercise`` qui se trouvent dans la table ``Exercise_done``. Cette dernière est en 
lien avec l'exercice grâce à une ``ForeignKey``. Du coup, ``exercises_done`` peut contenir plusieurs objets.

.. code-block:: python
    :linenos:

    @login_required
    @user_passes_test(is_teacher)
    def done(request, n_exercise):
        exercise = get_object_or_404(Exercise, id=n_exercise)
        exercises_done = Exercise_done.objects.filter(exercise_done=exercise)
        return render(request, 'exercises/done.html', locals())


......................................
La vue search
......................................

Ceci est la dernière vue de l'application. Son rôle est totalement différent de toutes les autres vues. En effet, cette vue ne retourne aucun template visible par l'utilisateur 
mais elle sert à l' ``input`` ``#search_input`` présent dans le template ``find.html`` de retouner le lien de l'exercice ``exercise.pk``.
Une méthode Ajax est nécessaire pour éviter de faire recharger la page et rendre les recherches plus rapide. 

.. code-block:: python
    :linenos:

    def search(request):
        search_input = request.GET["search"]
        
        exercise = Exercise.objects.get(pk=search_input)
        
        pk = exercise.pk
        url = reverse("exercises:resolve", args=[exercise.pk])
        
        json_dict = {
            "pk" : pk,
            "url" : url,
        }
        
        json_string = json.dumps(json_dict)
        
        return HttpResponse(json_string)



--------------------------------------
Les urls
--------------------------------------



......................................
Les urls de la racine du projet
......................................

Les urls du code suivant servent tout simplement à indiquer les urls de base de l'application. Cela veut dire que suite à l'url http://webmath-thirteenfoil8.c9.io/ [#f11]_ , 
un simple rajout d'un des urls suivants, c'est à dire : ``admin``, ``exercises``, ``common`` ou ``permission``, amenera l'utilisateur directement à la base d'une des applications du projet.
À cela, il faut signaler la présence de la fonction ``include()`` permet à chaque urls présent dans les applications de pouvoir s'ajouter à l'url de base. Les urls de l'application ``exercises``
sont expliqués dans la rubrique suivante.

.. code-block:: python
    :linenos:

    from django.conf.urls import patterns, include, url
    from django.contrib import admin 
    
    urlpatterns = patterns('',
    
        url(r'^admin/', include(admin.site.urls)),
        url(r'^exercises/', include('exercises.urls', namespace='exercises')),
        url(r'^common/', include('common.urls', namespace="common")),
        url(r'^permission/', include('permission.urls', namespace="permission")),
        
    )



......................................
Les urls de l'application exercises
......................................

Tout d'abord, on importe les vues qui seront utilisées dans l'application. Pour cela, on indique dans quel répertoire les vues se trouvent(cf. ligne3). 
Par convention, on nomme les urls d'un application du même nom que son template et de sa vue.
Pour les urls suivants, dès qu'il y a la présence de ``(\d+)/``, cela appelera la vue sur laquelle l'url dirige en utilisant le nombre entré à la suite de 
``/exercices/X`` ( ou X est un des urls situés ci-dessous ) comme valeur de l'argument ``n_exercise``. 
Par exemple, ``/exercices/done/1`` retournera la page des résolutions de l'exercice numéro 1, si l'exercice n'existe pas, la fonction ``get_object_or_404`` 
affichera une page d'erreur.


1. L'``url(r'^$', index, name="index")`` renvoie la page d'accueil du site.

2. L'``url(r'^create/$', create, name="create"),`` renvoie la page de création d'exercices, accessible que par les professeurs.

3. L'``url(r'^find/$', find, name="find"),`` renvoie la page de recherche des exercices.

4. L'``url(r'^done/(\d+)/$', done, name="done"),`` renvoie la page comportant les résolutions des élèves par rapport à un exercice.

5. L'``url(r'^resolve/(\d+)/$', resolve, name="resolve"),`` renvoie la page de résolutions d'un exercice.

6. L'``url(r'^correction/(\d+)/$', correction, name='correction'),`` renvoie la page de correction d'un exercice.

7. L'``url(r'^search/', search, name="search"),`` ne renvoie aucune page visible par l'utilisateur mais sert à afficher les données qui seront récupérées par la requête Ajax pour 
la recherche d'un exercice.




.. code-block:: python
    :linenos:

    from django.conf.urls import patterns, include, url
    from django.contrib import admin
    from exercises.views import index, create, find, resolve, correction, search, done
    
    urlpatterns = patterns('',
        url(r'^$', index, name="index"),
        url(r'^create/$', create, name="create"),
        url(r'^find/$', find, name="find"),
        url(r'^done/(\d+)/$', done, name="done"),
        url(r'^resolve/(\d+)/$', resolve, name="resolve"),
        url(r'^correction/(\d+)/$', correction, name='correction'),
        url(r'^search/', search, name="search"),
    )



--------------------------------------
Les templates
--------------------------------------

Dans les templates de cette application, on utilise les données présentes dans la base de deux manières différentes:

1.  Soit sous forme de boucle ``for``:

    .. code-block:: html
        :linenos:
        
        {% for line in correction_line %}
            <p>$$ {{ line }} $$</p>
        {% endfor %}

2.  Soit sous forme d'appel du champ présent dans les modèles directement sur l'objet d'``Exercise`` ou d'``Exercise_done``.
    Par exemple:
    
        .. code-block:: html
            :linenos:
            
            {{ exercise.equation }}
            {{ exercise.id }}

De plus, au début de chaque template, on doit intégrer la ligne de code ``{% extends "exercises/index.html" %}`` pour permettre au template traîté 
d'avoir le même Frontend que le template ``index.html`` qui est le template de base du site.
    
    

.......................................
Le template de base du site
.......................................


Pour ce qui est de la barre latéral se trouvant à gauche des pages du site, il faut mettre des liens vers les différents templates. Pour cela, on utilise 
une formule Django simple qui permet, si il y a un changement d'url par la suite dans le fichier ``urls.py`` de faire automatiquement le changement 
pour éviter les erreurs de redirection.

Pour ce qui est du Frontend, l'utilisation d'un thème Bootstrap permet de ne pas trop se focaliser sur le design. Pour cette application, Le thème `shop-item <http://startbootstrap.com/template-overviews/shop-item/>`_ [#f12]_
est parfait car il est simple, ergonomique et ne demande que très peu de modifications.


.. code-block:: html
    :linenos:

    <div class="list-group">
        <a href="{% url 'exercises:index' %}" class="list-group-item 
        {% block active-home %}active{% endblock %}">Accueil</a>
        
        <a href="{% url 'exercises:find' %}" class="list-group-item 
        {% block active-reso %}{% endblock %}">Résoudre un exercice</a>
        
        <a href="{% url 'exercises:create' %}" class="list-group-item 
        {% block active-create %}{% endblock %}">Création d'exercice</a>
        
    </div>
    
Les urls de redirection vers les différentes pages du site sont gérés de la manière ci-dessus. On utilise ``<a href="{% url 'exercises:<nom_du_template>' %}"`` 
pour renvoyer l'utilisateur vers les ``templates``. Le bloque {% block active-<home, reso ou create> %}{% endblock %} permet d'activer une classe sur l'onglet actuel. 

........................................
Le template ``create.html``
........................................


Le template ``create.html`` est le template utilisé par les professeurs pour créer l'exercice ainsi que son corrigé. Pour pouvoir enregistrer les données entrées par l'utilisateur,
la présence de la balise ``<form>`` est absolument nécéssaire. Toutes les données entrées sont traîtés dans la vue relative à ce template.


Le ``<button id="voir">`` utilise un script se trouvant sous ``exercises/js/create.js``. Ce script est codé en jQuery et permet d'afficher la deuxième partie du formulaire 
et, grâce à la méthode ``MathJax.Hub.Queue(["Typeset", MathJax.Hub])``, de formater l'équation entrée précédement en la mettant sous une forme mathématique.
Pour ce qui est de la documentation de Mathjax, elle se trouve `ici <https://www.mathjax.org/#docs>`_ [#f13]_ .
 
    

Le voici:

.. code-block:: javascript
    :linenos:

    $(document).ready(function() {
      $( ".corrigé" ).hide(); // cache la div du corrigé qui sera affiché plus tard
      $("#voir").click(function() {
          var $formule = $(".equation").val(); // Récupère la valeur de l'équation
          $(".formule").text("$$" + $formule + "$$"); // La formate en Latex grâce
          //à MathJax
          $(".corrigé").show();
          MathJax.Hub.Queue(["Typeset", MathJax.Hub]); // permet d'afficher l'équation
          //en Latex sans avoir à recharger la page
      });
      $("#submit-resolve").click(function() { 
          if ($("#correction").val() && $("#equation").val()) {
                  $("#create-form").submit(); // renvoie le formulaire si les
                  // tous les champs sont remplis
              }
          else {
              $("#form-warning").modal("show"); // Affiche un message d'erreur si
              // tous les champs ne sont pas rempli
              
          }
      });
    });

Pour ce qui est du deuxième ``button`` présent dans le template, il utilise le code javascript présent depuis la ligne 11. 
En utilisant la condition ``if ($("#correction").val() && $("#equation").val())``,on contrôle que tous les champs du formulaire ont été remplis, sinon, on affiche un message d'erreur.



.........................
Le template ``find.html``
.........................

Le template de cette page se trouve sous le fichier ``static/exercises/templates/find.html``. Ce template comporte tous les exercices déjà présent dans la base de données.

La fonctionnalité permettant la recherche d'un exercice nécessite le code ``html`` suivant :

.. code-block:: html
    :linenos:

    <div>
        <label for="search">Entrez le numéro de l'exercice</label>
        <input type="text" id="search_input" name="search" class="form-control">
        <button type="button" id="search" name="search" class="btn btn-warning">Rechercher
        </button>
    </div>
    <div class="alert alert-info" id="true">
        <strong>Succès!</strong> <span id="lien"></span> de l'exercice en question.
    </div>
    <div class="alert alert-info" id="false">
        <strong>Erreur!</strong> Cet exercice n'existe pas ou n'existe plus,
         veuillez entrez un autre numéro
    </div>
    <div>



    
Grâce au script de cette page se trouvant dans ``static/exercises/js/find.js``, la vue ``search`` analysée auparavant prend tout son sens car ce script utilise les données trouvées par
ajax pour les formater et les mettre en page suite à l'activation du bouton ``<button type="button" id="search" name="search" class="btn btn-warning">Rechercher</button>`` en utilisant le code suivant:

.. code-block:: javascript
    :linenos:

    $(document).ready(function() {
        $('#false').hide(); // Cache les divs #false et #true
        $('#true').hide();
        $("#search").click(function() {
            $("#lien").empty(); // Supprime l'éventuelle ancienne valeur
            var $search = $("#search_input").val(); // enregistre la valeur de
            //la recherche
            $('#false').hide();
            $('#true').hide();
            
            $.ajax({
                url: "/exercises/search/",
                type: "GET",
                dataType: "json",
                data : {
                    search : $search, //récupère les données de la recherche par
                    //rapport à l'exercice recherché ( $search )
                },
                success : function(response) { // Ajoute le lien de l'exercice si
                //il existe et l'affiche à l'utilisateur dans la div #true
                    var $url= response["url"];
                    $('#true').show();
                    $("<a>", {
                    "href": $url,
                    }).text("Voici le lien").appendTo("#lien");
                },
                error : function() { // Affiche le message d'erreur si l'exercice
                //n'existe pas 
                    $("#false").show();
                }
            });
        });
    });

Les commentaires parlent d'eux même. Si l'id de l'exercice existe, on affiche la div :``<div id="true">`` contenant le lien de l'exercice en question sinon, on affiche la 
div : ``<div id="false">`` indiquant que l'exercice n'existe pas.

Pour ce qui est de la mise en page, les ``panel`` de Bootstrap sont très clairs et permette de bien différencié la page de résolution de l'exercice et la page contenant les 
résolutions des élèves. Cette dernière est accessible que par les professeurs.

.. code-block:: html
    :linenos:
    
    <div class="panel panel-success">
        <div class="panel-heading">
            <a href="{% url 'exercises:resolve' exercise.id %}">{{ exercise.title }}:
            {{ exercise.owner }} no{{ exercise.id }} difficulté :{{ exercise.grade }}</a>
        </div>
        <div class="panel-body">
            <a id ="resolve" href="{% url 'exercises:done' exercise.id %}">
            Les résolutions des élèves</a>
        </div>
    </div>

``<div class="panel-heading">`` contient le lien de la page de résolutions et ``<div class="panel-body">`` contient la page contenant les résolutions des élèves.


............................
Le template ``resolve.html`` 
............................

``resolve.html`` permet à un élève de résoudre un exercice. Du coup, un formulaire doit être présent dans le template.
Pour cela, on utilise la balise ``<form>`` à laquelle il faut ajouter la commande ``{% csrf_token %}`` permettant de sécuriser les données qui seront entrées 
par l'utilisateur.

.. code-block:: html
    :linenos:

    <form id="resolve-form" action="{% url 'exercises:resolve' id %}" method="post">
    {% csrf_token %}
        <div>
            <label for="response">Résoudre l'équation</label>
            <textarea type="text" id="response" name="response" class="form-control">
            </textarea>
        </div>
        <button type="button" id="submit-resolve" class="btn btn-sm btn-primary">
        Soumettre et voir le corrigé</button>
        <a class="btn btn-sm btn-primary" href="{% url 'exercises:find' %}">Retour</a>
    </form>

    
Le bouton ``<button type="button" id="submit-resolve" class="btn btn-sm btn-primary">`` renvoie la même fonction javascript que pour le template ``find.html``.
Cela renvoie un message d'erreur si l'utilisateur n'a pas rempli tout le formulaire et envoie les données à la vue ``resolve.html`` si le formulaire est complet.

Le fichier javascript se trouve dans ``static/exercises/js/resolve.js``.

.. code-block:: javascript
    :linenos:
    
    $(document).ready(function() {
      $("#submit-resolve").click(function() {
        // renvoie le formulaire si tous les champs sont remplis
        if ($("#response").val()) {
            $("#resolve-form").submit();
        }
        else {
            // Affiche un message d'erreur si tous les champs ne sont pas remplis
            $("#form-warning").modal("show");
            
        }
      });
    });



.........................
le template ``done.html``
.........................

Le template ``done.html`` utilise la fonction ``get_lines`` présent dans ``models.py`` pour créer une liste contenant toutes les résolutions faites pour un exercice.
Ensuite, on traîte cette liste à l'aide d'une boucle ``for`` pour séparer les résolutions et rendre la page plus claire.
Si l'exercice ne comporte aucune résolution, on affiche le texte suivant : "Aucune résolution effectuée pour cet exercice"

.. code-block:: html
    :linenos:
    
    
    <h2>Voici l'équation de l'exercice no{{ exercise.id }}</h2>
    <h1 class="resolve">$$ {{ exercise.equation }} $$</h1>
    <h2 id="titre">Résolution des élèves</h2>
    {% if exercises_done %}
    {% for exercise in exercises_done %}
        <div class="thumbnail">
            <div class="caption-full">
                <h2>{{ exercise.student }}</h2>
                {% for element in exercise.get_lines %}
                <h2 class="resolve">$$ {{ element }} $$</h2>
                {% endfor %}
                <p id="date">Fait le : {{ exercise.do_on }}</p>
            </div>
        </div>
    {% endfor %}
    {% else %}
    <div class="thumbnail">
        <div class="caption-full">
            <h4 class="resolve">Aucune résolution effectuée pour cet exercice</h4>
        </div>
    </div>
    {% endif %}


.. [#f1] Le lien de la documentation de Python : https://docs.python.org/3/
.. [#f2] Le lien de la documentation d'Html : http://overapi.com/html/
.. [#f3] Le lien de la documentation de CSS : http://overapi.com/css/
.. [#f4] Le lien de la documentation de Javascript : http://overapi.com/javascript/
.. [#f5] Le lien de la documentation de Bootstrap : http://getbootstrap.com/getting-started/
.. [#f6] Le lien de la documentation de jQuery : http://overapi.com/jquery/
.. [#f7] Le lien de la documentation de Django : https://docs.djangoproject.com/en/1.7/
.. [#f8] Le line vers Cloud9 : https://c9.io/
.. [#f9] Le lien de la documentation GitHub: https://github.com/thirteenfoil8/TM-Code-Doc
.. [#f10] Le lien vers la page admin: http://webmath-thirteenfoil8.c9.io/admin/
.. [#f11] Le lien vers la page de base du projet: http://webmath-thirteenfoil8.c9.io/
.. [#f12] Le lien du thème : http://startbootstrap.com/template-overviews/shop-item/
.. [#f13] Le lien de la documentation MathJax : https://www.mathjax.org/#docs