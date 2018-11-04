from django.db import models

# Create your models here.
class Post(models.Model):
    email = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    password = models.TextField()
    confirm_password = models.TextField()
    name = models.TextField() 
    street = models.TextField() 
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    mission = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title