from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from webcafe.settings import EMAIL_HOST_USER

# Create your views here.
def contact (request):
    contact_form = ContactForm
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name= request.POST.get("name","")
            email= request.POST.get("email","")
            content= request.POST.get("content","")
            #Enviar correo
            email=EmailMessage(
                "WebCafe: Nuevo Mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                EMAIL_HOST_USER,
                #email destino
                "dani20cu@gmail.com",
                reply_to=[email]
            )
            try:
                email.send()
                return redirect (reverse("contact") + "?ok")
            except:
                return redirect (reverse("contact") + "?fail")
        
    return render(request, "contact/contact.html", {"form": contact_form})