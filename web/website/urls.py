from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('index.html', index_view, name='index'),

    path('esg.html', esg_view, name='esg'),
    path('ma.html', ma_view, name='ma'),
    path('supply.html', supply_view, name='supply'),
    path('human_rights.html', hr_view, name='hr'),

    path('integrity.html', integrity_view, name='integrity'),
    path('reputation.html', reputation_view, name='reputation'),
    path('sanctions.html', sanctions_view, name='sanctions'),
    path('intelligence.html', intelligence_view, name='intelligence'),

    path('investigation.html', investigation_view, name='investigation'),
    path('litigation.html', investigation_view, name='litigation'),
    path('assets.html', integrity_view, name='assets'),
    path('ci.html', integrity_view, name='ci'),

    path('about.html', about_view, name='about'),

    path('team/<int:pk>', team_view, name='team'),

    path('values.html', values_view, name='values'),
]