from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.login_view, name='login'), 
    path('sair/', views.logout_view, name='logout'), 
    path('cadastro/', views.registro_view, name='registro'), 
    
    path('home/', views.home, name='home'), 
    path('relatorio/', views.relatorio_desempenho, name='relatorio'), 
    
    path('matematica/', views.matematica, name='matematica'), 
    path('matematica/adicao/', views.niveis_adicao, name='niveis_adicao'), 
    path('matematica/subtracao/', views.niveis_subtracao, name='niveis_subtracao'), 
    path('matematica/multiplicacao/', views.niveis_multiplicacao, name='niveis_multiplicacao'), 
    path('matematica/divisao/', views.niveis_divisao, name='niveis_divisao'), 
    
    # Rota inteligente: recebe a operacao e o nivel direto da URL
    path('jogo/<str:operacao>/<str:nivel>/', views.jogo_tabuada, name='jogo_tabuada'), 
    
    path('salvar_jogada/', views.salvar_jogada, name='salvar_jogada'), 
]