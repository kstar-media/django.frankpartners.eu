from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactForm


def contact_page(request):
    forms = ContactForm()
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.INFO, 'Thanks, message sent successfully! Check your Email for further Informations')
            send_mail(
                'Contact Form',
                'Here is the message.',
                'coretics@outlook.com',
                ['munichstyles@gmail.com', 'ck@kstar-media.de'],
                fail_silently=False,
                )
            return redirect('contact:contact')
    context = {
        'forms': forms
    }

    return render(request, 'contact/contact.html', context)