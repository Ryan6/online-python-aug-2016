from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'Survey/index.html')

def results(request):
	request.session['yourName'] = request.POST['yourName']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return render(request, 'Survey/results.html')