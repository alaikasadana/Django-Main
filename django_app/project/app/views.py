print("views pagr call")

from django.shortcuts import render , redirect

# Create your views here.
from django.http import HttpResponse
import json
import csv
from django .urls import reverse
from urllib.parse import urlencode


def landingpage(req):
    # return HttpResponse("hello this is django project")
    # return HttpResponse("<h1 style='color:yellow;'>hello this is django project</h1>")
    return HttpResponse("<h1>hello this is django project</h1>")

def text_response(req):
    return HttpResponse("This is plain text response ." , content_type="text/plain")

def html_response(req):
    return HttpResponse("<h1>This is  HTML response .</h1>" , content_type="text/html")

def json_response(req):
    data={'name':'alaika','age':19,'course':'BCA'}
    json_data=json.dumps(data)
    return HttpResponse(json_data , content_type="application/json")


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Department', 'Salary'])
    writer.writerow(['Neeraj', 'IT', 50000])
    writer.writerow(['Ravi', 'HR', 40000])
    return response

def download_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Example content (real projects use ReportLab or WeasyPrint)
    response.write("This is a dummy PDF content.")
    return response

# def css_response(request):
#     css_content = " " "
#     body{
#         background-color:#f0f0f0;
#         font-family: Arial , sans-serif;

#     }

#     h1 {
#         color : blue;
#         text-align: center;

#     }

#     " " "
#     return HttpResponse(css_content , content_type="text/css")

# def myrender(request):
#        data={'name':'alaika',
#             'age':20,
#             'quali':'BCA'
          
#       }
#        return render (request , 'myrender.html',data) 

# def myrender(request,x):
#        data={'age':x}
#        return render (request , 'myrender.html',data) 

def myrender(request,name,age,quali):
       data={'name':name,
             'age':age,
             'qualification' :quali
            
          
      }
       return render (request , 'myrender.html',data)


def myredirect1(req):
    url = reverse ('myredirect2')
    data = urlencode({'name':'alaika','age':10})
    return redirect (f'{url}?{data}')

def myredirect2(req):
    print("Hello")
    # print(req.method)
    # print(req.get)
    return HttpResponse("hello")
