import json
import random
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
def menu_portugues(request):
    return render(request, 'menu_portugues.html')

@login_required(login_url='/')
def menu_ingles(request):
    return render(request, 'menu_ingles.html')

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

# --- O PAINEL DE RELATÓRIO RECONSTRUÍDO ---
@login_required(login_url='/')
def relatorio_desempenho(request):
    jogadas = RegistroJogada.objects.filter(jogador=request.user)
    total_geral = jogadas.count()
    
    estatisticas_matematica = []
    estatisticas_ingles = []
    estatisticas_portugues = []
    
    if total_geral > 0:
        operacoes_math = ['adicao', 'subtracao', 'multiplicacao', 'divisao']
        icones_math = {'adicao': '➕', 'subtracao': '➖', 'multiplicacao': '✖️', 'divisao': '➗'}
        for op in operacoes_math:
            jogadas_op = jogadas.filter(operacao=op)
            if jogadas_op.count() > 0:
                acertos = jogadas_op.filter(acertou=True).count()
                taxa = (acertos / jogadas_op.count()) * 100
                tempo_medio = jogadas_op.aggregate(Avg('tempo_segundos'))['tempo_segundos__avg']
                estatisticas_matematica.append({
                    'operacao': op.capitalize(), 'icone': icones_math[op], 'total': jogadas_op.count(),
                    'acertos': acertos, 'erros': jogadas_op.count() - acertos,
                    'taxa_acerto': round(taxa, 1), 'tempo_medio': round(tempo_medio, 1) if tempo_medio else 0
                })
        
        jogos_ingles = [('ingles', 'Vocabulário (Palavras)'), ('ingles_frases', 'Completar Frases')]
        for op_id, nome_op in jogos_ingles:
            jogadas_op = jogadas.filter(operacao=op_id)
            if jogadas_op.count() > 0:
                rodadas_perfeitas = jogadas_op.filter(acertou=True).count()
                taxa_op = (rodadas_perfeitas / jogadas_op.count()) * 100
                tempo_medio = jogadas_op.aggregate(Avg('tempo_segundos'))['tempo_segundos__avg']
                estatisticas_ingles.append({
                    'nome': nome_op, 'total_rodadas': jogadas_op.count(), 'rodadas_perfeitas': rodadas_perfeitas,
                    'taxa_perfeicao': round(taxa_op, 1), 'tempo_medio': round(tempo_medio, 1) if tempo_medio else 0
                })

        # Relatório atualizado com os 4 jogos!
        jogos_portugues = [
            ('portugues_ortografia', 'Ortografia'), 
            ('portugues_silaba', 'Sílaba Tônica'), 
            ('portugues_sinonimos', 'Sinónimos/Antónimos'),
            ('portugues_silabas', 'Caçador de Sílabas')
        ]
        for op_id, nome_op in jogos_portugues:
            jogadas_op = jogadas.filter(operacao=op_id)
            if jogadas_op.count() > 0:
                rodadas_perfeitas = jogadas_op.filter(acertou=True).count()
                taxa_op = (rodadas_perfeitas / jogadas_op.count()) * 100
                tempo_medio = jogadas_op.aggregate(Avg('tempo_segundos'))['tempo_segundos__avg']
                estatisticas_portugues.append({
                    'nome': nome_op, 'total_rodadas': jogadas_op.count(), 'rodadas_perfeitas': rodadas_perfeitas,
                    'taxa_perfeicao': round(taxa_op, 1), 'tempo_medio': round(tempo_medio, 1) if tempo_medio else 0
                })

    contexto = {
        'total_geral': total_geral,
        'estatisticas': estatisticas_matematica,
        'estatisticas_ingles': estatisticas_ingles,
        'estatisticas_portugues': estatisticas_portugues
    }
    return render(request, 'relatorio.html', contexto)

# --- O JOGO INTELIGENTE ---
@login_required(login_url='/')
def jogo_tabuada(request, operacao, nivel):
    contexto = {'operacao': operacao, 'nivel': nivel}
    return render(request, 'jogo.html', contexto)

