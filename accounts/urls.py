from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    path('<int:id>', views.vender, name='vender') 
               ]