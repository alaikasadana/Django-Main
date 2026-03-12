"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views



urlpatterns = [
    # path('admin/', admin.site.urls),
    # # path('landingpage/',views.landingpage,name='landingpage') 
    path('',views.landingpage,name='landingpage') ,   
    path('text_response/',views.text_response,name='text')    ,
    path('html_response/',views.html_response,name="html")  ,
    path('json_response/',views.json_response,name="json") ,
    path('download_csv/',views.download_csv,name="csv"),
    path('download_pdf/',views.download_pdf,name="pdf"),
    # path('myrender/',views.myrender,name="render"),

    #dyanmic url
    # path('myrender/<int:x>',views.myrender,name="render"),
    # path('myrender/<str:x>',views.myrender,name="render"),
    # path('myrender/<slug:x>',views.myrender,name="render"),
    path('myrender/<int:age>/<str:name>/<str:quali>/',views.myrender,name="render"),

    path('myredirect1/',views.myredirect2,name="myredirect1") ,
    path('myredirect2/',views.myredirect2,name="myredirect2")


]


