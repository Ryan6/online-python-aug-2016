from django.shortcuts import render, HttpResponse
import datetime as dt
# Create your views here.
def index(request):
	context = {
		"date": dt.date.today(),
		"time": dt.datetime.strftime(dt.datetime.now(), "%I:%M %p UTC")
	}
	return render(request, 'timedisplay/page.html', context)