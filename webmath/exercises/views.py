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

@login_required
def create(request):
    if request.method == 'POST': # sauvegarde des données dans la db
        title = request.POST['type']
        equation = request.POST['equation']
        grade = request.POST['grade']
        correction = request.POST['correction']
        owner = request.POST['owner']
        Exercise(title=title, owner=owner, equation=equation, grade=grade, correction=correction).save()
        
        return HttpResponseRedirect(reverse("exercises:index"))
    else:
        return render(request, 'exercises/create.html')

    
@login_required
def find(request):
    latest_exercise_list = Exercise.objects.all()
    return render(request, 'exercises/find.html', {"exercises_list" : latest_exercise_list})
    
def resolve(request, n_exercise):
    exercise = get_object_or_404(Exercise, id=n_exercise)
    if request.method == 'POST' :
        student = request.POST['student']
        equation = request.POST['response']
        Exercise_done(exercise_done=exercise, equation=equation, student=student).save()
        
        return HttpResponseRedirect(reverse("exercises:correction", args=[n_exercise]))
    else:
        return render(request, 'exercises/resolve.html', {"exercise" : exercise, "id" : n_exercise})

def done(request, n_exercise):
    exercise = get_object_or_404(Exercise, id=n_exercise)
    exercise_done_line = exercise.equation.split("\n")
    exercise_done_list = Exercise.objects.all()
    return render(request, 'exercises/done.html', locals())

def correction(request, n_exercise):
    correction = get_object_or_404(Exercise, id=n_exercise)
    correction_line = correction.correction.split("\n")
    return render(request,'exercises/correction.html', locals())
    
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