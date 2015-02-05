from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    #user = models.ManyToManyField('students.Student')
    
    # ceci veut dire qu'il n'y a forcément qu'un seul prof par exercice. C'est
    # un choix, mais il faudrait alors une option de partage qui permettrait de
    # partager un exercice avec d'autres profs coauteurs
    #owner = models.ForeignKey('teachers.Teacher')
    #collaborateurs = models.ForeignKey('teachers.Teacher')
    
    # éventuellement rajouter un champ "collaborateurs"
    
    #chapter = models.ManyToManyField('teachers.Chapter')
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30)
    donnee = models.CharField(max_length=200)
    equation = models.CharField(max_length=50)
    
    # documenter les champs ==> à quoi servent-ils ???
    grade = models.CharField(max_length=60, blank=True) # donnée une note de difficulté à l'exercice
    
    # essaye de garder une certaine cohérence (anglais / français) ... et cherche
    # le mot anglais (et également singulier / pluriel). Ce champ va stocker UN indice et non plusieurs
    # Ne peut-on pas imaginer plusieurs indices par exercice (il faudrait alors une FK vers une autre table
    # j'appellerais ce champ plutôt "comment"
    comment = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.title
        
# définir une nouvelle table "Hint" (indices) ==> un exo peut avoir plusieures indices.
# Il faudrait pouvoir ordonner les indices pour un certain exercice

class Exercise_done(models.Model):
    do_on = models.DateTimeField(auto_now_add=True)
    exercise_done = models.ForeignKey(Exercise)

class Hint_exo(models.Model):
    exercise = models.ManyToManyField(Exercise)
    hint = models.CharField(max_length= 200)
    
    
        
class Correction(models.Model):
    exercise = models.ForeignKey(Exercise)
    
    # je pense qu'en anglais, on dit plutôt "created_on", "updated_on"
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)