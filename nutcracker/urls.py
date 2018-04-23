"""nutcracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

import core.views
import accounts.views

urlpatterns = [
# CORE
    url(r'^$', core.views.index, name='home'),
    url(r'^about/$', core.views.about, name='about'),
    url(r'^tutoring/$', core.views.tutoring, name='tutoring'),
    url(r'^contact/$', core.views.contact, name='contact'),
    url(r'^videos/$', core.views.videos, name='videos'),
    url(r'^admin/', admin.site.urls),

# ACCOUNTS
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', accounts.views.signup, name='signup'),
    url(r'^signedup/$', accounts.views.signedup, name='signedup'),
    url(r'^change_password/$', accounts.views.change_password, name='change_password'),
    url(r'^password_changed/$', accounts.views.password_changed, name='password_changed'),
    url(r'^my_account/$', accounts.views.my_account, name='my_account'),

# SCIENCE
    url(r'^science/videos/$', core.views.sciencevids, name='sciencevids'),

# METHODS
    path('methods/', include('methodsvids.urls'))



]
