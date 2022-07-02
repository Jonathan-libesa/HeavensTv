from django.shortcuts import render
from Main.models import*
# Create your views here.

def video_testmony(request):
	testmonies=Youtube.objects.all().order_by('-created_on')
	context={'testmonies':testmonies}
	return render(request,'Testmony/testimonies_view.html',context)
