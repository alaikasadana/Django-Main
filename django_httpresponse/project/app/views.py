from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def text_response(request):
 return HttpResponse("This is a plain text response.",
 content_type="text/plain")

def html_response(request):
 html = "<h1>Welcome to My Django Site</h1><p>This is HTML content.</p>"
 return HttpResponse(html, content_type="text/html")

