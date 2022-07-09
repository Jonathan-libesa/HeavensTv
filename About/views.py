from django.shortcuts import render
from.models import*

# Create your views here.


def aboutpage(request):
	about=About.objects.all()
	context={'about':about}
	return render(request,'about/about_heavens.html',context)

