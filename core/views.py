from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

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

@login_required
@user_passes_test(lambda u: u.is_superuser)
def test(request):
	return render(request,'test.html')



# Create your views here.
