from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from.forms import*
from .models import*
from Users.models import*
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from validate_email import validate_email
from django.contrib.sites.shortcuts import get_current_site
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError,force_text
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
import threading
from django.views import View
from django.db.models import Sum
# Create your views here.

# To MAKE EASIER FOR EMAILING A USER
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
        #self.email.send(fail_silently=False)



def aboutparteneship(request):
	return render(request,'partnership/About_partnership.html')





def registerpage(request):
    form=PartnerSignUpForm()
    if request.method == "POST":
        form=PartnerSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + username)
            user.save()
            return redirect('login')
    context={'form':form}
    return render(request,'partnership/Registration.html',context)


def loginpage(request):
    if request.method == 'POST':
        context = {}
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if not user:
            messages.add_message(request, messages.WARNING,
                                 'Invalid credentials, try again')
            return render(request, 'partnership/Registration.html', context, status=401)

        login(request, user)

        messages.add_message(request, messages.SUCCESS,
                             f'WECLOME TO HEAVENSTV PARTNER  {user.username} ')

        return redirect(reverse('home_partner'))

    return render(request, 'partnership/Registration.html')

#LOGOUT VIEWS
def logoutUser(request):
    logout(request)
    return redirect('/')



@login_required(login_url='login')
def partnerhome(request):
    partner=request.user.partner
    return render(request,'partnership/dashboard.html')


@login_required(login_url='login')
def eventparnter(request):
    events=Event.objects.all()
    context={'events':events}
    return render(request,'partnership/Events.html',context)


@login_required(login_url='login')
def newsparnter(request):
    new=New.objects.all()
    context={'new':new}
    return render(request,'partnership/news.html',context)


#User View Profile
@login_required(login_url='login')
def profile_view_user(request):
    user=request.user
    context={'user':user}
    return render(request, 'partnership/profile_view.html', context)


#UPDATE USER INFORMATION
@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    return render(request, 'partnership/update-user.html', {'form': form})


#RESET PASSWORD 
class RequestPasswordReset(View):
    def get(self,request):
        return render(request,'partnership/password_reset.html')


    def post(self,request):
        email=request.POST['email']

        context ={
        'values':request.POST
        }

        if not validate_email(email):
            messages.error(request,'please supply validate email')
            return render(request,'partnership/password_reset.html',context)

        current_site = get_current_site(request)
        user = User.objects.filter(email=email)
        if user.exists():
            email_contents = { 
                'user': user[0],
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0]),
            }

            link = reverse('reset-user-password',kwargs={
                'uidb64':email_contents['uid'],'token':email_contents['token']
                })

            email_subject = 'Password reset instruction'

            reset_url='http://'+current_site.domain+link

            email= EmailMessage(
                email_subject,
                'Hi there,Please use the link below to reset your password \n' + reset_url,
                'noreply@semycolon.com',
                [email],
            )
            EmailThread(email).start()
        messages.success(request,'We have sent you an email to reset your password')
        return render(request,'partnership/password_reset.html')


class CompletePasswordReset(View):
    def get(self,request,uidb64,token):
        context = {
            'uidb64':uidb64,
            'token':token
        }
        try:
            user_id=force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                messages.info(request,'password link is invalid,please request a new one') 
                return render(request,'partnership/password_reset.html')       
        except Exception as identifer:
            pass
        return render(request,'partnership/new-password.html',context)


    def post(self,request,uidb64,token):
        context = {
            'uidb64':uidb64,
            'token':token
        }
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.warning(request,'password do not match')
            return render(request,'main/new-password.html',context)
        if len(password) < 6:
            messages.warning(request,'password too short')
            return render(request,'partnership/new-password.html',context)
        try:
            user_id=force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            messages.success(request,'password reset successfully,you can login now with new Password')
            return redirect('login') 
        except Exception as identifer:
            messages.info(request,'Something went wrong ,try again')
            return render(request,'partnership/new-password.html',context)


# Contribute for partner
@login_required(login_url='login')
def contribute_view(request):
    my_p=Partner.objects.get(user=request.user)
    contribute=Contribute.objects.filter(partner=my_p)
    contibute_count=Contribute.objects.filter(partner=my_p).aggregate(sum=Sum('amount'))
    total_contribute=contibute_count['sum']
    context={'contribute':contribute,'total_contribute':total_contribute}
    return render(request,'partnership/contribute_view.html',context)
    

@login_required(login_url='login')
def Contribute_make(request):
    my_p=Partner.objects.get(user=request.user)
    contribute=Contribute.objects.filter(partner=my_p)
    if request.method == "POST":
        contribute_form=ContributeForm(request.POST)
        if contribute_form.is_valid():
            contribute=contribute_form.save(commit=False)
            contribute.partner=my_p
            contribute=contribute_form.save()
            return render(request,'partnership/make_contribution.html',{'contribute': contribute})
    else:
        contribute_form=ContributeForm()
        return render(request, 'partnership/form_contribution.html', {'contribute_form':contribute_form})