from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from exercises.models import *
# Create your views here.
def index(request):
    return render(request, 'exercises/index.html')

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

def base(request):
    return render(request, 'exercises/base.html')

def find(request):
    latest_exercise_list = Exercise.objects.all()
    return render(request, 'exercises/find.html', {"exercises_list" : latest_exercise_list})
    
def resolve(request, n_exercise):
    exercise = get_object_or_404(Exercise, id=n_exercise)
    if request.method == 'POST' :
        student = request.POST['student']
        equation = request.POST['response']
        Exercise_done(exercise_done=exercise, equation= response, student=student)
        
        return HttpResponseRedirect(reverse("exercises:correction id"))
    else:
        return render(request, 'exercises/resolve.html', {"exercise" : exercise, "id" : n_exercise})

def correction(request, n_exercise):
    correction = get_object_or_404(Exercise, id=n_exercise)
    correction_line = correction.correction.split("\n")
    return render(request,'exercises/correction.html', locals())