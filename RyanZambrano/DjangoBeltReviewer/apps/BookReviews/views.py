from django.shortcuts import render, redirect
import re
import bcrypt
from .models import User, Book, Review

NAME_REGEX = re.compile(r'^[a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
	if 'current_user' not in request.session:
		request.session['current_user'] = ''
	if 'error' not in request.session:
		request.session['current_user'] = ''

	return render(request, 'BookReviews/index.html')

def register(request):
	# check for errors in form
	if not len(request.POST['name']) >= 2:
		request.session['error'] = 'Name must be at least TWO characters long'
		return redirect('/')
	if not NAME_REGEX.match(request.POST['name']):
		request.session['error'] = 'Name can only include letters'
		return redirect('/')
	if not EMAIL_REGEX.match(request.POST['email_register']):
		request.session['error'] = 'Please enter a valid email'
		return redirect('/')
	if not len(request.POST['pwd_register']) >= 8:
		request.session['error'] = 'Password must be at least 8 characters'
		return redirect('/')
	if not request.POST['pwd_confirm'] == request.POST['pwd_register']:
		request.session['error'] = 'Passwords must match'
		return redirect('/')
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# TO-DO #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# > check if username or email already in use
	# >	error : must use different username or email

	# generate hashed password
	password = request.POST['pwd_register'].encode('UTF_8')
	request.session['hashed'] = bcrypt.hashpw(password, bcrypt.gensalt())

	# create user
	User.objects.create(
		name		= request.POST['name'].capitalize(),
		username	= request.POST['username'],
		email		= request.POST['email_register'],
		hashed_pwd	= request.session['hashed'],
		)

	request.session['current_user'] = request.POST['username']

	return render(request, 'BookReviews/books.html')



def login(request):
	# check for errors in form
	if not User.objects.filter(email=request.POST['email_login']):
		request.session['error'] = 'There are no accounts associated with this email address.'
		return redirect('/')

	current_user = User.objects.get(email=request.POST['email_login'])

	# check password match
	if not bcrypt.hashpw(request.POST['pwd_login'].encode('UTF_8'), current_user.hashed_pwd.encode('UTF_8')) == current_user.hashed_pwd:
		request.session['error'] = 'Incorrect Password.'
		request.session['current_user'] = ''
		current_user = ''
		return redirect('/')
	
	request.session['current_user'] = current_user.username
	
	return render(request, 'BookReviews/books.html')


def books(request):
	all_books = Book.objects.all() 
	recents = []
	if len(all_books) > 3:
		for book in all_books:
			if book.id in range(len(all_books)-2,len(all_books)+1):
				recents.append(book)
	else:
		for book in all_books:
			recents.append(book)

	context = {
		'books': all_books,
		'recents': recents
	}

	if request.session['current_user'] == '':
		request.session['error'] = 'Please log in'
		return redirect('/')
	return render(request, 'BookReviews/books.html', context)

def reviews(request, id):
	book = Book.objects.get(id=id)
	reviews = Review.objects.filter(book=book)

	context = {
	'title': book.title,
	'author': book.author,
	'reviews': reviews
	}

	return render(request, 'BookReviews/reviews.html', context)

def add(request):
	return render(request, 'BookReviews/add.html')

def process_add(request):
	if not len(request.POST['booktitle']) > 0:
		return redirect('/books/add')
	if not len(request.POST['newauthor']) > 0:
		pass # choose from the dropdown
	if not len(request.POST['review']) > 0:
		return redirect('/books/add')
	
	# if book already there
	for book in list(Book.objects.filter(title=request.POST['booktitle'])):
		if request.POST['booktitle'] == book.title:
			Review.objects.create(
				score	= request.POST['rating'],
				text 	= request.POST['review'],
				user	= User.objects.get(username=request.session['current_user']),
				### make sure newauthor / oldauthor
				book 	= Book.objects.get(title=request.POST['booktitle']),
			)
			book_id = Book.objects.get(title=request.POST['booktitle']).id
			return redirect('/books/%s' % book_id)

	# if book not already there
	Book.objects.create(
		title	= request.POST['booktitle'],
		author	= request.POST['newauthor'],
	)
	Review.objects.create(
		score	= request.POST['rating'],
		text 	= request.POST['review'],
		user	= User.objects.get(username=request.session['current_user']),
		### make sure newauthor / oldauthor
		book 	= Book.objects.get(title=request.POST['booktitle']),
	)


	book_id = Book.objects.get(title=request.POST['booktitle']).id
	return redirect('/books/%s' % book_id)

def user(request):
	return render(request, 'BookReviews/books/user.html')

def logout(request):
	request.session['current_user'] = ''
	request.session['error'] = ''
	return redirect('/')