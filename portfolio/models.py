from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    concern = models.TextField(max_length = 250)
    
    def __str__(self):
        return self.name
    
    