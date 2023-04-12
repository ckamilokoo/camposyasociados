from django.shortcuts import render , redirect
from .forms import FormularioContacto
from django.views.decorators.csrf import requires_csrf_token

from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre =request.POST.get("nombre")
            email =request.POST.get("email")
            contenido =request.POST.get("contenido")

            email=EmailMessage("Mensaje desde app django",
            "el usuario con nombre {} con la direccion  {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["camilo.camposog@gmail.com"],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html",{'miFormulario':FormularioContacto})


