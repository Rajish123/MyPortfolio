from django.shortcuts import render
from .models import Contact, Project, CurriculumVitae
from django.http import FileResponse

# Create your views here.

def home(request):
    context = {}
    projects = Project.objects.all().order_by("-created").values()[:3]
    all_projects = Project.objects.all().order_by("-created").values()[3:]
    context = {'project':projects, 'all_projects':all_projects}
    return render(request,'portfolio/index.html',context)

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

def CV(request):
    get_cv = CurriculumVitae.objects.first()
    return FileResponse(get_cv.cv.open(),as_attachment= True, filename = "RajishCV.pdf")