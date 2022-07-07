from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('index.html', index_view, name='index'),

    path('esg.html', esg_view, name='esg'),
    path('ma.html', esg_view, name='ma'),
    path('supply.html', esg_view, name='supply'),
    path('human_rights.html', esg_view, name='hr'),

    path('integrity.html', integrity_view, name='integrity'),
    path('reputation.html', integrity_view, name='reputation'),
    path('sanctions.html', integrity_view, name='sanctions'),
    path('intelligence.html', integrity_view, name='intelligence'),

    path('investigations.html', investigation_view, name='investigations'),
    path('litigation.html', investigation_view, name='litigation'),
    path('assets.html', investigation_view, name='assets'),
    path('ci.html', investigation_view, name='ci'),

    path('about.html', about_view, name='about'),

    path('team/<int:pk>', team_view, name='team'),

    path('values.html', values_view, name='values'),
]

app_name='website'