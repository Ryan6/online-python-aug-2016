from django.shortcuts import render, redirect
import re
import bcrypt
from .models import User

NAME_REGEX = re.compile(r'^[a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
	if 'action' not in request.session:
		request.session['action'] = ''
	if 'error' not in request.session:
		request.session['error'] = ''
	# {{error}} in index.html > session['error'] instead of printing errors > errors show up on index

	if 'hashed' not in request.session:
		request.session['hashed'] = ''
	if 'name' not in request.session:
		request.session['name'] = ''
	
	return render(request, 'LoginRegistration/index.html')

def register(request):

	# check for errors in form
	if not NAME_REGEX.match(request.POST['first_name']) and len(request.POST['first_name']) >= 2:
		print 'first name problem'
		return redirect('/')
	if not NAME_REGEX.match(request.POST['last_name']) and len(request.POST['last_name']) >= 2:
		print 'last name problem'
		return redirect('/')
	if not EMAIL_REGEX.match(request.POST['email_register']):
		print 'email problem'
		return redirect('/')
	if not len(request.POST['pwd_register']) >= 8:
		print 'pwd register problem'
		return redirect('/')
	if not request.POST['pwd_confirm'] == request.POST['pwd_register']:
		print 'pwd match problem'
		return redirect('/')
	#### check if email already in db

	# generate hashed password
	password = request.POST['pwd_register'].encode('UTF_8')
	request.session['hashed'] = bcrypt.hashpw(password, bcrypt.gensalt())

	# create user
	User.objects.create(
		first_name	= request.POST['first_name'].capitalize(),
		last_name	= request.POST['last_name'].capitalize(),
		email		= request.POST['email_register'],
		hashed_pwd	= request.session['hashed'],
		)

	request.session['name'] = request.POST['first_name'].capitalize()
	request.session['action'] = 'registered.'

	return redirect('/success')

def login(request):
	# check for errors in form
	if not User.objects.filter(email=request.POST['email_login']):
		print 'EMAIL NOT HERE'
		return redirect('/')

	current_user = User.objects.get(email=request.POST['email_login'])

	# check password match
	if not bcrypt.hashpw(request.POST['pwd_login'].encode('UTF_8'), current_user.hashed_pwd.encode('UTF_8')) == current_user.hashed_pwd:
		print 'pwds do not match'
		return redirect('/')

	request.session['name'] = current_user.first_name.capitalize()
	request.session['action'] = 'logged in.'

	return redirect('/success')

def success(request):
	context = {
		'userName': request.session['name'],
		'action': request.session['action'],
		'users': User.objects.all()
	}
	return render(request, 'LoginRegistration/success.html', context)