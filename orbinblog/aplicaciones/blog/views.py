from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home(request):
    posts=Post.objects.filter(estado=True)
    return render(request, "index.html", {'posts':posts})

def detallePost(request, slug):
    post=Post.objects.get(slug=slug)
    return render(request,'post.html', {'detalle_post':post})    

def post(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Post'))
    return render(request, "post.html", {'posts':posts})

def contacto(request):
    if request.method=="POST":
        
        subject=request.POST["name"]
        message=request.POST["email"] + " " + request.POST["subject"] + " " + request.POST["message"]
        
        
        
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["serviceasamblea99@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        
        return render(request, "index.html")

    return render(request, "index.html")


 



