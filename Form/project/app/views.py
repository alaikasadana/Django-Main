from django.shortcuts import render
from.models import student
def index(req):
    return render(req,'index.html')

def formdata(req):
    n=req.POST.get('name')
    e=req.POST.get('email')
    t1=req.POST.get('tell')
    t2=req.POST.get('tell2')
    q=req.POST.getlist('quali')
    s=req.POST.get('state')
    g=req.POST.get('gender')
    i=req.FILES.get('image')
    d=req.FILES.get('document')
    a = req.FILES.get('audio')
    v = req.FILES.get('video')


    print(n,g,e,t1,t2,q,s,i,d,a,v)
    student.objects.create(name=n,email=e,contact=t1,qualification=q,state=s,gender=g,image=i,document=d,audio=a,video=v)


    # print(n,e,t1,t2,q,sep=',')
    # print(type(n),type(e),type(t1),type(t2),sep=',')
# Create your views here.