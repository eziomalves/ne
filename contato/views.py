from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages

def contato(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
                messages.info(request,'E-mail enviado com sucesso.')
            except BadHeaderError:
                messages.info(request,'Erro ao enviar e-mail.')
       
    return render(request, "contato.html", {'form': form})
