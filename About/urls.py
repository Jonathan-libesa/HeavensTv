from django.urls import path
from.import views
#from.views import 

urlpatterns = [
    path('aboutopen-heavens-ministry',views.aboutpage,name="about"),
    #path('club/<str:pk>/participants/remove',views.removeparticipants,name="remove_follower"),

    ]


