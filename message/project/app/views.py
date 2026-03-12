from django.shortcuts import render , redirect
from django.contrib import messages

# Create your views here.
def index(req):
    messages.info(req,"Welcom to my page")
    messages.error(req,"Error")
    messages.success(req,"Successfull")
    messages.debug(req,"Debugging")
    messages.warning(req,"Heat protect")
    return redirect("home")

def home(req):
    return render(req,"home.html")

    