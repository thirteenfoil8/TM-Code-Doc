from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    #user = models.ManyToManyField('students.Student')
    
    # ceci veut dire qu'il n'y a forcément qu'un seul prof par exercice. C'est
    # un choix, mais il faudrait alors une option de partage qui permettrait de
    # partager un exercice avec d'autres profs coauteurs
    
    # éventuellement rajouter un champ "collaborateurs"
    
    # documenter les champs ==> à quoi servent-ils ???
    owner = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30)
    equation = models.CharField(max_length=50)
    grade = models.CharField(max_length=60) # donnée une note de difficulté à l'exercice
    correction = models.CharField(max_length = 200)
    def __str__(self):
        return self.title
        
# définir une nouvelle table "Hint" (indices) ==> un exo peut avoir plusieures indices.
# Il faudrait pouvoir ordonner les indices pour un certain exercice

class Exercise_done(models.Model):
    student = models.CharField(max_length=20)
    do_on = models.DateTimeField(auto_now_add=True)
    exercise_done = models.OneToOneField(Exercise)
    equation = models.CharField(max_length = 200)

class Exercise_type(models.Model):
    pass
    