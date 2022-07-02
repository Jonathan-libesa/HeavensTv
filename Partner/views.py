from django.shortcuts import render

# Create your views here.


def aboutparteneship(request):
	return render(request,'partnership/About_partnership.html')