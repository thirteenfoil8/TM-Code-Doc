from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
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

@login_required
@user_passes_test(is_teacher)
def create(request):
    # enregistre les données du formulaire dans la base de données si requête POST sinon, retourne la page
    if request.method == 'POST': 
        title = request.POST['type']
        equation = request.POST['equation']
        grade = request.POST['grade']
        correction = request.POST['correction']
        owner = request.user.username # prendre l'username du user dans la table User de Django
        Exercise(title=title, owner=owner, equation=equation, grade=grade, correction=correction).save()
        
        return HttpResponseRedirect(reverse("exercises:index"))
    else:
        return render(request, 'exercises/create.html')
    
@login_required
def find(request):
    latest_exercise_list = Exercise.objects.all() # Assigne les Querysets des objets exercise
    return render(request, 'exercises/find.html', {"exercises_list" : latest_exercise_list})

@login_required    
def resolve(request, n_exercise):
    exercise = get_object_or_404(Exercise, id=n_exercise) # Assigne les Querysets des objets exercise, 404 si inexistant
    # enregistre les données du formulaire dans la base de données si requête POST sinon, retourne la page 
    if request.method == 'POST' :
        student = request.user.username
        resolution = request.POST['response']
        Exercise_done(exercise_done=exercise, resolution=resolution, student=student).save() # sauvegarde des données dans la db
        
        return HttpResponseRedirect(reverse("exercises:correction", args=[n_exercise]))
    else:
        return render(request, 'exercises/resolve.html', {"exercise" : exercise, "id" : n_exercise})


@login_required
@user_passes_test(is_teacher)
def done(request, n_exercise):
    exercise = get_object_or_404(Exercise, id=n_exercise)
    exercises_done = Exercise_done.objects.filter(exercise_done=exercise) # Crée une liste avec les resolutions d'un exercice
    return render(request, 'exercises/done.html', locals())


def correction(request, n_exercise):
    correction = get_object_or_404(Exercise, id=n_exercise)
    correction_line = correction.correction.split("\n") # crée une liste avec chaque ligne de la correction
    return render(request,'exercises/correction.html', locals())
    
def search(request):
    # Retourne une page html invisible pour l'utilisateur mais permettant de faire une recherche sans avoir à
    # recharger la page.
    search_input = request.GET["search"]
    
    exercise = Exercise.objects.get(pk=search_input)
    
    pk = exercise.pk
    url = reverse("exercises:resolve", args=[exercise.pk])
    
    # ce dictionnaire est utilisé dans /static/js/find.js pour retourner le lien de l'exercice recherché à l'utilisateur
    json_dict = {
        "pk" : pk,
        "url" : url,
    }
    
    json_string = json.dumps(json_dict)
    
    return HttpResponse(json_string)