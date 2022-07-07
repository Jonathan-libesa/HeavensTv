from django.urls import path
from.import views

urlpatterns = [
    path('about_partenership',views.aboutparteneship,name="partenship"),
    path('Signup_partners',views.Register,name="Register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('donate_view/',views.donate,name="give"),
    
 ] 