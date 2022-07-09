from django.urls import path
from.import views
from.views import CompletePasswordReset,RequestPasswordReset
urlpatterns = [
    path('about_partenership',views.aboutparteneship,name="partenship"),
    path('Signup_partners',views.registerpage,name="Register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('my/',views.partnerhome,name="home_partner"),
    path('event_view/',views.eventparnter,name="event"),
    path('news_view/',views.newsparnter,name="news"),
    path('profile_view_user', views.profile_view_user, name="user_profile"),
    path('update-user-view', views.updateUser, name="update-user"),
    path('request-password-reset-link',RequestPasswordReset.as_view(),name="request-password"),
    path('set-new-password/<uidb64>/<token>',CompletePasswordReset.as_view(), name='reset-user-password'),
    path('contribution_view',views.contribute_view,name="contribute_view"),
    path('make_contribution',views.Contribute_make,name="form_contribute")
    
    #path('donate/<str:pk>',views.charge,name="donate")
    
 ] 