"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('services/', views.services, name='services'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('add_department',views.add_department,name='add_department'),
    path('all_department',views.all_department,name='all_department'),
    path('save_department',views.save_department,name='save_department'),
    # path('addemp',views.addemp,name='addemp'),
    path('add_employees',views.add_employees,name='add_employees'),
    path('save_emp',views.save_emp,name="save_emp")

    # path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard')
     # path('register/',views.register,name='register'),

]
