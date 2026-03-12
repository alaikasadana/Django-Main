
from django.urls import path 
from .views import *

urlpatterns = [
  
    path('',Stu_list.as_view()),
    path('stu_Detail/<int:pk>/' ,Stu_Detail.as_view()),
]




