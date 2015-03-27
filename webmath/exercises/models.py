from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    
    owner = models.CharField(max_length=20)  # créateur
    created_on = models.DateTimeField(auto_now_add=True) # date de création
    title = models.CharField(max_length=30) # type d'exercice ( choisi dans create.html )
    equation = models.CharField(max_length=50) # Equation de l'exercice
    grade = models.CharField(max_length=60) # difficulté ( entre 1 et 5 )
    correction = models.CharField(max_length = 200) # corrigé de l'exercice
    def __str__(self):
        return self.title + " " + self.owner + " " + str(self.pk) # recherche plus facile dans http://webmath-thirteenfoil8.c9.io/admin/
        
class Exercise_done(models.Model): # Résolutions d'un exercice ( n...1 )
    student = models.CharField(max_length=20) # Etudiant résolvant l'équation
    do_on = models.DateTimeField(auto_now_add=True) # date de résolution
    exercise_done = models.ForeignKey(Exercise) # l'exercice auquel les résolutions seront liées
    resolution = models.CharField(max_length = 200) # la résolution
    
    def __str__(self):
        return self.exercise_done.title + " " + self.exercise_done.owner + str(self.exercise_done.pk) + " fait par: " + self.student # recherche plus facile dans http://webmath-thirteenfoil8.c9.io/admin/
        
    def get_lines(self): # retourne une liste avec chaque ligne de la résolution.
        return self.resolution.split("\n")