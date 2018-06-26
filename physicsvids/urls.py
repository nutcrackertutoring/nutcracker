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

from django.conf.urls import url
import physicsvids.views

urlpatterns = [

# All of these start with physics/ as defined in urls.py in nutcracker home directory
    url(r'^videos/$', physicsvids.views.physics, name='physics'),
    url(r'^videos/circular-motion-horizontal-plane/$', physicsvids.views.circ_mot_hor, name='circ_mot_hor'),
    url(r'^videos/connected-bodies/$', physicsvids.views.con_bodies, name='con_bodies'),
    url(r'^videos/electromagnetic-induction/$', physicsvids.views.electromag_induc, name='electromag_induc'),
    url(r'^videos/incline-plane/$', physicsvids.views.incline_plane, name='incline_plane'),
    url(r'^videos/newtons-3-laws/$', physicsvids.views.newtons_laws, name='newtons_laws'),





]
