from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from todolist.models import Task

# Create your views here.

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(f"Datos recibidos: Usuario: {username}, Contraseña 1: {password}, Contraseña 2: {password2}")
        
        if User.objects.filter(username=username).exists():
            # Si el nombre de usuario ya existe, muestra un mensaje de error.
            return render(request, 'index.html', {'message1': 'El nombre de usuario ya existe.'})
        elif password!= password2:
            # Si las contraseñas no coinciden, muestra un mensaje de error.
            return render(request, 'index.html',{'message2': 'Las contraseñas no coinciden.'})
        else:
            # Si las contraseñas coinciden, crea el usuario.
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return render(request, 'index.html', {'message3': 'Usuario creado exitosamente.'})    
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a una URL segura después de iniciar sesión
            return redirect('home')
        else:
            # Mensaje más específico para el usuario
            return render(request, 'login.html', {'message': 'Credenciales incorrectas.'})
    
    return render(request, 'login.html')

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})



def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')