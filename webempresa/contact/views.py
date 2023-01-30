from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    context = {
        'form': contact_form,
    }

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos correo y redireccionamos
            email = EmailMessage(
                "Mensaje de contacto",
                "De {} <{}>\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["edeajob27@gmail.com"],
                reply_to=[email]
            )
            try:
                # Todo salio bien
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                # Algo salio mal
                return redirect(reverse('contact') + "?fail")

    return render(request,'contact/contact.html',context)