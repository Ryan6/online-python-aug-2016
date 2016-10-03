from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def home(request):
	if 'activities_text' in request.session:
		pass
	else:
		request.session['activities_text'] = ''
	if 'gold' in request.session:
		pass
	else:
		request.session['gold'] = 0

	context = {
		'gold': request.session['gold'],
		'activities_text': request.session['activities_text'],
	}
	return render(request, 'NinjaGold/index.html', context)

def process_money(request, methods=['POST']):
	if request.POST['building']=='farm':
		temp = random.randrange(10,21)
		request.session['gold'] += temp
	if request.POST['building']=='cave':
		temp = random.randrange(5,11)
		request.session['gold'] += temp
	if request.POST['building']=='house':
		temp = random.randrange(2,6)
		request.session['gold'] += temp
	if request.POST['building']=='casino':
		temp = random.randrange(-50,51)
		request.session['gold'] += temp
		if temp > 0:
			request.session['activities_text'] += '\nWon ' + str(temp) + ' gold at the casino!'
			return redirect('/')
		if temp < 0:
			request.session['activities_text'] += '\nLost ' + str(abs(temp)) + ' gold at the casino... Ouch.'
			return redirect('/')
		if temp == 0:
			request.session['activities_text'] += '\nBroke even at the casino.'
			return redirect('/')
	request.session['activities_text'] += '\nEarned ' + str(temp) + ' gold at the ' + request.POST['building']

	return redirect('/')

def reset(request):
	request.session['gold'] = 0
	request.session['activities_text'] = 'Your gold was reset.'
	return redirect('/')