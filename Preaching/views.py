from django.shortcuts import render
from.models import*
# Create your views here.



def preaching(request):
	preach=Preaching.objects.all().order_by('-created_on')
	context={'preach':preach}
	return render(request,'main/preach_view.html',context)