from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required



def methods(request):
    return render(request,'methods.html',{'section': 'videos'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def antidif_rule(request):
    return render(request,'methods/antidif_rule.html',{'section': 'antidif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def binom_dist(request):
    return render(request,'methods/binom_dist.html',{'section': 'prob_dist'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def chain_rule(request):
    return render(request,'methods/chain_rule.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def combinatorics(request):
    return render(request,'methods/combinatorics.html',{'section': 'discrete'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def cond_prob(request):
    return render(request,'methods/cond_prob.html',{'section': 'discrete'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def cont_dist(request):
    return render(request,'methods/cont_dist.html',{'section': 'prob_dist'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def cubic_graphs(request):
    return render(request,'methods/cubic_graphs.html',{'section': 'func_graph'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def der_antider_graph(request):
    return render(request,'methods/der_antider_graph.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def dif_first_princ(request):
    return render(request,'methods/dif_first_princ.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def dif_rule(request):
    return render(request,'methods/dif_rule.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def exact_values(request):
    return render(request,'methods/exact_values.html',{'section': 'trig'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def exp_log_graphs(request):
    return render(request,'methods/exp_log_graphs.html',{'section': 'func_graph'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def finding_samp_size(request):
    return render(request,'methods/finding_samp_size.html',{'section': 'prob_dist'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def general_sols(request):
    return render(request,'methods/general_sols.html',{'section': 'trig'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def indep_events(request):
    return render(request,'methods/indep_events.html',{'section': 'discrete'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def int_recog(request):
    return render(request,'methods/int_recog.html',{'section': 'antidif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def inverses1(request):
    return render(request,'methods/inverses1.html',{'section': 'func_graph'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def limits(request):
    return render(request,'methods/limits.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def matrix_mult(request):
    return render(request,'methods/matrix_mult.html',{'section': 'func_graph'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def matrix_transforms(request):
    return render(request,'methods/matrix_transforms.html',{'section': 'func_graph'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def measures_centre(request):
    return render(request,'methods/measures_centre.html',{'section': 'discrete'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def measures_spread(request):
    return render(request,'methods/measures_spread.html',{'section': 'discrete'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def mut_excl_events(request):
    return render(request,'methods/mut_excl_events.html',{'section': 'discrete'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def norm_dist(request):
    return render(request,'methods/norm_dist.html',{'section': 'prob_dist'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def prod_rule(request):
    return render(request,'methods/prod_rule.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def quot_rule(request):
    return render(request,'methods/quot_rule.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def simul_eqs(request):
    return render(request,'methods/simul_eqs.html',{'section': 'func_graph'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def sin_cos_with_horiz(request):
    return render(request,'methods/sin_cos_with_horiz.html',{'section': 'trig'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def sin_cos_without_horiz(request):
    return render(request,'methods/sin_cos_without_horiz.html',{'section': 'trig'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def stand_norm(request):
    return render(request,'methods/stand_norm.html',{'section': 'prob_dist'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def stat_points(request):
    return render(request,'methods/stat_points.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def tan_graphs(request):
    return render(request,'methods/tan_graphs.html',{'section': 'trig'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def tangents_normals(request):
    return render(request,'methods/tangents_normals.html',{'section': 'dif'})

@login_required
@permission_required('methodsvids.view_methods', raise_exception=True)
def trig_eqs(request):
    return render(request,'methods/trig_eqs.html',{'section': 'trig'})



# Create your views here.
