from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_view, name='login'),
    path('cadastro/', views.registro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),

    path('selecionar-ano/', views.selecionar_ano_view, name='selecionar_ano'),
    path('trocar-ano/', views.trocar_ano_view, name='trocar_ano'),
    path('home/', views.home_view, name='home'),
    path('em-breve/', views.em_breve_view, name='em_breve'),

    path('matematica/', views.menu_matematica, name='menu_matematica'),
    path('matematica/operacoes/', views.menu_operacoes, name='menu_operacoes'),
    path('matematica/numeracao/', views.numeracao_quiz, name='numeracao_quiz'),
    path('matematica/<str:operacao>/', views.niveis_operacao, name='niveis_operacao'),
    path('jogo/<str:operacao>/<str:nivel>/', views.jogo_tabuada, name='jogo_tabuada'),
    path('salvar-jogada/', views.salvar_jogada, name='salvar_jogada'),
    path('relatorio/', views.relatorio_view, name='relatorio'),
    path('painel-professor/', views.painel_professor_view, name='painel_professor'),
    path('painel-professor/aluno/<int:aluno_id>/', views.relatorio_aluno_view, name='relatorio_aluno'),

    path('portugues/', views.menu_portugues, name='menu_portugues'),
    path('portugues/<str:modulo>/', views.portugues_quiz, name='portugues_quiz'),

    path('geografia/', views.menu_geografia, name='menu_geografia'),
    path('geografia/<str:modulo>/', views.geografia_quiz, name='geografia_quiz'),

    path('ingles/', views.menu_ingles, name='menu_ingles'),
    path('ingles/<str:modulo>/', views.ingles_quiz, name='ingles_quiz'),

    path('ciencias/', views.menu_ciencias, name='menu_ciencias'),
    path('ciencias/<str:modulo>/', views.ciencias_quiz, name='ciencias_quiz'),

    path('historia/', views.menu_historia, name='menu_historia'),
    path('historia/<str:modulo>/', views.historia_quiz, name='historia_quiz'),
    # A partir do Passo 5, as demais disciplinas passam a ter suas próprias
    # rotas aqui, no lugar de apontar para 'em_breve'.
]
