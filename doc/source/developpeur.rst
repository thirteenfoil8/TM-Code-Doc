####################################
Documentation du développeur
####################################

Cette partie de la documentation est essentiellement destinée au développeur qui aimerait comprendre comment cette application fonctionne.

Tout ce qui concerne les modèles, les vues, les urls, les templates, ... est affiché ci-dessous. Le code est accompagné de quelques annotations mais celles-ci sont là 
que pour donner quelques précisions quant à celui-ci. Il est donc nécéssaire de connaître les languages de programmation et les FrameWorks suivant pour comprendre la documentation 
développeur: 

* Les languages de programmation:

    * [#f1]_ `Python <https://docs.python.org/3/>`_ 
    
    * [#f2]_ `Html  <http://overapi.com/html/>`_ 
    
    * [#f3]_ `Css  <http://overapi.com/css/>`_ 
    
    * [#f4]_ `Javascript  <http://overapi.com/javascript/>`_ 
    
* Les FrameWorks:

    * [#f5]_ `Bootstrap  <http://getbootstrap.com/getting-started/>`_ 
    
    * [#f6]_ `jQuery  <http://overapi.com/jquery/>`_ 
    
    * [#f7]_ `Django  <https://docs.djangoproject.com/en/1.7/>`_ 
    

--------------------------------------
Les modèles
--------------------------------------


Les modèles de l'application Exercice ne sont pas très nombreux. Ils servent surtout à la création et à la résolution des exercices. ( A compléter)

.. code-block:: python

    from django.db import models
    from django.contrib.auth.models import User
    
    
    class Exercise(models.Model):
        
        owner = models.CharField(max_length=20)  # créateur de l'exercice   
        created_on = models.DateTimeField(auto_now_add=True) # Date de création
        updated_on = models.DateTimeField(auto_now=True)
        title = models.CharField(max_length=30) # C'est le titre de l'exercice ( factorisation ou développement)
        equation = models.CharField(max_length=50) # C'est l'équation entrée par le professeur
        grade = models.CharField(max_length=60) # donnée une note de difficulté à l'exercice
        correction = models.CharField(max_length = 200) # Ceci est le corrigé de l'exercice ( obligatoire )
        def __str__(self):
            return self.title + " " + self.owner + " " + str(self.pk)
            
    class Exercise_done(models.Model):
        student = models.CharField(max_length=20)  # L'élève aillant résolu l'exercice
        do_on = models.DateTimeField(auto_now_add=True) # La date à laquelle il l'a fait
        exercise_done = models.ForeignKey(Exercise) # L'exercice en question qu'il a résolu
        equation = models.CharField(max_length = 200) # Sa résolution
        
        def __str__(self):
            return self.exercise_done.title + " " + self.exercise_done.owner + str(self.exercise_done.pk) + " fait par: " + self.student

--------------------------------------
Les vues
--------------------------------------

......................................
La vue create
......................................

Pour ce qui est du code fonctionnant derrière cette partie de l'application, la difficulté se trouve surtout dans la sauvegarde des données.

En effet, il faut que pour chaques données entrées dans les balises Html permettant d'entrer les valeurs du type, de l'équation et la difficulté puissent être enregistrer dans une variable et les enregistrer
dans la base de donnée dans la table ``Exercices``. Le code permettant de faire ça se trouve dans le fichier ``views.py`` dans la vue ``create``.

.. code-block:: python
    
    @login_required
    def create(request):
    if request.method == 'POST': # sauvegarde des données dans la db
        title = request.POST['title']
        donnee = request.POST['donnee']
        equation = request.POST['equation']
        
        Exercise(title=title, donnee=donnee, equation=equation).save()
        
        return HttpResponseRedirect(reverse("exercises:index"))
    else:
        return render(request, 'exercises/create.html')
        

......................................
La vue find
......................................

.. code-block:: python

    @login_required
    def find(request):
        latest_exercise_list = Exercise.objects.all()
        return render(request, 'exercises/find.html', {"exercises_list" : latest_exercise_list})

......................................
La vue resolve
......................................

La vue resolve se trouvant dans le fichier ``views.py`` est la vue qui permet d'afficher un exercice dans son template ``resolve.html`` et si il n'y a pas d'exercice suite à l'url entré par l'utilisateur,
elle renvoit une erreur 404. Grâce à celle-ci, chaque exercice à sa propre page.

Le code de cette vue est assez rudimentaire mais l'import ainsi que l'utilisation de ``get_object_or_404`` est à noter.

.. code-block:: python

    def resolve(request, n_exercise):
    exercise = get_object_or_404(Exercise, id=n_exercise)
    if request.method == 'POST' :
        student = request.POST['student']
        equation = request.POST['response']
        Exercise_done(exercise_done=exercise, equation=equation, student=student).save()
        
        return HttpResponseRedirect(reverse("exercises:correction", args=[n_exercise]))
    else:
        return render(request, 'exercises/resolve.html', {"exercise" : exercise, "id" : n_exercise})
    



......................................
La vue correction
......................................


.. code-block:: python

    def correction(request, n_exercise):
        correction = get_object_or_404(Exercise, id=n_exercise)
        correction_line = correction.correction.split("\n")
        return render(request,'exercises/correction.html', locals())


.....................................
La vue done
.....................................


.. code-block:: python

    def done(request, n_exercise):
        exercise = get_object_or_404(Exercise, id=n_exercise)
        exercise_done_line = exercise.equation.split("\n")
        exercise_done_list = Exercise.objects.all()
        return render(request, 'exercises/done.html', locals())


......................................
La vue search
......................................



.. code-block:: python

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


Pour ce qui est du Frontend, le thème bootstrap ``shop-item`` est un thème simple nécéssitant que très peu de modifications. Il se trouve [#f8]_ `ici <http://startbootstrap.com/template-overviews/shop-item/>`_ .

Pour ce qui est de la barre latéral se trouvant à gauche des pages du site, il faut mettre des liens vers les différents template. Ceci se fait non pas en recopiant le lien
de la page web directement mais en utilisant une formule Django simple qui permet, si il y a un changement d'url par la suite dans le fichier ``urls.py`` de faire automatiquement le changement 
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
    
On constate qu'un block ``{% block active %}`` a été ajouté à chaque lien. Celui-ci permet d'activer la classe ``list-group-item`` dans la page actuel.


........................................
Le template create.html
........................................


Le template ``create.html`` est le template utilisé par les professeurs pour créer l'exercice ainsi que son corrigé. Pour pouvoir enregistrer les données entrées par l'utilisateur,
la présence de la balise ``<form>`` est absolument nécéssaire. Toutes les données entrées sont traîtés dans la vue relative à ce template.

Voici le template ``exercises/templates/create.html``.

.. code-block:: html

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
                            <label for="owner">Nom du professeur</label>
                            <input type="text" name="owner" class="form-control">
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
Pour ce qui est de la documentation de Mathjax, elle se trouve [#f9]_ `ici <https://www.mathjax.org/#docs>`_ .
 
    

Le voici:

.. code-block:: javascript

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
                <ul><h4>La difficulté croît de 1 à 5</h4>
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
                        <li><a href="{% url 'exercises:resolve' exercise.id %}">{{ exercise.title }}: {{ exercise.owner }} no{{ exercise.id }} difficulté :{{ exercise.grade }}</a></li>
                    {% endfor %}
                </div>
                </ul>
            </div>
        </div>
    </div>
    {% endblock %}

    
Grâce au script de cette page se trouvant dans ``static/exercises/js/find.js``, la vue ``search`` analysée auparavant prend tout son sens car ce script utilise les données trouvées par
ajax pour les formater et les mettre en page en utilisant le code suivant:

.. code-block :: javascript

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
                            <label for="student">Nom de l'élève</label>
                            <input id="student" type="text" name="student" class="form-control">
                        </div>
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

.......................
le template correction.html
.......................

.. code-block:: html

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




.. rubric::

.. [#f1] Le lien de la documentation de Python : https://docs.python.org/3/
.. [#f2] Le lien de la documentation d'Html : http://overapi.com/html/
.. [#f3] Le lien de la documentation de CSS : http://overapi.com/css/
.. [#f4] Le lien de la documentation de Javascript : http://overapi.com/javascript/
.. [#f5] Le lien de la documentation de Bootstrap : http://getbootstrap.com/getting-started/
.. [#f6] Le lien de la documentation de jQuery : http://overapi.com/jquery/
.. [#f7] Le lien de la documentation de Django : https://docs.djangoproject.com/en/1.7/
.. [#f8] Le lien du thème : http://startbootstrap.com/template-overviews/shop-item/
.. [#f9] Le lien de la documentation MathJax : https://www.mathjax.org/#docs