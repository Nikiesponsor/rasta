from django import views
from django.urls import path
from .import  views
from .views import  *

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name="contacts"),
    path('details/<int:int_album>',views.deatilsAlbum,name="details")
]
