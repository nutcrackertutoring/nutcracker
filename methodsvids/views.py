from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required



def methods(request):
    return render(request,'methods.html',{'section': 'videos'})


@permission_required('methodsvids.view_methods', raise_exception=True)
def antidif_rule(request):
    return render(request,'methods/antidif_rule.html',{'section': 'antidif'})


# Create your views here.
