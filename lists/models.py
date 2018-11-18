from django.db import models

# Create your models here.
class Institutions(models.Model):
    pass

#Institutions
class Item(models.Model):
    #id_inst = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    email = models.TextField(default='')
    password = models.TextField(default='')
    confirm_password = models.TextField(default='')
    name = models.TextField(default='') 
    street = models.TextField(default='') 
    city = models.TextField(default='')
    state = models.TextField(default='')
    zipcode = models.TextField(default='')
    mission = models.TextField(default='')
    list = models.ForeignKey(Institutions, default=None)
        
#programEducationalObjectives
class ProgramEducationalObjectives(models.Model):
    institution = models.ForeignKey(Item, default=None)
    objective = models.TextField(default='')
    
    def __str__(self):
        return self.objective

#Student outcomes
class StudentOutcome(models.Model):
    institution = models.ForeignKey(Item, default=None)
    studentOutcome = models.TextField(default='' )


    