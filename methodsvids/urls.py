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
import methodsvids.views

urlpatterns = [

# All of these start with methods/ as defined in urls.py in nutcracker home directory
    url(r'^videos/$', methodsvids.views.methods, name='methods'),
    url(r'^videos/antidifferentiation-by-rule/$', methodsvids.views.antidif_rule, name='antidif_rule'),
    url(r'^videos/binomial-distributions/$', methodsvids.views.binom_dist, name='binom_dist'),
    url(r'^videos/chain-rule/$', methodsvids.views.chain_rule, name='chain_rule'),
    url(r'^videos/combinatorics/$', methodsvids.views.combinatorics, name='combinatorics'),
    url(r'^videos/conditional-probability/$', methodsvids.views.cond_prob, name='cond_prob'),
    url(r'^videos/continuous-distributions/$', methodsvids.views.cont_dist, name='cont_dist'),
    url(r'^videos/cubic-graphs/$', methodsvids.views.cubic_graphs, name='cubic_graphs'),
    url(r'^videos/derivative-and-antiderivative-from-graph/$', methodsvids.views.der_antider_graph, name='der_antider_graph'),
    url(r'^videos/differentiation-by-first-principles/$', methodsvids.views.dif_first_princ, name='dif_first_princ'),
    url(r'^videos/differentiation-by-rule/$', methodsvids.views.dif_rule, name='dif_rule'),
    url(r'^videos/exact-values/$', methodsvids.views.exact_values, name='exact_values'),
    url(r'^videos/exponential-and-log-graphs/$', methodsvids.views.exp_log_graphs, name='exp_log_graphs'),
    url(r'^videos/binomial-finding-sample-size/$', methodsvids.views.finding_samp_size, name='finding_samp_size'),
    url(r'^videos/general-solutions/$', methodsvids.views.general_sols, name='general_sols'),
    url(r'^videos/independant-events/$', methodsvids.views.indep_events, name='indep_events'),
    url(r'^videos/integration-by-recognition/$', methodsvids.views.int_recog, name='int_recog'),
    url(r'^videos/inverses-1/$', methodsvids.views.inverses1, name='inverses1'),
    url(r'^videos/limits/$', methodsvids.views.limits, name='limits'),
    url(r'^videos/matrix-multiplication/$', methodsvids.views.matrix_mult, name='matrix_mult'),
    url(r'^videos/matrix-transformations/$', methodsvids.views.matrix_transforms, name='matrix_transforms'),
    url(r'^videos/measures-of-centre/$', methodsvids.views.measures_centre, name='measures_centre'),
    url(r'^videos/measures-of-spread/$', methodsvids.views.measures_spread, name='measures_spread'),
    url(r'^videos/mutually-exclusive-events/$', methodsvids.views.mut_excl_events, name='mut_excl_events'),
    url(r'^videos/normal-distributions/$', methodsvids.views.norm_dist, name='norm_dist'),
    url(r'^videos/product-rule/$', methodsvids.views.prod_rule, name='prod_rule'),
    url(r'^videos/quotient-rule/$', methodsvids.views.quot_rule, name='quot_rule'),
    url(r'^videos/simultaneous-equations-number-of-solutions/$', methodsvids.views.simul_eqs, name='simul_eqs'),
    url(r'^videos/sin-and-cos-graphs-with-horizontal-translation/$', methodsvids.views.sin_cos_with_horiz, name='sin_cos_with_horiz'),
    url(r'^videos/sin-and-cos-graphs-without-horizontal-translation/$', methodsvids.views.sin_cos_without_horiz, name='sin_cos_without_horiz'),
    url(r'^videos/standard-normal-distributions/$', methodsvids.views.stand_norm, name='stand_norm'),
    url(r'^videos/finding-stationary-points/$', methodsvids.views.stat_points, name='stat_points'),
    url(r'^videos/tan-graphs/$', methodsvids.views.tan_graphs, name='tan_graphs'),
    url(r'^videos/tangents_and_normals/$', methodsvids.views.tangents_normals, name='tangents_normals'),
    url(r'^videos/solving-trig-equations/$', methodsvids.views.trig_eqs, name='trig_eqs'),






]
