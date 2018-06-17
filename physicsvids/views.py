from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


def physics(request):
    return render(request,'physics.html',{'section': 'videos'})

@login_required
@permission_required('physicsvids.view_physics', raise_exception=True)
def con_bodies(request):
    return render(request,'physics/con_bodies.html',{'section': 'motion'})

@login_required
@permission_required('physicsvids.view_physics', raise_exception=True)
def electromag_induc(request):
    return render(request,'physics/electromag_induc.html',{'section': 'electromag'})

@login_required
@permission_required('physicsvids.view_physics', raise_exception=True)
def incline_plane(request):
    return render(request,'physics/incline_plane.html',{'section': 'motion'})

@login_required
@permission_required('physicsvids.view_physics', raise_exception=True)
def newtons_laws(request):
    return render(request,'physics/newtons_laws.html',{'section': 'motion'})

# Create your views here.
