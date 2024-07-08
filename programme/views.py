from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    album=Album.objects.all()
    single=Single.objects.all()
    return render(request,'home.html',{'albums':album,'singles':single})
def contact(request):
    return render(request,'contact.html')

def deatilsAlbum(request,int_album):
    details=Album.objects.get(pk=int_album)
    return render(request,"details.html",{'details':details})

