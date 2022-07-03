"""currency_check URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from generator import views

urlpatterns = [
    path('', views.home),
    path('bisection_method_calculator', views.bisection_method_calculator),
    path('chord_method_calculator', views.chord_method_calculator),
    path('newton_method_calculator', views.newton_method_calculator),
    path('simple_iteration_method_calculator', views.simple_iteration_method_calculator),
    path('bisection_method_calculator_result/', views.bisection_method_calculator_result),
    path('chord_method_calculator_result/', views.chord_method_calculator_result),
    path('newton_method_calculator_result/', views.newton_method_calculator_result),
    path('simple_iteration_method_calculator_result/', views.simple_iteration_method_calculator_result),

]
