from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Feedback, Item, CategoriaItem
from django.contrib.auth.models import User
from .forms import Task, Task2
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator



@login_required(redirect_field_name='login')
def index(request):
    anuncios = Item.objects.all().order_by('-id').filter(ativo=True)
    paginator = Paginator(anuncios, 20)
    page = request.GET.get('p')
    anuncios = paginator.get_page(page)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})






@login_required(redirect_field_name='login')
def detalhe(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'paginas/mostrar.html', {'item': item})

@login_required(redirect_field_name='login')
def anunciar(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')
        cidade = request.POST.get('cidade')
        bairro = request.POST.get('bairro')
        foto = request.FILES.get('foto')
        foto2 = request.FILES.get('foto2')
        foto3 = request.FILES.get('foto3')
        contato = request.POST.get('contato')
        contato2 = request.POST.get('contato2')
        user = get_object_or_404(User, pk=request.user.id)
        
        
        add = Item.objects.create(titulo=titulo, categoria_id=categoria, valor=valor,
                                  descricao=descricao, cidade=cidade, bairro=bairro,
                                  foto=foto, foto2=foto2, foto3=foto3, contato=contato,
                                  contato2=contato2, user=user, data=datetime.now().strftime("%d/%m/%Y"))
        add.save()
        return redirect('home')
    else:
        return render(request, 'paginas/anunciar.html')



@login_required(redirect_field_name='login')
def suporte(request):
    
    if request.method == 'POST':
        motivo = request.POST.get('motivo')
        descricao = request.POST.get('descricao')
        user = get_object_or_404(User, pk=request.user.id)
        add = Feedback.objects.create(user=user, motivo=motivo, descricao=descricao)
        add.save()
        return redirect('home')
    
    else:        
        return render(request, 'paginas/suporte.html')


@login_required(redirect_field_name='login')
def meu_anuncio(request):
    tudo = Item.objects.filter(user_id=request.user.id)
    return render(request, 'paginas/meu_anuncio.html', {'tudo':tudo})


@login_required(redirect_field_name='login')
def animais(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=3,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def eletrodomestico(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=4,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def eletronico(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=5,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def festa(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=6,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def imovel(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=7,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def moda(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=8,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def servico(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=9,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def veiculo(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=10,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def vaga(request):
    anuncios = Item.objects.all().order_by('-id').filter(categoria=11,ativo=True)
    return render(request, 'paginas/index.html', {'anuncios': anuncios})

@login_required(redirect_field_name='login')
def buscar(request):
    termo = request.GET.get('termo')
    anuncios = Item.objects.order_by('-id').filter(titulo__icontains=termo,ativo=True)
    resultados = anuncios.count()
    return render(request, 'paginas/buscar.html', {'anuncios': anuncios, 'resultados':resultados})