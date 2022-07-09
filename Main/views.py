from django.shortcuts import render
from.models import*
from About.models import* 
#from Prayer.models import*
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail
import threading
from django.contrib import messages
from Partner.forms import*
from Partner.models import*

# Create your views here.

# TO ADD NEWS AND ANNOUNCENTS INFORMATION

def donate(request):
    donate=Donate.objects.all()
    if request.method == "POST":
        donate_form=DonateForm(request.POST)
        if donate_form.is_valid():
            donate=donate_form.save()
            return render(request,'main/payment.html',{'donate': donate})
    else:
        donate_form=DonateForm()
        return render(request, 'main/donate.html', {'donate_form': donate_form})

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
		'''.format(data['name'],data['message'])
		send_mail(data['name'],message,'',['jonathanlibesa@gmail.com'])
		messages.success(request,'We have recieved your email we will pray for you')
		return render(request,'main/home.html')
	else:
		context={'pages':pages,'about':about,'youtube':youtube}	
		return render(request,'main/home.html',context)
	


def contact(request):
	if request.method == "POST":
		name= request.POST['name']
		subject= request.POST['subject']
		email= request.POST['email']
		message= request.POST['message']

		data= {
			'name':name,
			'subject':subject,
			'email':email,
			'message':message
		}


		message= '''
		New message:{}

		from:{}
		'''.format(data['message'],data['email'])
		send_mail(data['subject'],message,'',['jonathanlibesa@gmail.com'])	
		messages.success(request,'We have recieved your email our team will respond to you soon')
		return render(request,'main/contact.html')
	else:
		return render(request,'main/contact.html')

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

def con(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phn = request.POST.get('phn')
        desc = request.POST.get('desc')
        cont = Contact(name=name,email=email,phn=phn,desc= desc,date=datetime.today())
        cont.save()
        messages.success(request, 'Your mesaage has been sent')
    return render(request, 'contact.html')