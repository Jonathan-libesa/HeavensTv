from django.urls import path
from.import views

urlpatterns = [
    path('Teaching_view',views.preaching,name="preach_view"),
    ] 