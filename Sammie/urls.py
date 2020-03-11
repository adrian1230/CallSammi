"""Sammie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from understand.views import error404, error500
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import handler404, handler500
# from understand.views import register, loginn
from understand.views import Submit, Data

admin.site.site_header = "Sammie"
admin.site.index_title = "Welcome to Sammie's Internal Portal"

urlpatterns = [
    path('ahbjdkasjdk/Sammi/admin/uas9d', admin.site.urls),
    path('',Submit.as_view(),name="SSubmit"),
    # path('',loginn,name="Login"),
    # path('register/',register,name="RegisterS"),
    path('result/',Data.as_view(),name="DataS")
]

handler404 = 'understand.views.error404'
handler500 = 'understand.views.error500'
