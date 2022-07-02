from django.shortcuts import render
from.models import*
from About.models import* 
#from Prayer.models import*
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail
import threading
from django.contrib.messages import constants as messages

# Create your views here.

# To MAKE EASIER FOR EMAILING A USER
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
        #self.email.send(fail_silently=False)

        
def homeview(request):
	pages=Page.objects.all()
	about=About.objects.all()
	youtube=Youtube.objects.all().order_by('-created_on')[0:3]
	if request.method == "POST":
		name=request.POST['name']
		country=request.POST['country']
		email=request.POST['email']
		phone=request.POST['phone']
		message=request.POST['message']

		data={
			'name':name,
			'country':country,
			'email':email,
			'phone':phone,
			'message':message
		}
		message='''
		New Message:{}

		from:{}
		'''.format(data['name'],data['message'],data['phone'])
		send_mail(data['name'],message,phone,'',['jonathanlibesa@gmail.com'])
		message.SUCCESS(request,'We have recieved your email our team will respond to you soon')
		return render(request,'main/home.html')
	else:
		context={'pages':pages,'about':about,'youtube':youtube}	
		return render(request,'main/home.html',context)
	


def contact(request):
	return render(request,'main/contact.html')

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}