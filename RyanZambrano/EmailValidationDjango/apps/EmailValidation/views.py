from django.shortcuts import render, redirect
import re
from .models import Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
	if 'message' not in request.session:
		request.session['message'] = 'hello'
	
	context = {
		'message': request.session['message']
	}
	
	print request.session['message']
	return render(request, 'EmailValidation/index.html', context)

def success(request):
	context = {
		'emails': Email.objects.all(),
	}
	if request.method == 'POST':
		if EMAIL_REGEX.match(request.POST['UserEmail']):
			print "Email is valid"
			Email.objects.create(email=request.POST['UserEmail'])
		else:
			print "Email is not valid"
			request.session['message'] = 'Please enter a valid email.'
			return redirect('/')
	print Email.objects.all()

	return render(request, 'EmailValidation/success.html', context)
