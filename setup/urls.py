from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # Nova rota invisível que o Javascript vai usar para enviar os dados
    path('salvar_jogada/', views.salvar_jogada, name='salvar_jogada'), 
]