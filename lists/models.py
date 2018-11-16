from django.db import models

# Create your models here.
class Institutions(models.Model):
    pass

#Institutions
class Item(models.Model):
    #id_inst = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    email = models.TextField()
    password = models.TextField()
    confirm_password = models.TextField()
    name = models.TextField() 
    street = models.TextField() 
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    mission = models.TextField()
    list = models.ForeignKey(Institutions, default=None)
        
#programEducationalObjectives
class ProgramEducationalObjectives(models.Model):
    institution = models.ForeignKey(Item, default=None)
    objective = models.TextField()
    
    def __str__(self):
        return self.objective

#Student outcomes
class StudentOutcome(models.Model):
    institution = models.ForeignKey(Item, default=None)
    studentOutcome = models.TextField()


    