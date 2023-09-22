from django.shortcuts import render

from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novoUsuario = Usuario()
    novoUsuario.nome = request.POST.get('nome')
    novoUsuario.idade = request.POST.get('idade')
    novoUsuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)