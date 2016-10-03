from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
	if 'number' not in request.session:
		request.session['number'] = 0	
	return render(request,'randomword/index.html')

def randomNumber(request):
	print request.method
	if request.method == "POST":
		print request.POST
		request.session['number'] += 1
		request.session['random'] = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for x in range(14))
		return redirect('/')
	else:
		return redirect('/')