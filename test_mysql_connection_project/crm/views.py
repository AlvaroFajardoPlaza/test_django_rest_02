from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from .models import User
from .forms import NewUserForm, LoginForm

"""
Dentro de este archivo vamos a gestionar el registro y login de usuarios a nuestra bbdd en MYSQL.
"""

def homepage(request):
    # asignamos a una variable el formulario que hemos creado
    registerForm = NewUserForm()

    # 1. Nos aseguramos que el tipo de request que estamos haciendo es de tipo POST
    if request.method == "POST":
        registerForm = NewUserForm(request.POST)

        # 2. Comprobamos que los datos son válidos
        if registerForm.is_valid():

            try:
                registerForm.save()
                print("Hemos registrado al nuevo usuario")

                return redirect(reverse("crm:dashboard") + '?ok')
            except Exception as e:
                print("No hemos podido registrar a este usuario")
                print(e, type(e).__name)
                return
        # else:
        #     return redirect(reverse("crm:") + '?error')
            
    
    return render(request, "register_login_page.html", {'registerForm': registerForm })


def register(request):
    pass




def my_login(request):

    loginForm = LoginForm()

    # Validamos el método POST
    if request.method == "POST":
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            # Obtenemos los datos del form
            email = loginForm.cleaned_data['email']
            password = loginForm.cleaned_data['password']

            userMatched = get_object_or_404(User, email=email)
            print("Hay userMatched????", userMatched)
            print("La contraseña introducida es:", password)
            print("La contraseña del usuario es:", userMatched.password)

            if (userMatched is not None) and (password == userMatched.password):
                 # La contraseña es correcta
                print("Usuario autenticado correctamente.")
                return redirect(reverse("crm:dashboard") + '?ok')
            else:
                print("Contraseña incorrecta. No has podido hacer login")
                return redirect(reverse("crm") + '?error')
    
    return render(request, "login_page.html", { 'loginForm': loginForm })

        



    


def dashboard(request):
    return render(request, "dashboard.html")



def logout(request):
    pass