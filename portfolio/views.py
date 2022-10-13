from django.shortcuts import render
from .models import Contact

# Create your views here.

def home(request):
    return render(request,'portfolio/home.html')

def about(request):
    return render(request,'portfolio/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        concern = request.POST['concern']
        obj = Contact(name=name,phone=phone,email=email,concern=concern)
        obj.save()
    return render(request,'portfolio/contact.html')
 