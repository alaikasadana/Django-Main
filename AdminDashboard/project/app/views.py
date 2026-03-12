from django.shortcuts import render, redirect
from .models import Student, dep,emp


# ---------------- HOME / STATIC PAGES ----------------
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


# ---------------- LOGIN ----------------
def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(e,p)
        if e == 'admin@gmail.com' and p == 'admin123':
            req.session['admin_email'] = e
            req.session['admin_password'] = p
            req.session['admin_name'] = 'admin'
            return redirect('dashboard')
        
        user = Student.objects.filter(email=e)
        if user:
            userdata = Student.objects.get(email = e)
            if p == userdata.password_1:
                id = userdata.id
                req.session['user_id']=id
                name = userdata.name
                req.session['user_name']=name
                email = userdata.email
                req.session['user_email']=email
                return redirect('dashboard')
            else:
                req.session['y']="Email and password not match"
                return redirect('login')
        else:
            req.session['x']="Email Not Register"
            return redirect('register')
    y = req.session.get('y','')    
    return render(req,'login.html',{'y':y})

def dashboard(req):
    if 'admin_email' in req.session and 'admin_password' in req.session:
        a_email = req.session['admin_email']
        a_password = req.session['admin_password']
        a_name= req.session['admin_name']
        a_data = {
            "name" : a_name,
            "email" : a_email,
            "password" : a_password,

        }
        return render(req,'admin_dashboard.html',{'data':a_data})
    
    if 'user_id' in req.session:
        id = req.session['user_id']
        userdata = Student.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password_1
        }
        return render(req,'dashboard.html',{'data':data})
    else:
        return redirect('login')




# ---------------- LOGOUT ----------------
def logout(request):
    request.session.flush()
    return redirect('login')



def save_department(req):
    if req.method=='POST':
          dname=req.POST.get('dept_name')
          dcode=req.POST.get('dept_code')
          dhead=req.POST.get('dept_head')
          dbudget=req.POST.get('dept_budget')
          ddesc=req.POST.get('dept_desc')
          deptdata=dep.objects.filter(dept_name=dname)
          if not deptdata:
            dep.objects.create(dept_name=dname,dept_code=dcode,dept_head=dhead,dept_budget=dbudget,dept_desc=ddesc)
            return redirect("add_department")
          else:
            return redirect('add_department')
     
    return redirect('login')

    
def add_department(req):
    if 'admin_email' in req.session and 'admin_password' in req.session:
          a_data = {
            'email': req.session['admin_email'],
            'password': req.session['admin_password'],
            'name': req.session['admin_name']
        }
          return render(req,'admin_dashboard.html', {'data': a_data,"add_department":True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})
    
# def add_employees(req):
#     if 'admin_email' in req.session and 'admin_password' in req.session:
#           a_data = {
#             'email': req.session['admin_email'],
#             'password': req.session['admin_password'],
#             'name': req.session['admin_name']
#         }
#           return render(req,'admin_dashboard.html', {'data': a_data,"add_employees":True})
#     else:
#         msg={'msg':'login first'}
#         return render(req,"login.html",{'msg':msg})

def all_department(req):
    if 'admin_email' in req.session and 'admin_password' in req.session:
          a_data = {
            'email': req.session['admin_email'],
            'password': req.session['admin_password'],
            'name': req.session['admin_name']
        }
          return render(req,'admin_dashboard.html', {'data': a_data,"":True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

def add_employees(req):
      if 'admin_email' in req.session and 'admin_password' in req.session:
          a_data = {
            'email': req.session['admin_email'],
            'password': req.session['admin_password'],
            'name': req.session['admin_name']
        }
      if req.method=='POST':
           fname=req.POST.get('fname')
           lname=req.POST.get('lname')
           email=req.POST.get('email')
           img=req.FILES.get('img')
           adhaar=req.FILES.get('adhaar')
           code=req.POST.get('code')
           mobile=req.POST.get('mobile')
           DOB=req.POST.get('DOB')
           gender=req.POST.get('gender')
           edu=req.POST.getlist('edu')
           dept=req.POST.get('dept')
           emp.objects.create(fname=fname,lname=lname,email=email,img=img,adhaar=adhaar,code=code,mobile=mobile,DOB=DOB,gender=gender,edu=edu,dept=dept)
           return render(req,'admin_dashboard.html')
      else:
           return redirect('login')
      

def save_emp(req):
       if 'admin_email' in req.session and 'admin_password' in req.session:
            a_data = {
                 'email': req.session['admin_email'],
                 'password': req.session['admin_password'],
                 'name': req.session['admin_name']
              }
            if req.method=='POST':
               print(req.POST)
     





# def register(req):

#     if req.method == "POST":
#         n = req.POST.get('name')
#         e = req.POST.get('email')
#         c = req.POST.get('contact')
#         p1 = req.POST.get('password_1')
#         p2 = req.POST.get('password_2')
#         print(n,e,c,p1,p2)
#         user = Student.objects.filter(email=e)

#         if user:
#             # return render(req,'login.html',{"msg":"email alredy exist"})
#             req.session['x'] = "email alredy exist"
#             return redirect('login')
#         else:
#             Student.objects.create(name=n,email=e,contact=c,password_1=p1,password_2=p2)
#             return redirect('login')
#     x = req.session.get('x','')
#     return render(req,"register.html",{'x':x})


# def dashboard(req):
#     if 'admin_email' in req.session and 'admin_password' in req.session:
#         a_email = req.session['admin_email']
#         a_password = req.session['admin_password']
#         a_name= req.session['admin_name']
#         a_data = {
#             "name" : a_name,
#             "email" : a_email,
#             "password" : a_password,

#         }
#         return render(req,'admin_dashboard.html',{'data':a_data})
    
#     if 'user_id' in req.session:
#         id = req.session['user_id']
#         userdata = Student.objects.get(id=id)
#         data = {
#             'name':userdata.name,
#             'email':userdata.email,
#             'contact':userdata.contact,
#             'password':userdata.password_1
#         }
#         return render(req,'dashboard.html',{'data':data})
#     else:
#         return redirect('login')

