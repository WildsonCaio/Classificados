from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detalhe/n°<int:id>',views.detalhe, name='detalhe'),
    path('anunciar/',views.anunciar, name='anunciar'),
    path('suporte/', views.suporte, name='suporte'),
    path('meus_anúncios/', views.meu_anuncio, name="meu_anuncio"),
    path('Animais_de_Estimação/', views.animais, name="animais"),
    path('Eletrodomésticos/', views.eletrodomestico, name="eletro"),
    path('Eletrônicos_e_Celulares/', views.eletronico, name="eletronico"),
    path('Festas_e_Eventos/', views.festa, name="festa"),
    path('Imóveis/', views.imovel, name="imovel"),
    path('Moda_e_Beleza/', views.moda, name="moda"),
    path('Serviços/', views.servico, name="servico"),
    path('Veículos_e_Peças/', views.veiculo, name="veiculo"),
    path('Vagas_de_Emprego/', views.vaga, name="vaga"),
    path('buscar/', views.buscar, name="buscar")
    
]
