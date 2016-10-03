from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
	}
	return render(request, 'DisappearingNinjas/index.html', context)

def ninjas(request, color):
	context = {
		"color": color,
	}
	return render(request, 'DisappearingNinjas/ninjas.html', context)