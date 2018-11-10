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
class programEducationalObjectives(models.Model):
    #institution = models.ForeignKey(Inst, default=None)
    institution = models.TextField()
    objective = models.TextField()

#Student outcomes
class studentOutcome(models.Model):
    #institution = models.ForeignKey(Inst, default=None)
    institution = models.TextField()
    sttudentOutcome = models.TextField()