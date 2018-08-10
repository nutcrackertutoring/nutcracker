from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from core.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template

from django.http import HttpResponse



def index(request):
    return render(request,'index.html',{'section': 'home'})

def about(request):
    return render(request,'about.html',{'section': 'about'})

def tutoring(request):
    return render(request,'tutoring.html',{'section': 'tutoring'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                contact_email,
                ['nathan.goldwaser@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact_form_sent')
        
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form}, {'section': 'contact'})


def contact_form_sent(request):
    return render(request,'contact_form_sent.html')

def videos(request):
    return render(request,'videos.html',{'section': 'videos'})

def faq(request):
    return render(request,'faq.html',{'section': 'faq'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def test(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                contact_email,
                ['nathan.goldwaser@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact_form_submitted')
        
    else:
        form = ContactForm()
    return render(request, 'test.html', {'form': form})



# Create your views here.
