from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    concern = models.TextField(max_length = 250)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length = 50)
    language = models.CharField(max_length = 255)
    description = models.TextField(max_length = 255,blank=True,null=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    image= models.ImageField(upload_to = "ProjectImage/",default = "default.jpeg")
    url = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.title
    
class CurriculumVitae(models.Model):
    cv = models.FileField(upload_to = "CV")
    
    