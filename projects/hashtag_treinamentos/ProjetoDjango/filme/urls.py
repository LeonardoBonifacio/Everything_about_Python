# url - view - templates

from django.urls import path,include
from .views import HomePage,HomeFilmes, DetalhesFilme,PesquisaFilme,Paginaperfil
from django.contrib.auth import views as auth_view # views de autentificação do login do usuário

app_name = 'filme'

urlpatterns = [
    path('', HomePage.as_view(), name = 'homepage'),
    path('filmes/', HomeFilmes.as_view(), name = 'homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name = 'detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name = 'pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html') ,name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html') ,name='logout'), 
    path('editarperfil', Paginaperfil.as_view(), name='editarperfil'),
]