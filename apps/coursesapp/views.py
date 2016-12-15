from django.shortcuts import render, redirect
from .models import Course

def index(request):
    courses = Course.objects.all()
    context = {
        "courses" : courses
    }
    print courses.query
    return render(request, "coursesapp/index.html", context)

def process(request):
    course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def delete(request, id):
    courses = Course.objects.get(id=id)
    context = {'courses': courses}
    return render(request, "coursesapp/delete.html", context)

def destroy(request, id):
    instance = Course.objects.get(id=id)
    instance.delete()
    return redirect("/")


# Create your views here.
