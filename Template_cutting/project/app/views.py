from django.shortcuts import render , redirect

# Create your views here.
def landing(req):
    return render (req , 'landing.html')


def about(req):
    return render (req , 'about.html')

def register(req):
    return render (req , 'register.html')


def contact(req):
    return render (req , 'contact.html')
