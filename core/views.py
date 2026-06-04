import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import RegistroJogada

# --- SISTEMA DE ACESSO ---
def login_view(request):
    erro = None
    if request.method == 'POST':
        usuario_digitado = request.POST.get('usuario')
        senha_digitada = request.POST.get('senha')
        user = authenticate(request, username=usuario_digitado, password=senha_digitada)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            erro = "E-mail ou senha incorretos. Tente novamente!"
    return render(request, 'login.html', {'erro': erro})

def logout_view(request):
    logout(request)
    return redirect('login')

def registro_view(request):
    erro = None
    sucesso = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if not email.endswith('@csanl.com.br'):
            erro = "Acesso negado: Utilize o e-mail oficial do colégio (@csanl.com.br)."
        elif User.objects.filter(username=email).exists():
            erro = "Este e-mail já está cadastrado!"
        else:
            user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
            user.save()
            sucesso = "Aluno cadastrado com sucesso! Faça o login."
    return render(request, 'registro.html', {'erro': erro, 'sucesso': sucesso})

# --- TELAS DE NAVEGAÇÃO DO PORTAL ---
@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/')
def matematica(request):
    return render(request, 'matematica.html')

@login_required(login_url='/')
def niveis_adicao(request):
    return render(request, 'niveis_adicao.html')

@login_required(login_url='/')
def niveis_subtracao(request):
    return render(request, 'niveis_subtracao.html')

@login_required(login_url='/')
def niveis_multiplicacao(request):
    return render(request, 'niveis_multiplicacao.html')

@login_required(login_url='/')
def niveis_divisao(request):
    return render(request, 'niveis_divisao.html')

# --- O PAINEL DE RELATÓRIO ---
@login_required(login_url='/')
def relatorio_desempenho(request):
    # Puxa apenas as jogadas do aluno que está logado
    jogadas = RegistroJogada.objects.filter(jogador=request.user)
    total_geral = jogadas.count()
    
    estatisticas_matematica = []
    
    if total_geral > 0:
        operacoes = ['adicao', 'subtracao', 'multiplicacao', 'divisao']
        icones = {'adicao': '➕', 'subtracao': '➖', 'multiplicacao': '✖️', 'divisao': '➗'}
        
        for op in operacoes:
            jogadas_op = jogadas.filter(operacao=op)
            total_op = jogadas_op.count()
            
            if total_op > 0:
                acertos = jogadas_op.filter(acertou=True).count()
                taxa = (acertos / total_op) * 100
                tempo_medio = jogadas_op.aggregate(Avg('tempo_segundos'))['tempo_segundos__avg']
                
                estatisticas_matematica.append({
                    'operacao': op.capitalize(),
                    'icone': icones[op],
                    'total': total_op,
                    'acertos': acertos,
                    'erros': total_op - acertos,
                    'taxa_acerto': round(taxa, 1),
                    'tempo_medio': round(tempo_medio, 1) if tempo_medio else 0
                })

    contexto = {
        'total_geral': total_geral,
        'estatisticas': estatisticas_matematica
    }
    
    return render(request, 'relatorio.html', contexto)

# --- O JOGO INTELIGENTE ---
@login_required(login_url='/')
def jogo_tabuada(request, operacao, nivel):
    contexto = {
        'operacao': operacao,
        'nivel': nivel
    }
    return render(request, 'jogo.html', contexto)

@csrf_exempt
def salvar_jogada(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            usuario_logado = request.user if request.user.is_authenticated else None
            
            RegistroJogada.objects.create(
                jogador=usuario_logado,
                operacao=dados.get('operacao', 'multiplicacao'),
                nivel=dados.get('nivel', 'unidades'),
                numero_1=dados['numero_1'],
                numero_2=dados['numero_2'],
                resposta_aluno=dados['resposta_aluno'],
                acertou=dados['acertou'],
                tempo_segundos=dados['tempo_segundos']
            )
            return JsonResponse({'status': 'sucesso'})
        except Exception as e:
            return JsonResponse({'status': 'erro', 'mensagem': str(e)})
            
    return JsonResponse({'status': 'metodo_invalido'})