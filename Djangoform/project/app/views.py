from django.shortcuts import render , redirect
from .forms import StudentForm

# Create your views here.
def landing(request):
    return render(request, 'landing.html')


# def register(req):
#     if req.method=="POST":
#             X=StudentForm(req.POST)
#             # print(X)
#             if X.is_valid():
#                  print( X.cleaned_data)
#                  X.save()
#                  return redirect('landing')
#     xyz = StudentForm()
#     return render(req, 'register.html', {'frm': xyz })


def register(req):
    if req.method == "POST":
        X = StudentForm(req.POST)
        if X.is_valid():
            print("hii")
            print(X.cleaned_data)
            X.save()
            return redirect('landing')
    
    else:
        X = StudentForm()

    return render(req, 'register.html', {'frm': X})

