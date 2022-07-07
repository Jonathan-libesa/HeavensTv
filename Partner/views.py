from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from.forms import*
from .models import*
from Users.models import*
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def aboutparteneship(request):
	return render(request,'partnership/About_partnership.html')

#def donate(request):
   # return render(request,'partnership/donate.html')


# TO ADD NEWS AND ANNOUNCENTS INFORMATION

def donate(request):
    donate=Donate.objects.all()
    if request.method == "POST":
        donate_form=DonateForm(request.POST)
        if donate_form.is_valid():
            donate=donate_form.save()
            return render(request,'partnership/payment.html',{'donate': donate})
    else:
        donate_form=DonateForm()
        return render(request, 'partnership/donate.html', {'donate_form': donate_form})
#STUDENT REGISTRATION TO LOGIN


def charge(request,pk):
    donate=get_object_or_404(Donate,id=pk)
    return render(request, 'partnership/payment.html', {'donate': donate})


def Register(request):
    form=PartnerSignUpForm()
    if request.method == "POST":
        form=PartnerSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            first_name=form.cleaned_data.get('first_name')
            messages.success(request,'Account was created for ' + first_name)
            user.save()
            messages.success(request,'We sent you an email to verify your account')
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
            return render(request,'partnership/login.html' , context)

        login(request, user)

        messages.add_message(request, messages.SUCCESS,
                             f'Welcome  {user.username} ')

        return redirect(reverse('admin-dashboard'))

    return render(request,'partnership/login.html')


#LOGOUT VIEWS
def logoutUser(request):
    logout(request)
    return redirect('/')