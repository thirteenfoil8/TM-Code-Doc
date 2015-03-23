from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    
    owner = models.CharField(max_length=20)  
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30)
    equation = models.CharField(max_length=50)
    grade = models.CharField(max_length=60) 
    correction = models.CharField(max_length = 200)
    def __str__(self):
        return self.title + " " + self.owner + " " + str(self.pk)
        
class Exercise_done(models.Model):
    student = models.CharField(max_length=20)
    do_on = models.DateTimeField(auto_now_add=True)
    exercise_done = models.ForeignKey(Exercise)
    resolution = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.exercise_done.title + " " + self.exercise_done.owner + str(self.exercise_done.pk) + " fait par: " + self.student
        
    def get_lines(self):
        return self.resolution.split("\n")