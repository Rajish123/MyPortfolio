from django.contrib import admin
from .models import Contact, Project, CurriculumVitae

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','concern']
    
@admin.register(Project)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title','language','description','image']
    
@admin.register(CurriculumVitae)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['cv',]