from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('Abtus',views.Abtus,name='Abtus'),
    path('Hist',views.Hist,name='Hist'),
    path('Regi',views.Regi,name='Regi'),
    path('video_feed',views.video_feed,name='video_feed'),
]
