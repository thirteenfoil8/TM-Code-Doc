####################################
Documentation du développeur
####################################

Cette partie de la documentation est essentiellement destinée au développeur qui aimerait comprendre comment cette application fonctionne.
Il est a noté que le projet contenant l'entier des fichiers est sur un `dépôt <https://github.com/thirteenfoil8/TM-Code-Doc>`_ [#f1]_ GitHub.

Tout ce qui concerne les modèles, les vues, les urls, les templates, ... est affiché ci-dessous. Le code est accompagné de quelques annotations mais celles-ci sont là 
que pour donner quelques précisions quant à celui-ci. Il est donc nécéssaire de connaître les languages de programmation et les frameworks suivant pour comprendre la documentation 
développeur: 

* Les languages de programmation:

  * `Python <https://docs.python.org/3/>`_ [#f2]_
  
  * `Html  <http://overapi.com/html/>`_ [#f3]_ 
  
  * `Css  <http://overapi.com/css/>`_ [#f4]_
  
  * `Javascript  <http://overapi.com/javascript/>`_ [#f5]_
    
* Les FrameWorks:

  * `Bootstrap  <http://getbootstrap.com/getting-started/>`_ [#f6]_ 
  
  * `jQuery  <http://overapi.com/jquery/>`_ [#f7]_ 
  
  * `Django  <https://docs.djangoproject.com/en/1.7/>`_ [#f8]_ 
  
  


.. raw:: latex

    \pagebreak



--------------------------------------
Les modèles
--------------------------------------

1. Les modèles de cette application sont les suivants:
    * ``Exercise``
        
        Ce modèle contient les informations relatives à un exercice en particulier. Il contient le nom du créateur : ``owner``, la date de création : ``created_on``, 
        le titre de l'exercice : ``title`` ( celui-ci ne possède que 4 choix présents dans le template ``create.html`` présent plus bas dans la documentation ), 
        l'équation que l'élève devra traîter : ``equation``, la difficulté de l'exercice : ``grade`` ( choisi entre 1 et 5 également dans ``create.html`` ), 
        et enfin la correction de l'exercice : ``correction``.
        La fonction ``def __str__(self)`` sert uniquement à rendre quelque chose de plus propre sur la [#f8]_ `page <http://webmath-thirteenfoil8.c9.io/admin/>`_ prévue pour les admins du site.
    
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
            
            owner = models.CharField(max_length=20)  
            created_on = models.DateTimeField(auto_now_add=True)
            title = models.CharField(max_length=30)
            equation = models.CharField(max_length=50)
            grade = models.CharField(max_length=60) 
            correction = models.CharField(max_length = 200)
            def __str__(self):
                return self.title + " " + self.owner + " " + str(self.pk)
                
        class Exercise_done(models.Model):
            student = models.CharField(max_length=20)
            do_on = models.DateTimeField(auto_now_add=True)
            exercise_done = models.ForeignKey(Exercise)
            resolution = models.CharField(max_length = 200)
            
            def __str__(self):
                return self.exercise_done.title + " " + self.exercise_done.owner + str(self.exercise_done.pk) + " fait par: " + self.student
                
            def get_lines(self):
                return self.resolution.split("\n")

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
        if request.method == 'POST': # sauvegarde des données dans la db
            title = request.POST['type']
            equation = request.POST['equation']
            grade = request.POST['grade']
            correction = request.POST['correction']
            owner = request.user.username
            Exercise(title=title, owner=owner, equation=equation, grade=grade, correction=correction).save()
            
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
        latest_exercise_list = Exercise.objects.all()
        return render(request, 'exercises/find.html', {"exercises_list" : latest_exercise_list})

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
        exercise = get_object_or_404(Exercise, id=n_exercise)
        if request.method == 'POST' :
            student = request.user.username
            resolution = request.POST['response']
            Exercise_done(exercise_done=exercise, resolution=resolution, student=student).save()
            
            return HttpResponseRedirect(reverse("exercises:correction", args=[n_exercise]))
        else:
            return render(request, 'exercises/resolve.html', {"exercise" : exercise, "id" : n_exercise})
    



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


.. code-block:: python
    :linenos:

    from django.conf.urls import patterns, include, url
    from django.contrib import admin
    from exercises.views import index, create, base, find, resolve, correction, search, done
    
    urlpatterns = patterns('',
        url(r'^$', index, name="index"),
        url(r'^create/$', create, name="create"),
        url(r'^base/$', base, name="base"),
        url(r'^find/$', find, name="find"),
        url(r'^done/(\d+)/$', done, name="done"),
        url(r'^resolve/(\d+)/$', resolve, name="resolve"),
        url(r'^correction/(\d+)/$', correction, name='correction'),
        url(r'^search/', search, name="search"),
    )



--------------------------------------
Les templates
--------------------------------------

.......................................
Le template de base du site
.......................................


Pour ce qui est du Frontend, le thème bootstrap ``shop-item`` est un thème simple nécéssitant que très peu de modifications. Il se trouve [#f10]_ `ici <http://startbootstrap.com/template-overviews/shop-item/>`_ .

Le code du template de base est le suivant:

.. code-block:: html
    :linenos:
    
    {% load staticfiles %}
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
    
        <title>{% block title %}Accueil{% endblock %}</title>
    
        <!-- Custom CSS -->
        <link href="{% static 'exercises/css/shop-item.css' %}" rel="stylesheet">
        <script src="https://code.jquery.com/jquery-1.11.0.min.js"></script>
        <script src="https://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
        <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css" >
        <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js"></script>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
        
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="{% static 'exercises/css/style.css' %}">
        
        {% block head %}{% endblock %}
    
        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
    
    </head>
    
    <body>
    
        <!-- Navigation -->
        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Webmath</a>
                </div>
                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li>
                            <a href="#">Cours</a>
                        </li>
                        <li>
                            <a href="{% url 'exercises:index' %}">Exercices</a>
                        </li>
                        <li>
                            <a href="http://quiztm-2014-2-blm08.c9.io/quiz/create/">Quiz</a>
                        </li>
                    </ul>
                </div>
                <!-- /.navbar-collapse -->
            </div>
            <!-- /.container -->
        </nav>
    
        <!-- Page Content -->
        <div class="container">
    
            <div class="row">
    
                <div class="col-md-3">
                    <p class="lead">Exercices</p>
                    <div class="list-group">
                        <a href="{% url 'exercises:index' %}" class="list-group-item {% block active-home %}active{% endblock %}">Accueil</a>
                        <a href="{% url 'exercises:find' %}" class="list-group-item {% block active-reso %}{% endblock %}">Rechercher un exercice</a>
                        <a href="{% url 'exercises:create' %}" class="list-group-item {% block active-create %}{% endblock %}">Création d'exercice</a>
                    </div>
                </div>
    
                {% block content %}
                <div class="col-md-9">
    
                    <div class="thumbnail">
                        <div class="caption-full">
                            <h1>Bienvenue!</h1>
                            <p>Bienvenue sur la page de l'application des exercices de Webmath. Cliquez sur un des onglets selon la fonctionnalité que vous voulez utiliser.</p>
                        </div>
                    </div>
                </div>
                {% endblock %}
    
            </div>
    
        </div>
    </body>
    
    </html>

Pour ce qui est de la barre latéral se trouvant à gauche des pages du site, il faut mettre des liens vers les différents template. Ceci se fait non pas en recopiant le lien
de la page web directement mais en utilisant une formule Django simple qui permet, si il y a un changement d'url par la suite dans le fichier ``urls.py`` de faire automatiquement le changement 
pour éviter les erreurs de redirection.

le code est le suivant :

.. code-block:: html
    :linenos:

    <div class="list-group">
        <a href="{% url 'exercises:index' %}" class="list-group-item {% block active-home %}
        active{% endblock %}">Accueil</a>
        <a href="{% url 'exercises:find' %}" class="list-group-item {% block active-reso %}
        {% endblock %}">Résoudre un exercice</a>
        <a href="{% url 'exercises:create' %}" class="list-group-item {% block active-create %}
        {% endblock %}">Création d'exercice</a>
    </div>
    
On constate qu'un block ``{% block active %}`` a été ajouté à chaque lien. Celui-ci permet d'activer la classe ``list-group-item`` dans la page actuel.


........................................
Le template create.html
........................................


Le template ``create.html`` est le template utilisé par les professeurs pour créer l'exercice ainsi que son corrigé. Pour pouvoir enregistrer les données entrées par l'utilisateur,
la présence de la balise ``<form>`` est absolument nécéssaire. Toutes les données entrées sont traîtés dans la vue relative à ce template.

Voici le template ``exercises/templates/create.html``.

.. code-block:: html
    :linenos:

    {% extends "exercises/index.html" %}
    {% load staticfiles %}
    
    {% block head %}<script type='text/javascript' src="{% static 'exercises/js/create.js' %}"></script>{% endblock %}
    {% block title %}Création d'exercice{% endblock %}
    
    {% block active-home %}{% endblock %}
    {% block active-create %}active{% endblock %}
    {% block content %}
    <form action="{% url 'exercises:create' %}" method="post">{% csrf_token %}
        <div class="col-md-9">
            <div class="thumbnail">
                <div class="caption-full">
                    <h1>Création d'exercice</h1>
                        <div>
                            <label for="title">Type d'exercice</label>
                            <SELECT name="type" id='type' class="form-control">
                		        <OPTION VALUE="Factorisation du 1er degré">Factorisation du 1er degré</OPTION>
                		        <OPTION VALUE="Factorisation du 2eme degré">Factorisation du 2eme degré</OPTION>
                		        <OPTION VALUE="Développement du 1er degré">Développement du 1er degré</OPTION>
                		        <OPTION VALUE="Développement du 2eme degré">Développement du 2eme degré</OPTION>
                	        </SELECT>
            	        </div>
                        <div>
                            <label for="equation">Equation à résoudre</label>
                            <input type="text" name="equation" class="form-control equation">
                        </div>
                        <div>
                            <label for="grade">Difficulté</label>
                        	<SELECT name="grade" class="form-control">
            	                <OPTION VALUE="1">1</OPTION>
            	                <OPTION VALUE="2">2</OPTION>
                        		<OPTION VALUE="3">3</OPTION>
                        		<OPTION VALUE="4">4</OPTION>
                        		<OPTION VALUE="5">5</OPTION>
                        	</SELECT>
                        </div>
                            <button type="button" id="voir" class="btn btn-sm btn-primary">Faire le corrigé</button>
                        </div>
                    
                </div>
            </div>
        </div>
        <div class="col-md-offset-3 col-md-9">
            <div class="thumbnail corrigé">
                <div class="caption-full">
                    <h1>Création de son corrigé</h1>
                    <p class="formule"></p>
                    <div>
                        <label for="correction"><br>Développement du corrigé</label>
                        <textarea id="correction" class="form-control" name="correction"></textarea>
                    </div>
                    <input type="submit" class="btn btn-sm btn-primary">
                </div>
            </div>
        </div>
    </form>
    {% endblock %}



Le ``<button id="voir">`` utilise un script se trouvant sous ``exercises/js/create.js``. Ce script est codé en jQuery et permet d'afficher la deuxième partie du formulaire 
et, grâce à la méthode ``MathJax.Hub.Queue(["Typeset", MathJax.Hub])``, de formater l'équation entrée précédement en la mettant sous une forme mathématique.
Pour ce qui est de la documentation de Mathjax, elle se trouve [#f11]_ `ici <https://www.mathjax.org/#docs>`_ .
 
    

Le voici:

.. code-block:: javascript
    :linenos:

    $(document).ready(function() {
        $( ".corrigé" ).hide();
        $("#voir").click(function() {
            var $formule = $(".equation").val();
            $(".formule").text("$$" + $formule + "$$");
            $(".corrigé").show();
            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        });
    });



.........................
Le template find.html
.........................

Le template de cette page se trouve sous le fichier ``static/exercises/templates/find.html``. Ce template comporte tous les exercices déjà présent dans la base de donnée.

Voici le template:

.. code-block:: html
    :linenos:

    {% extends "exercises/index.html" %}
    {% load staticfiles %}
    {% block title %}Résolution d'exercice{% endblock %}
    {% block active-home %}{% endblock %}
    {% block active-reso %}active{% endblock %}
    {% block head %}<script type='text/javascript' src="{% static 'exercises/js/find.js' %}"></script>
    <link rel="stylesheet" type="text/css" href="{% static 'exercises/css/find.css' %}"/>
    {% endblock %}
    {% block content %}
    <div class="col-md-9">
        <div class="thumbnail">
            <div class="caption-full">
                <h1>Rechercher un exercice</h1>
                <div>
                    <label for="search">Entrez le numéro de l'exercice</label>
                    <input type="text" id="search_input" name="search" class="form-control">
                    <button type="button" id="search" name="search" class="btn btn-warning">Rechercher</button>
                </div>
                <div class="alert alert-info" id="true">
                    <strong>Succès!</strong> <span id="lien"></span> de l'exercice en question.
                </div>
                <div class="alert alert-info" id="false">
                    <strong>Erreur!</strong> Cet exercice n'existe pas ou n'existe plus, veuillez entrez un autre numéro
                </div>
                <div>
                    {% for exercise in exercises_list %}
                    <div class="panel panel-success">
                        <div class="panel-heading">
                            <a href="{% url 'exercises:resolve' exercise.id %}">{{ exercise.title }}: {{ exercise.owner }} no{{ exercise.id }} difficulté :{{ exercise.grade }}</a>
                        </div>
                        <div class="panel-body">
                            <a id ="resolve" href="{% url 'exercises:done' exercise.id %}">Les résolutions des élèves</a>
                        </div>
                    </div>
                    {% endfor %}
                </div>
    
            </div>
        </div>
    </div>
    {% endblock %}

    
Grâce au script de cette page se trouvant dans ``static/exercises/js/find.js``, la vue ``search`` analysée auparavant prend tout son sens car ce script utilise les données trouvées par
ajax pour les formater et les mettre en page en utilisant le code suivant:

.. code-block :: javascript
    :linenos:

    $(document).ready(function() {
        $('#false').hide();
        $('#true').hide();
        $("#search").click(function() {
            $("#lien").empty();
            var search = $("#search_input").val();
            $('#false').hide();
            $('#true').hide();
            
            $.ajax({
                url: "/exercises/search/",
                type: "GET",
                dataType: "json",
                data : {
                    search : search,
                },
                success : function(response) {
                    var $url= response["url"];
                    $('#true').show();
                    $("<a>", {
                    "href": $url,
                    }).text("Voici le lien").appendTo("#lien");
                },
                error : function() {
                    $("#false").show();
                }
            });
        });
    });


...........................
Le template resolve.html 
...........................



.. code-block:: html
    :linenos:

    {% extends "exercises/index.html" %}
    {% load staticfiles %}
    {% block head %}<script type='text/javascript' src="{% static 'exercises/js/resolve.js' %}"></script>{% endblock %}
    {% block title %}Résolution d'exercice{% endblock %}
    {% block active-home %}{% endblock %}
    {% block active-reso %}active{% endblock %}
    {% block content %}
    <div class="col-md-9">
        <div class="thumbnail">
            <div class="caption-full">
                <h1 id="title">{{ exercise.title }}</h1>
                <div class="thumbnail">
                    <p id ="donnee">{{ exercise.donnee }}</p>
                    <p>$$ {{ exercise.equation }} $$</p>
                    <h6>crée le :{{ exercise.created_on  }}</h6>
                    <form id="resolve-form" action="{% url 'exercises:resolve' id %}" method="post">{% csrf_token %}
                        <div>
                            <label for="response">Résoudre l'équation</label>
                            <textarea type="text" id="response" name="response" class="form-control"></textarea>
                        </div>
                        <button type="button" id="submit-resolve" class="btn btn-sm btn-primary">Soumettre et voir le corrigé</button>
                        <a class="btn btn-sm btn-primary" href="{% url 'exercises:find' %}">Retour</a>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <div class="modal fade" id="form-warning">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title">Erreur</h4>
                </div>
                <div class="modal-body">
                    <p>Vous devez remplir tous les champs pour soumettre votre réponse</p>
                </div>
                <div class="modal-footer">
                    <a type="button" class="btn btn-success" data-dismiss="modal">Ok</a>
                </div>
            </div>
        </div>
    </div>
    {% endblock %}

............................
le template correction.html
............................

.. code-block:: html
    :linenos:

    {% extends "exercises/index.html" %}
    {% load staticfiles %}
    {% block title %}Correction{% endblock %}
    {% block active-home %}{% endblock %}
    {% block active-reso %}active{% endblock %}
    {% block content %}
    <div class="col-md-9">
        <div class="thumbnail">
            <div class="caption-full">
                <h1>Corrigé de l'exercice</h1>
                {% for line in correction_line %}
                    <p>$$ {{ line }} $$</p>
                {% endfor %}
                <a class="btn btn-sm btn-primary" href="{% url 'exercises:find' %}">Retour</a>
            </div>
        </div>
    </div>
    {% endblock %}


.........................
le template done.html
.........................


.. code-block:: html
    :linenos:
    
    {% extends "exercises/index.html" %}
    {% load staticfiles %}
    {% block title %}Exercice fait par les élèves{% endblock %}
    {% block active-home %}{% endblock %}
    {% block active-reso %}active{% endblock %}
    {% block head %}
    <link rel="stylesheet" type="text/css" href="{% static 'exercises/css/done.css' %}"/>
    {% endblock %}
    {% block content %}
    <div class="col-md-9">
        <div class="thumbnail">
            <div class="caption-full">
                <div>
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
                </div>
                    <a class="btn btn-sm btn-primary" href="{% url 'exercises:find' %}">Retour</a>
                </div>
            </div>
        </div>
    </div>
    {% endblock %}


.. rubric::
.. [#f1] Le lien de la documentation GitHub: https://github.com/thirteenfoil8/TM-Code-Doc
.. [#f2] Le lien de la documentation de Python : https://docs.python.org/3/
.. [#f3] Le lien de la documentation d'Html : http://overapi.com/html/
.. [#f4] Le lien de la documentation de CSS : http://overapi.com/css/
.. [#f5] Le lien de la documentation de Javascript : http://overapi.com/javascript/
.. [#f6] Le lien de la documentation de Bootstrap : http://getbootstrap.com/getting-started/
.. [#f7] Le lien de la documentation de jQuery : http://overapi.com/jquery/
.. [#f8] Le lien de la documentation de Django : https://docs.djangoproject.com/en/1.7/
.. [#f9] Le lien vers la page admin: http://webmath-thirteenfoil8.c9.io/admin/
.. [#f10] Le lien du thème : http://startbootstrap.com/template-overviews/shop-item/
.. [#f11] Le lien de la documentation MathJax : https://www.mathjax.org/#docs