from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")

def aboutus(request):
    return render(request,"aboutus.html")

def kitchen(request):
    return render(request,"kitchen.html" )

def engeneering(request):
    return render(request,"engeneering.html" )

def spa(request):
    return render(request,"spa.html" )

def contact(request):
    return render(request,"contact.html" )


def send_email(request): 
    subject = str(request.POST["subject_1"])
    name= str(request.POST["name1"])
    email = str(request.POST["email_id1"])
    mmsg = str(request.POST["msg"])
    mess = f"Name: {name}\nEmail: {email}\n\nMessage: {mmsg}"
    recipient_list = ['kirankumarr1901@gmail.com'] # List of recipient email addresses
    
    send_mail(subject, mess, str(request.POST["email_id1"]), recipient_list,fail_silently=False)
    messages.success(request,'The Message Send. Please Wait We Will Get to You in a Short While')
    return redirect("contact" )

def furniture(request):
    return render(request,"furniture.html")

def veg(request):
    return render(request,"veg.html" )