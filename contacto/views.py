from django.shortcuts import redirect, render
from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            telefono = request.POST.get("telefono")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {}, el teléfono {} y con la dirección email {} escribe lo siguiente:\n\n {}".format(nombre, telefono, email, contenido),
            "",["samusdr27@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except Exception as ex:
                print(ex)
                return redirect("/contacto/?noValido")

            
            # email = EmailMessage("Mensaje desde Samu_SDR17 WebSite",
            # " {}, {}, {}, Mensaje:\n\n {}".format(nombre, telefono, email, contenido),
            # "",["samusdr27@gmail.com"],reply_to=[email])

            # try:
            #     email.send()
            #     return redirect("/contacto/?valido")
            # except:
            #     return redirect("/contacto/?novalido")


    return render(request, 'contacto/contacto.html', {'miFormulario': formulario_contacto})