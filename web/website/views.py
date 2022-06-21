from django.shortcuts import render
from .models import service, team

def index_view(request):
    context = {
        "title":"HOME22 - Frank Partners",
        "link":"https///lkcpölkc",
        "headline": "Boutique risk consultancy specialised in high quality ESG and Integrity Due Diligence"
    }
    return render(request, 'sites/index.html', context)

### ESG ###
def esg_view(request):
    qs = service.objects.filter(headline="ESG")
    print (qs)
    context = {
        "title":"ESG - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/esg.html', context)

def ma_view(request):
    qs = service.objects.filter(headline="M&A ESG due diligence & advisory")
    print (qs)
    context = {
        "title":"ESG - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/esg.html', context)

def supply_view(request):
    qs = service.objects.filter(headline="Supply Chain")
    print (qs)
    context = {
        "title":"Supply Chain - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/supply.html', context)

def hr_view(request):
    qs = service.objects.filter(headline="Human Rights")
    print (qs)
    context = {
        "title":"Human - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/human_rights.html', context)

### INTEGRITY ###

def integrity_view(request):
    qs = service.objects.filter(headline="Reputational & compliance due diligence")
    print (qs)
    context = {
        "title":"Reputational & compliance due diligence - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/reputation.html', context)

def reputation_view(request):
    qs = service.objects.filter(headline="Reputational & compliance due diligence")
    print (qs)
    context = {
        "title":"Reputational & compliance due diligence - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/reputation.html', context)

def sanctions_view(request):
    qs = service.objects.filter(headline="Sanctions")
    print (qs)
    context = {
        "title":"Sanctions - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/sanctions.html', context)

def intelligence_view(request):
    qs = service.objects.filter(headline="Business intelligence")
    print (qs)
    context = {
        "title":"Business intelligence - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/intelligence.html', context)

#INVESTIGATIONS

def investigation_view(request):
    qs = service.objects.filter(headline="Investigation")
    print (qs)
    context = {
        "title":"Investigation - Frank Partners",
        "content": qs,
    }
    return render(request, 'sites/investigation.html', context)

#ABOUT

def about_view(request):
    context = {
        "title":" ABOUT - Frank Partners",
        "headline": "Our Company",
        "text": "FP was established in 2012 as a boutique consultancy specialised in high-end intelligence and integrity due diligence on business partners, investment targets and third parties. Today, we are a diversified industry leader in compliance and ESG advisory services globally, pioneers in applying intelligence gathering skills to the fields of ESG and supply chain risk. Our clients – primarily investment firms and corporates in the Nordics and DACH region – engage us when they require analysis of risks and opportunities in connection with investment targets and business partners. We are known as thorough researchers, yet advisory services are always tailored to our clients’ specific needs. Our analysis helps to just to manage risks but also to seize opportunities – with a focus on value creation and improved sustainability. Never keen to just ‘tick boxes’, we guide our clients’ business strategy by providing actionable and smart recommendations.",
        "name": "Anthony",
        "position": "Project Manager",
    }
    return render(request, 'sites/about.html', context)

def values_view(request):
    context = {
        "title":" VALUES - Frank Partners",
        "headline": "Our Values",
        "text": "FP was established in 2012 as a boutique consultancy specialised in high-end intelligence and integrity due diligence on business partners, investment targets and third parties. Today, we are a diversified industry leader in compliance and ESG advisory services globally, pioneers in applying intelligence gathering skills to the fields of ESG and supply chain risk. Our clients – primarily investment firms and corporates in the Nordics and DACH region – engage us when they require analysis of risks and opportunities in connection with investment targets and business partners. We are known as thorough researchers, yet advisory services are always tailored to our clients’ specific needs. Our analysis helps to just to manage risks but also to seize opportunities – with a focus on value creation and improved sustainability. Never keen to just ‘tick boxes’, we guide our clients’ business strategy by providing actionable and smart recommendations.",
        "name": "Anthony",
        "position": "Project Manager",
    }
    return render(request, 'sites/values.html', context)

def about_view(request):
    qs = team.objects.all()
    print (qs)
    context = {
        "title":" ABOUT - Frank Partners",
        "headline": "Our Values",
        "text": "FP was established in 2012 as a boutique consultancy specialised in high-end intelligence and integrity due diligence on business partners, investment targets and third parties. Today, we are a diversified industry leader in compliance and ESG advisory services globally, pioneers in applying intelligence gathering skills to the fields of ESG and supply chain risk. Our clients – primarily investment firms and corporates in the Nordics and DACH region – engage us when they require analysis of risks and opportunities in connection with investment targets and business partners. We are known as thorough researchers, yet advisory services are always tailored to our clients’ specific needs. Our analysis helps to just to manage risks but also to seize opportunities – with a focus on value creation and improved sustainability. Never keen to just ‘tick boxes’, we guide our clients’ business strategy by providing actionable and smart recommendations.",
        "content": qs,
    }
    return render(request, 'sites/about.html', context)

def team_view(request, pk):
    qs = team.objects.all()
    print (qs)
    context = {
        "title":" ABOUT - Frank Partners",
        "headline": "Our Values",
        "text": "FP was established in 2012 as a boutique consultancy specialised in high-end intelligence and integrity due diligence on business partners, investment targets and third parties. Today, we are a diversified industry leader in compliance and ESG advisory services globally, pioneers in applying intelligence gathering skills to the fields of ESG and supply chain risk. Our clients – primarily investment firms and corporates in the Nordics and DACH region – engage us when they require analysis of risks and opportunities in connection with investment targets and business partners. We are known as thorough researchers, yet advisory services are always tailored to our clients’ specific needs. Our analysis helps to just to manage risks but also to seize opportunities – with a focus on value creation and improved sustainability. Never keen to just ‘tick boxes’, we guide our clients’ business strategy by providing actionable and smart recommendations.",
        "content": qs,
    }
    return render(request, 'sites/profile.html', context)