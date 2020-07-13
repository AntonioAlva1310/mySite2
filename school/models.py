from django.db import models

# Create your models here.
class Clasroom(models.Model):
    subject_of_study = models.CharField(max_length=75)
    beginning_date = models.DateTimeField('date published')

    def __str__(self):
        return self.subject_of_study

class Student(models.Model):
    clasroom = models.ForeignKey(Clasroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    

    def __str__(self):
        return self.name