@csrf_exempt
def salvar_jogada(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            usuario_logado = request.user if request.user.is_authenticated else None
            RegistroJogada.objects.create(
                jogador=usuario_logado, operacao=dados.get('operacao', 'multiplicacao'),
                nivel=dados.get('nivel', 'unidades'), numero_1=dados.get('numero_1', 0),
                numero_2=dados.get('numero_2', 0), resposta_aluno=dados.get('resposta_aluno', '0'),
                acertou=dados.get('acertou', True), tempo_segundos=dados.get('tempo_segundos', 0)
            )
            return JsonResponse({'status': 'sucesso'})
        except Exception as e:
            return JsonResponse({'status': 'erro', 'mensagem': str(e)})
    return JsonResponse({'status': 'metodo_invalido'})

# --- MÓDULO DE INGLÊS ---
@login_required(login_url='/')
def ingles_vocabulario(request):
    vocabulario = [
        {'palavra': 'Dog', 'emoji': '🐶'}, {'palavra': 'Cat', 'emoji': '🐱'}, 
        {'palavra': 'Spider', 'emoji': '🕷️'}, {'palavra': 'Mouse', 'emoji': '🐭'},
        {'palavra': 'Bird', 'emoji': '🐦'}, {'palavra': 'Lion', 'emoji': '🦁'},
        {'palavra': 'Fish', 'emoji': '🐟'}, {'palavra': 'Chicken', 'emoji': '🐔'},
        {'palavra': 'Elephant', 'emoji': '🐘'}, {'palavra': 'School', 'emoji': '🏫'}, 
        {'palavra': 'Book', 'emoji': '📖'}, {'palavra': 'Pencil', 'emoji': '✏️'}, 
        {'palavra': 'Computer', 'emoji': '💻'}, {'palavra': 'Chair', 'emoji': '🪑'}, 
        {'palavra': 'Classroom', 'emoji': '🧑‍🏫'}, {'palavra': 'Student', 'emoji': '🎒'},
        {'palavra': 'Earth', 'emoji': '🌍'}, {'palavra': 'Sun', 'emoji': '☀️'},
        {'palavra': 'Moon', 'emoji': '🌙'}, {'palavra': 'Rain', 'emoji': '🌧️'},
        {'palavra': 'Tree', 'emoji': '🌳'}, {'palavra': 'River', 'emoji': '🏞️'},
        {'palavra': 'Fire', 'emoji': '🔥'}, {'palavra': 'Snow', 'emoji': '❄️'},
        {'palavra': 'Wind', 'emoji': '🌬️'}, {'palavra': 'Beach', 'emoji': '🏖️'},
        {'palavra': 'Car', 'emoji': '🚗'}, {'palavra': 'Airplane', 'emoji': '✈️'},
        {'palavra': 'Bus', 'emoji': '🚌'}, {'palavra': 'Building', 'emoji': '🏢'},
        {'palavra': 'Church', 'emoji': '⛪'}, {'palavra': 'House', 'emoji': '🏠'}, 
        {'palavra': 'Door', 'emoji': '🚪'}, {'palavra': 'Kitchen', 'emoji': '🍽️'}, 
        {'palavra': 'Bedroom', 'emoji': '🛏️'}, {'palavra': 'Lamp', 'emoji': '💡'}, 
        {'palavra': 'Window', 'emoji': '🪟'}, {'palavra': 'Umbrella', 'emoji': '☔'}, 
        {'palavra': 'Table', 'emoji': '/static/img/table.png', 'is_image': True},
        {'palavra': 'Orange', 'emoji': '🍊'}, {'palavra': 'Apple', 'emoji': '🍎'},
        {'palavra': 'Potato', 'emoji': '🥔'}, {'palavra': 'Banana', 'emoji': '🍌'},
        {'palavra': 'Pineapple', 'emoji': '🍍'}, {'palavra': 'Onion', 'emoji': '🧅'},
        {'palavra': 'Tomato', 'emoji': '🍅'}, {'palavra': 'Mango', 'emoji': '🥭'},
        {'palavra': 'Hat', 'emoji': '🎩'}, {'palavra': 'Shorts', 'emoji': '🩳'},
        {'palavra': 'Shirt', 'emoji': '👕'}, {'palavra': 'Pants', 'emoji': '👖'},
        {'palavra': 'Jacket', 'emoji': '🧥'}, {'palavra': 'Shoes', 'emoji': '👞'},
        {'palavra': 'Foot', 'emoji': '🦶'}, {'palavra': 'Feet', 'emoji': '👣'},
        {'palavra': 'Hand', 'emoji': '🖐️'}, {'palavra': 'Eye', 'emoji': '👁️'},
        {'palavra': 'Head', 'emoji': '👤'}, {'palavra': 'Hair', 'emoji': '💇'},
        {'palavra': 'Leg', 'emoji': '🦵'}, {'palavra': 'Nose', 'emoji': '👃'},
        {'palavra': 'Mouth', 'emoji': '👄'}, {'palavra': 'Ear', 'emoji': '👂'},
        {'palavra': 'Red', 'emoji': '🔴'}, {'palavra': 'Blue', 'emoji': '🔵'},
        {'palavra': 'Happy', 'emoji': '😄'}, {'palavra': 'Sad', 'emoji': '😢'},
        {'palavra': 'Play soccer', 'emoji': '⚽'}, {'palavra': 'Ride a bike', 'emoji': '🚲'},
        {'palavra': 'Basketball', 'emoji': '🏀'}, {'palavra': 'Chess game', 'emoji': '♟️'}
    ]
    itens_jogo = random.sample(vocabulario, 12)
    palavras = [item['palavra'] for item in itens_jogo]
    imagens = itens_jogo.copy()
    random.shuffle(palavras)
    random.shuffle(imagens)
    contexto = {'palavras': palavras, 'imagens': imagens}
    return render(request, 'ingles_drag_drop.html', contexto)

@login_required(login_url='/')
def ingles_frases(request):
    distratores = ['apple', 'book', 'car', 'blue', 'rain', 'house', 'spider', 'table', 'shoes', 'onion', 'happy', 'pencil', 'door', 'water', 'sun', 'moon', 'bird', 'lion', 'church', 'building', 'nose', 'ear', 'jacket', 'bus', 'red', 'tree', 'bike', 'sunny', 'cloudy', 'windy', 'hot', 'cold', 'rainy', 'warm']
    templates = [
        {'frase': 'Do you have a pet ______?', 'variacoes': [{'resposta': 'dog', 'emoji': '🐶'}, {'resposta': 'cat', 'emoji': '🐱'}, {'resposta': 'mouse', 'emoji': '🐭'}, {'resposta': 'fish', 'emoji': '🐟'}]},
        {'frase': 'My favorite fruit is ______.', 'variacoes': [{'resposta': 'apple', 'emoji': '🍎'}, {'resposta': 'banana', 'emoji': '🍌'}, {'resposta': 'pineapple', 'emoji': '🍍'}, {'resposta': 'mango', 'emoji': '🥭'}, {'resposta': 'orange', 'emoji': '🍊'}]},
        {'frase': 'The book is on the ______.', 'variacoes': [{'resposta': 'table', 'emoji': '/static/img/table.png', 'is_image': True}]},
        {'frase': 'He likes to play ______.', 'variacoes': [{'resposta': 'soccer', 'emoji': '⚽'}, {'resposta': 'basketball', 'emoji': '🏀'}, {'resposta': 'chess', 'emoji': '♟️'}]},
        {'frase': 'Are you going to the ______?', 'variacoes': [{'resposta': 'beach', 'emoji': '🏖️'}, {'resposta': 'church', 'emoji': '⛪'}, {'resposta': 'house', 'emoji': '🏠'}, {'resposta': 'school', 'emoji': '🏫'}]},
        {'frase': 'I like to ______ in the park.', 'variacoes': [{'resposta': 'ride a bike', 'emoji': '🚲'}, {'resposta': 'play soccer', 'emoji': '⚽'}, {'resposta': 'swim', 'emoji': '🏊'}, {'resposta': 'rollerblade', 'emoji': '🛼'}]},
        {'frase': 'The color of the sky is ______.', 'variacoes': [{'resposta': 'blue', 'emoji': '☁️'}]},
        {'frase': 'The ______ is yellow.', 'variacoes': [{'resposta': 'sun', 'emoji': '☀️'}, {'resposta': 'banana', 'emoji': '🍌'}]},
        {'frase': 'She is wearing a beautiful ______.', 'variacoes': [{'resposta': 'shirt', 'emoji': '👕'}, {'resposta': 'jacket', 'emoji': '🧥'}, {'resposta': 'hat', 'emoji': '🎩'}]},
        {'frase': 'The weather today is ______.', 'variacoes': [{'resposta': 'sunny', 'emoji': '☀️'}, {'resposta': 'cloudy', 'emoji': '☁️'}, {'resposta': 'windy', 'emoji': '🌬️'}, {'resposta': 'rainy', 'emoji': '🌧️'}]},
        {'frase': 'I need a jacket because it is very ______!', 'variacoes': [{'resposta': 'cold', 'emoji': '🥶'}, {'resposta': 'windy', 'emoji': '🌬️'}]},
        {'frase': 'Let\'s go to the beach! It is so ______ today.', 'variacoes': [{'resposta': 'hot', 'emoji': '🥵'}, {'resposta': 'warm', 'emoji': '😎'}, {'resposta': 'sunny', 'emoji': '☀️'}]}
    ]
    moldes_escolhidos = random.sample(templates, min(8, len(templates)))
    frases_geradas = []
    for molde in moldes_escolhidos:
        var_escolhida = random.choice(molde['variacoes'])
        resposta_certa = var_escolhida['resposta']
        opcoes_erradas = random.sample([d for d in distratores if d != resposta_certa], 3)
        opcoes_finais = opcoes_erradas + [resposta_certa]
        random.shuffle(opcoes_finais)
        frases_geradas.append({'frase': molde['frase'], 'resposta': resposta_certa, 'opcoes': opcoes_finais, 'emoji': var_escolhida['emoji']})
    contexto = {'frases_json': json.dumps(frases_geradas)}
    return render(request, 'ingles_frases.html', contexto)

# --- MÓDULO DE PORTUGUÊS ---
@login_required(login_url='/')
def portugues_ortografia(request):
    banco_palavras = [
        {'palavra': 'CA___ORRO', 'resposta': 'CH', 'opcoes': ['X', 'CH', 'SH']},
        {'palavra': 'PÁ___ARO', 'resposta': 'SS', 'opcoes': ['S', 'SS', 'Ç']},
        {'palavra': 'E___ELENTE', 'resposta': 'XC', 'opcoes': ['C', 'S', 'XC']},
        {'palavra': 'A___ÚCAR', 'resposta': 'Ç', 'opcoes': ['S', 'SS', 'Ç']},
        {'palavra': 'GIRA___OL', 'resposta': 'SS', 'opcoes': ['S', 'SS', 'Ç']},
        {'palavra': '___INÁSTICA', 'resposta': 'G', 'opcoes': ['G', 'J']},
        {'palavra': 'MA___ESTADE', 'resposta': 'J', 'opcoes': ['G', 'J']},
        {'palavra': 'FA___INA', 'resposta': 'X', 'opcoes': ['X', 'CH', 'S']},
        {'palavra': 'CENOU___A', 'resposta': 'R', 'opcoes': ['R', 'RR']},
        {'palavra': 'CA___O (automóvel)', 'resposta': 'RR', 'opcoes': ['R', 'RR']},
        {'palavra': '___ACARÉ', 'resposta': 'J', 'opcoes': ['G', 'J']},
        {'palavra': '___ÍCARA', 'resposta': 'X', 'opcoes': ['X', 'CH', 'SS']},
    ]
    itens_jogo = random.sample(banco_palavras, 10)
    for item in itens_jogo:
        random.shuffle(item['opcoes'])
    contexto = {'palavras_json': json.dumps(itens_jogo)}
    return render(request, 'portugues_ortografia.html', contexto)

@login_required(login_url='/')
def portugues_silaba(request):
    banco_palavras = [
        {'palavra': 'CAFÉ', 'resposta': 'Oxítona'},
        {'palavra': 'AMOR', 'resposta': 'Oxítona'},
        {'palavra': 'PORTUGUÊS', 'resposta': 'Oxítona'},
        {'palavra': 'COMPUTADOR', 'resposta': 'Oxítona'},
        {'palavra': 'FELIZ', 'resposta': 'Oxítona'},
        {'palavra': 'MENINO', 'resposta': 'Paroxítona'},
        {'palavra': 'MESA', 'resposta': 'Paroxítona'},
        {'palavra': 'LÁPIS', 'resposta': 'Paroxítona'},
        {'palavra': 'FÁCIL', 'resposta': 'Paroxítona'},
        {'palavra': 'JANELA', 'resposta': 'Paroxítona'},
        {'palavra': 'MÁGICO', 'resposta': 'Proparoxítona'},
        {'palavra': 'ÁRVORE', 'resposta': 'Proparoxítona'},
        {'palavra': 'LÂMPADA', 'resposta': 'Proparoxítona'},
        {'palavra': 'PÁSSARO', 'resposta': 'Proparoxítona'},
        {'palavra': 'MÉDICO', 'resposta': 'Proparoxítona'},
    ]
    itens_jogo = random.sample(banco_palavras, 10)
    contexto = {'palavras_json': json.dumps(itens_jogo)}
    return render(request, 'portugues_silaba.html', contexto)

@login_required(login_url='/')
def portugues_sinonimos(request):
    banco_pares = [
        {'palavra': 'RÁPIDO', 'oposto': 'LENTO'}, {'palavra': 'QUENTE', 'oposto': 'FRIO'},
        {'palavra': 'LONGE', 'oposto': 'PERTO'}, {'palavra': 'GRANDE', 'oposto': 'PEQUENO'},
        {'palavra': 'DIA', 'oposto': 'NOITE'}, {'palavra': 'BOM', 'oposto': 'MAU'},
        {'palavra': 'CLARO', 'oposto': 'ESCURO'}, {'palavra': 'CHEIO', 'oposto': 'VAZIO'},
        {'palavra': 'ALTO', 'oposto': 'BAIXO'}, {'palavra': 'FORTE', 'oposto': 'FRACO'},
        {'palavra': 'FELIZ', 'oposto': 'TRISTE'}, {'palavra': 'FÁCIL', 'oposto': 'DIFÍCIL'},
        {'palavra': 'GIGANTE', 'oposto': 'MINÚSCULO'}, {'palavra': 'BARULHO', 'oposto': 'SILÊNCIO'}
    ]
    itens_jogo = random.sample(banco_pares, 10)
    palavras_arrastar = itens_jogo.copy()
    palavras_alvo = itens_jogo.copy()
    random.shuffle(palavras_arrastar)
    random.shuffle(palavras_alvo)
    contexto = {'palavras_arrastar': palavras_arrastar, 'palavras_alvo': palavras_alvo}
    return render(request, 'portugues_sinonimos.html', contexto)

@login_required(login_url='/')
def portugues_silabas(request):
    banco_palavras = [
        {'palavra': 'LEGO', 'separacao': 'LE-GO', 'resposta': 2},
        {'palavra': 'FERRARI', 'separacao': 'FER-RA-RI', 'resposta': 3},
        {'palavra': 'MERCEDES', 'separacao': 'MER-CE-DES', 'resposta': 3},
        {'palavra': 'FUTEBOL', 'separacao': 'FU-TE-BOL', 'resposta': 3},
        {'palavra': 'CRAQUE', 'separacao': 'CRA-QUE', 'resposta': 2},
        {'palavra': 'ESCOLINHA', 'separacao': 'ES-CO-LI-NHA', 'resposta': 4},
        {'palavra': 'ESTAÇÃO', 'separacao': 'ES-TA-ÇÃO', 'resposta': 3},
        {'palavra': 'ESTATÍSTICA', 'separacao': 'ES-TA-TÍS-TI-CA', 'resposta': 5},
        {'palavra': 'MÉXICO', 'separacao': 'MÉ-XI-CO', 'resposta': 3},
        {'palavra': 'FILIPINAS', 'separacao': 'FI-LI-PI-NAS', 'resposta': 4},
        {'palavra': 'PRAIA', 'separacao': 'PRAI-A', 'resposta': 2},
        {'palavra': 'INVESTIMENTO', 'separacao': 'IN-VES-TI-MEN-TO', 'resposta': 5},
        {'palavra': 'PLANILHA', 'separacao': 'PLA-NI-LHA', 'resposta': 3},
        {'palavra': 'SOL', 'separacao': 'SOL', 'resposta': 1},
        {'palavra': 'MAR', 'separacao': 'MAR', 'resposta': 1}
    ]
    itens_jogo = random.sample(banco_palavras, 10)
    contexto = {'palavras_json': json.dumps(itens_jogo)}
    return render(request, 'portugues_silabas.html', contexto)