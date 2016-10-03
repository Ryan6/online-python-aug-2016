from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
	context ={
	'courses' : Course.objects.all()
	}
	return render(request, 'CoursesApp/index.html', context)

def courses(request):
	Course.objects.create(name=request.POST['courseName'], description=request.POST['courseDescription'])
	return redirect('/')

def destroy(request, id):
	if request.method == 'POST':
		Course.objects.filter(id=id).delete()
		return redirect('/')

	context ={
	'courses' : Course.objects.filter(id=id)
	}
	return render(request, 'CoursesApp/destroy.html', context)