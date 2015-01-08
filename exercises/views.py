from django.shortcuts import render, HttpResponseRedirect
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
