from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render(request,'login.html',{'status':status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html',{'status':status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario.objects.filter(email=email)

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')


    try:
        senha = sha256(senha.encode()).hexdigest() # Criptografa a senha
        usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha
        )
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')
    


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        # armazenando numa session, que é uma variavel global do sistema, o id do usuario que acabou de fazer login
        request.session['usuario'] = usuario[0].id
        return redirect('/livro/home/')


def sair(request):
    request.session.flush() # Limpa a sessão em que o usuário estava logado
    return redirect('/auth/login/')