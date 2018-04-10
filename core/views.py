from django.shortcuts import render

def index(request):
    return render(request,'index.html',{'section': 'home'})

def about(request):
    return render(request,'about.html',{'section': 'about'})

def tutoring(request):
    return render(request,'tutoring.html',{'section': 'tutoring'})

def contact(request):
    return render(request,'contact.html',{'section': 'contact'})


def videos(request):
    return render(request,'videos.html',{'section': 'videos'})


def sciencevids(request):
    return render(request,'sciencevids.html',{'section': 'videos'})


# Create your views here.
