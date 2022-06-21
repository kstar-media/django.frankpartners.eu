from django.shortcuts import render

def index_view(request):
    context = {
        "title":"HOME - Frank Partners",
        "headline": "Boutique risk consultancy specialised in high quality ESG and Integrity Due Diligence"
    }
    return render(request, 'sites/index.html', context)

def service_view(request):
    context = {
        "title":"ESG - Frank Partners",
        "headline": "ESG Services"
    }
    return render(request, 'sites/service.html', context)

def integrity_view(request):
    context = {
        "title":"INTEGRITY - Frank Partners",
        "headline": "Integrity Services"
    }
    return render(request, 'sites/integrity.html', context)