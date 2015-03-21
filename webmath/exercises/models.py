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
    resolution = models.CharField(max_length = 200) # Sa résolution
    
    def __str__(self):
        return self.exercise_done.title + " " + self.exercise_done.owner + str(self.exercise_done.pk) + " fait par: " + self.student