from django.shortcuts import render

# Create your views here.
def login(req):
    return render(req,'login.html')

def forgetpass(req):
    return render(req,'forgetpass.html')

