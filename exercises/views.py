from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from exercises.models import *
# Create your views here.
def index(request):
    return render(request, 'exercises/index.html')

def create(request):
    if request.method == 'POST': # sauvegarde des données dans la db
        title = request.POST['title']
        donnee = request.POST['donnee']
        equation = request.POST['equation']
        
        Exercise(title=title, donnee=donnee, equation=equation).save()
        
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
    return render(request, 'exercises/resolve.html', {"exercise" : exercise})