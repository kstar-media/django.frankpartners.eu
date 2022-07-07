from django.shortcuts import render
from .models import service, team

def index_view(request):
    context = {
        "title":"HOME - Frank Partners",
        "link":"https///lkcpölkc",
        "headline": "Boutique risk consultancy specialised in high quality ESG and Integrity Due Diligence"
    }
    return render(request, 'sites/index.html', context)

### ESG ###
def esg_view(request):
    esg = service.objects.filter(group="ESG").order_by('id')

    print (esg)
    context = {
        "title":"ESG - Frank Partners",
        "content": esg,
    }
    return render(request, 'sites/esg.html', context)

### INTEGRITY ###

def integrity_view(request):
    integrity = service.objects.filter(group="Integrity").order_by('-id')
    print (integrity)
    context = {
        "title":"Integrity - Frank Partners",
        "content": integrity,
    }
    return render(request, 'sites/integrity.html', context)

#INVESTIGATIONS

def investigation_view(request):
    investigations = service.objects.filter(group="Investigations").order_by('id')
    print (investigations)
    context = {
        "title":"Investigation - Frank Partners",
        "content": investigations,
    }
    return render(request, 'sites/investigations.html', context)

#ABOUT

def about_view(request):
    context = {
        "title":" ABOUT - Frank Partners",
        "headline": "Our Company",
        "text": "FP was established in 2012 as a boutique consultancy specialised in high-end intelligence and integrity due diligence on business partners, investment targets and third parties. Today, we are a diversified industry leader in compliance and ESG advisory services globally, pioneers in applying intelligence gathering skills to the fields of ESG and supply chain risk. Our clients – primarily investment firms and corporates in the Nordics and DACH region – engage us when they require analysis of risks and opportunities in connection with investment targets and business partners. We are known as thorough researchers, yet advisory services are always tailored to our clients’ specific needs. Our analysis helps to just to manage risks but also to seize opportunities – with a focus on value creation and improved sustainability. Never keen to just ‘tick boxes’, we guide our clients’ business strategy by providing actionable and smart recommendations.",
        "head2": "Anthony",
        "text2": "Project Manager",
    }
    return render(request, 'sites/about.html', context)

def values_view(request):
    context = {
        "title":" VALUES - Frank Partners",
        "headline": "Our Values",
        "text": "FP was established in 2012 as a boutique consultancy specialised in high-end intelligence and integrity due diligence on business partners, investment targets and third parties. Today, we are a diversified industry leader in compliance and ESG advisory services globally, pioneers in applying intelligence gathering skills to the fields of ESG and supply chain risk. Our clients – primarily investment firms and corporates in the Nordics and DACH region – engage us when they require analysis of risks and opportunities in connection with investment targets and business partners. We are known as thorough researchers, yet advisory services are always tailored to our clients’ specific needs. Our analysis helps to just to manage risks but also to seize opportunities – with a focus on value creation and improved sustainability. Never keen to just ‘tick boxes’, we guide our clients’ business strategy by providing actionable and smart recommendations.",
        "head2": "Anthony",
        "text2": "Project Manager",
    }
    return render(request, 'sites/values.html', context)

def about_view(request):
    qs = team.objects.all()
    print (qs)
    context = {
        "title":" ABOUT - Frank Partners",
        "headline": "Our Company",
        "text": "FP was established in 2012 as a boutique consultancy specialised in high-end intelligence and integrity due diligence on business partners, investment targets and third parties. Today, we are a diversified industry leader in compliance and ESG advisory services globally, pioneers in applying intelligence gathering skills to the fields of ESG and supply chain risk. Our clients – primarily investment firms and corporates in the Nordics and DACH region – engage us when they require analysis of risks and opportunities in connection with investment targets and business partners. We are known as thorough researchers, yet advisory services are always tailored to our clients’ specific needs. Our analysis helps to just to manage risks but also to seize opportunities – with a focus on value creation and improved sustainability. Never keen to just ‘tick boxes’, we guide our clients’ business strategy by providing actionable and smart recommendations.",
        "content": qs,
    }
    return render(request, 'sites/about.html', context)

def team_view(request, pk):
    qs = team.objects.get(id=pk)
    print (qs)
    context = {
        "title":" ABOUT - Frank Partners",
        "headline": "Our Values",
        "text": "FP was established in 2012 as a boutique consultancy specialised in high-end intelligence and integrity due diligence on business partners, investment targets and third parties. Today, we are a diversified industry leader in compliance and ESG advisory services globally, pioneers in applying intelligence gathering skills to the fields of ESG and supply chain risk. Our clients – primarily investment firms and corporates in the Nordics and DACH region – engage us when they require analysis of risks and opportunities in connection with investment targets and business partners. We are known as thorough researchers, yet advisory services are always tailored to our clients’ specific needs. Our analysis helps to just to manage risks but also to seize opportunities – with a focus on value creation and improved sustainability. Never keen to just ‘tick boxes’, we guide our clients’ business strategy by providing actionable and smart recommendations.",
        "content": qs,
    }
    return render(request, 'sites/profile.html', context)