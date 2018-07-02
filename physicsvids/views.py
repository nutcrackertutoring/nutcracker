from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


def physics(request):
    return render(request,'physics.html',{'section': 'videos'})

@login_required
@permission_required('physicsvids.view_physics', raise_exception=True)
def circ_mot_hor(request):
    return render(request,'physics/circ_mot_hor.html',{'section': 'motion'})

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
def muons(request):
    return render(request,'physics/muons.html',{'section': 'relativity'})

@login_required
@permission_required('physicsvids.view_physics', raise_exception=True)
def newtons_laws(request):
    return render(request,'physics/newtons_laws.html',{'section': 'motion'})

@login_required
@permission_required('physicsvids.view_physics', raise_exception=True)
def rh_rules(request):
    return render(request,'physics/rh_rules.html',{'section': 'electromag'})

@login_required
@permission_required('physicsvids.view_physics', raise_exception=True)
def wave_graphs(request):
    return render(request,'physics/wave_graphs.html',{'section': 'waves'})
# Create your views here.
