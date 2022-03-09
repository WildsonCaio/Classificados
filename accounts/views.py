from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from paginas.models import Item


def cadastro(request):

    try:
        usuario_aux = User.objects.get(username=request.POST['usu'])

        if usuario_aux:
            messages.info(request, 'Usuário com esse nome ja existe.')
            return render(request, 'paginas/cadastro.html')

    except:
        if request.method == "POST":
            user = request.POST['usu']
            contato = request.POST.get('numero')
            senha = request.POST['senha']
            senha2 = request.POST['senha2']
            
            if senha != senha2:
                messages.info(request, 'Senhas não coincidem, tente novamente.')
                return render(request, 'paginas/cadastro.html')
            
            elif len(senha) < 5:
                messages.info(request, 'A senha precisa ter mais que 4 digitos.')
                return render(request, 'paginas/cadastro.html')
            
            else:
                add = User.objects.create_user(username=user, password=senha, first_name=contato)
                add.save()
                return redirect('login')

        else:
            return render(request, 'paginas/cadastro.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("usuario")
        password = request.POST.get("senha")
        usuario = auth.authenticate(
            request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.info(request, 'Usuário ou Senha incorretos.')
            return render(request, 'paginas/login.html')
    else:
        return render(request, 'paginas/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def vender(request, id):
    remover = get_object_or_404(Item, id=id)
    remover.delete()
    return redirect('meu_anuncio')