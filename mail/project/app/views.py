from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse



# Create your views here.
def signup(req):
    return render(req,'signup.html')


def djangomail(req):
    if req.method =="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        contact=req.POST.get('contact')
        query=req.POST.get('query')
        print(name,email,contact,query)

        send_mail(
        "testing django mail",
        f"mail from django server {email}, {name}, {contact}, {query}",
         email,
        ["alaikasadana8817@gmail.com"],
        fail_silently=False,
    )
        return HttpResponse("MAIL DONE")