import json
import logging
import random
import secrets
import string
from collections import OrderedDict
from functools import wraps
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import RegistroJogada, BancoQuestao

logger = logging.getLogger(__name__)


def registro_view(request):
    """Tela de cadastro de um novo aluno."""
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip().lower()
        senha = request.POST.get('senha', '')

        if not nome or not email or not senha:
            return render(request, 'registro.html', {
                'erro': 'Preencha todos os campos.'
            })

        if User.objects.filter(username=email).exists():
            return render(request, 'registro.html', {
                'erro': 'Já existe um cadastro com este e-mail.'
            })

        User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
        return render(request, 'login.html', {
            'sucesso': 'Cadastro realizado com sucesso! Faça login para continuar.'
        })

    return render(request, 'registro.html')


def login_view(request):
    """
    Tela de login. Depois de logar:
    - se o aluno ainda não escolheu o ano nesta sessão -> tela de seleção de ano
    - se já escolheu -> vai direto pra Home
    """
    if request.method == 'POST':
        email = request.POST.get('usuario', '').strip().lower()
        senha = request.POST.get('senha', '')

        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            if request.session.get('ano_selecionado'):
                return redirect('home')
            return redirect('selecionar_ano')

        return render(request, 'login.html', {
            'erro': 'E-mail ou senha incorretos.'
        })

    return render(request, 'login.html')


def logout_view(request):
    logout(request)  # logout() do Django já limpa toda a sessão, incluindo o ano escolhido
    return redirect('login')


@login_required(login_url='/')
def selecionar_ano_view(request):
    """Tela onde o aluno escolhe entre 1º e 5º ano (Ensino Fundamental I)."""
    if request.method == 'POST':
        ano = request.POST.get('ano')
        if ano in ['1', '2', '3', '4', '5']:
            request.session['ano_selecionado'] = ano
            return redirect('home')

    return render(request, 'selecionar_ano.html')


@login_required(login_url='/')
def trocar_ano_view(request):
    """Permite o aluno voltar à tela de seleção de ano a qualquer momento."""
    request.session.pop('ano_selecionado', None)
    return redirect('selecionar_ano')


@login_required(login_url='/')
def home_view(request):
    """Home de verdade: cards das disciplinas + informações do aluno."""
    if not request.session.get('ano_selecionado'):
        return redirect('selecionar_ano')

    contexto = {
        'nome_aluno': request.user.first_name or request.user.username,
        'ano_selecionado': request.session.get('ano_selecionado'),
    }
    return render(request, 'home.html', contexto)


@login_required(login_url='/')
def em_breve_view(request):
    """
    Placeholder temporário: os cards das disciplinas apontam pra cá até
    construirmos cada uma delas de verdade (Passo 5 em diante). Existe de
    propósito para NUNCA termos um link morto ('#') no meio do caminho.
    """
    materia = request.GET.get('materia', 'Esta seção')
    return render(request, 'em_breve.html', {'materia': materia})


# ─────────────────────────────────────────────
# PORTUGUÊS — 5 módulos (quiz genérico reaproveitado)
# ─────────────────────────────────────────────

MODULOS_PORTUGUES = {
    'ortografia': ('Ortografia', '✏️'),
    'sinonimos_antonimos': ('Sinônimos e Antônimos', '🔄'),
    'encontros_vocalicos': ('Encontros Vocálicos', '🔤'),
    'digrafos': ('Dígrafos', '🔠'),
    'classificacao_silabica': ('Classificação Silábica', '🎵'),
    'encontros_consonantais': ('Encontros Consonantais', '🔗'),
    'substantivos_adjetivos': ('Substantivos e Adjetivos', '🏷️'),
    'tipos_de_frase': ('Tipos de Frase', '💬'),
    'tempos_verbais': ('Tempos Verbais', '⏰'),
    'substantivos_singular_plural': ('Singular e Plural', '🔢'),
    'artigos': ('Artigos', '🔖'),
}


@login_required(login_url='/')
def menu_portugues(request):
    """Tela com os 5 módulos de Português."""
    return render(request, 'menu_portugues.html')


@login_required(login_url='/')
def portugues_quiz(request, modulo):
    """
    Quiz genérico, reaproveitado pelos 5 módulos de Português — todos
    usam o mesmo formato {pergunta, resposta, opcoes} no BancoQuestao,
    então uma view só resolve todos.
    """
    nome_modulo, icone_modulo = MODULOS_PORTUGUES.get(modulo, (modulo.title(), '📚'))

    todas = list(
        BancoQuestao.objects.filter(disciplina__nome='portugues', modulo=modulo, ativo=True)
        .values('enunciado', 'resposta_correta', 'dados_extras')
    )
    banco = [
        {'pergunta': q['enunciado'], 'resposta': q['resposta_correta'], 'opcoes': list(q['dados_extras'].get('opcoes', []))}
        for q in todas
    ]
    itens_jogo = random.sample(banco, min(10, len(banco)))
    for item in itens_jogo:
        random.shuffle(item['opcoes'])

    return render(request, 'portugues_quiz.html', {
        'questoes_json': json.dumps(itens_jogo),
        'modulo': modulo,
        'nome_modulo': nome_modulo,
        'icone_modulo': icone_modulo,
    })


# ─────────────────────────────────────────────
# GEOGRAFIA — 5 módulos (mesmo padrão genérico de Português)
# ─────────────────────────────────────────────

MODULOS_GEOGRAFIA = {
    'extrativismo': ('Extrativismo', '🌳'),
    'regioes_brasil': ('Regiões do Brasil', '🗺️'),
    'agricultura': ('Agricultura', '🌾'),
    'pecuaria': ('Pecuária', '🐄'),
    'paisagem': ('Paisagem', '🏞️'),
    'setores_economia': ('Setores da Economia', '🏙️'),
}


@login_required(login_url='/')
def menu_geografia(request):
    """Tela com os 5 módulos de Geografia."""
    return render(request, 'menu_geografia.html')


@login_required(login_url='/')
def geografia_quiz(request, modulo):
    """Quiz genérico, reaproveitado pelos 5 módulos de Geografia."""
    nome_modulo, icone_modulo = MODULOS_GEOGRAFIA.get(modulo, (modulo.title(), '🌎'))

    todas = list(
        BancoQuestao.objects.filter(disciplina__nome='geografia', modulo=modulo, ativo=True)
        .values('enunciado', 'resposta_correta', 'dados_extras')
    )
    banco = [
        {'pergunta': q['enunciado'], 'resposta': q['resposta_correta'], 'opcoes': list(q['dados_extras'].get('opcoes', []))}
        for q in todas
    ]
    itens_jogo = random.sample(banco, min(10, len(banco)))
    for item in itens_jogo:
        random.shuffle(item['opcoes'])

    return render(request, 'geografia_quiz.html', {
        'questoes_json': json.dumps(itens_jogo),
        'modulo': modulo,
        'nome_modulo': nome_modulo,
        'icone_modulo': icone_modulo,
    })


# ─────────────────────────────────────────────
# INGLÊS — 4 módulos (mesmo padrão genérico)
# ─────────────────────────────────────────────

MODULOS_INGLES = {
    'weather_clothes': ('Weather & Clothes', '☀️'),
    'atividades_like': ('Atividades', '🏃'),
    'vocabulario_geral': ('Vocabulário Geral', '📖'),
    'esportes_convites': ('Esportes e Convites', '⚽'),
    'vocabulario_visual': ('Vocabulário Visual', '🖼️'),
    'casa_comodos': ('Rooms in the House', '🏠'),
    'science_vertebrates_invertebrates': ('Vertebrates x Invertebrates', '🦴'),
    'science_oviparous_viviparous': ('Oviparous x Viviparous', '🥚'),
    'science_habitats': ('Animal Habitats', '🌍'),
    'science_eating_habits': ('Eating Habits', '🍽️'),
}


@login_required(login_url='/')
def menu_ingles(request):
    """Tela com os 4 módulos de Inglês."""
    return render(request, 'menu_ingles.html')


@login_required(login_url='/')
def ingles_quiz(request, modulo):
    """Quiz genérico, reaproveitado pelos 4 módulos de Inglês."""
    nome_modulo, icone_modulo = MODULOS_INGLES.get(modulo, (modulo.title(), '🇬🇧'))

    todas = list(
        BancoQuestao.objects.filter(disciplina__nome='ingles', modulo=modulo, ativo=True)
        .values('enunciado', 'resposta_correta', 'dados_extras')
    )
    banco = [
        {'pergunta': q['enunciado'], 'resposta': q['resposta_correta'], 'opcoes': list(q['dados_extras'].get('opcoes', []))}
        for q in todas
    ]
    itens_jogo = random.sample(banco, min(10, len(banco)))
    for item in itens_jogo:
        random.shuffle(item['opcoes'])

    return render(request, 'ingles_quiz.html', {
        'questoes_json': json.dumps(itens_jogo),
        'modulo': modulo,
        'nome_modulo': nome_modulo,
        'icone_modulo': icone_modulo,
    })


@login_required(login_url='/')
def menu_ingles_science(request):
    """
    Sub-hub 'Science' dentro de Inglês: 4 quizzes (usam ingles_quiz,
    sem view própria) + 4 jogos de colmeia temáticos (usam a view
    ingles_science_hive_view abaixo).
    """
    return render(request, 'menu_ingles_science.html')


# Cada tema tem um "pool" de pares (emoji do animal, rótulo em inglês
# único). O rótulo já inclui a classificação (ex: "Lion – Vertebrate"),
# assim cada par tem um texto único — evita a ambiguidade de ter duas
# células iguais na tela (o mesmo problema que corrigimos na Colmeia da
# Multiplicação, aqui resolvido de outra forma: nome do animal + categoria).
TEMAS_SCIENCE_HIVE = {
    'vertebrates-invertebrates': {
        'nome': 'Vertebrates x Invertebrates',
        'icone': '🦴',
        'pares': [
            ('🦁', 'Lion – Vertebrate'), ('🐍', 'Snake – Vertebrate'), ('🐸', 'Frog – Vertebrate'),
            ('🐦', 'Bird – Vertebrate'), ('🐟', 'Fish – Vertebrate'), ('🐢', 'Turtle – Vertebrate'),
            ('🐝', 'Bee – Invertebrate'), ('🕷️', 'Spider – Invertebrate'), ('🐌', 'Snail – Invertebrate'),
            ('🦀', 'Crab – Invertebrate'), ('🐙', 'Octopus – Invertebrate'), ('🦋', 'Butterfly – Invertebrate'),
        ],
    },
    'oviparous-viviparous': {
        'nome': 'Oviparous x Viviparous',
        'icone': '🥚',
        'pares': [
            ('🐔', 'Chicken – Oviparous'), ('🐢', 'Turtle – Oviparous'), ('🦎', 'Lizard – Oviparous'),
            ('🐸', 'Frog – Oviparous'), ('🦆', 'Duck – Oviparous'), ('🦉', 'Owl – Oviparous'),
            ('🐶', 'Dog – Viviparous'), ('🐱', 'Cat – Viviparous'), ('🐮', 'Cow – Viviparous'),
            ('🐴', 'Horse – Viviparous'), ('🐷', 'Pig – Viviparous'), ('🐑', 'Sheep – Viviparous'),
        ],
    },
    'habitats': {
        'nome': 'Animal Habitats',
        'icone': '🌍',
        'pares': [
            ('🐟', 'Fish – Aquatic'), ('🐬', 'Dolphin – Aquatic'), ('🦈', 'Shark – Aquatic'),
            ('🦁', 'Lion – Terrestrial'), ('🐘', 'Elephant – Terrestrial'), ('🐴', 'Horse – Terrestrial'),
            ('🦅', 'Eagle – Aerial'), ('🦋', 'Butterfly – Aerial'), ('🐝', 'Bee – Aerial'),
            ('🐒', 'Monkey – Arboreal'), ('🦥', 'Sloth – Arboreal'), ('🦜', 'Parrot – Arboreal'),
        ],
    },
    'eating-habits': {
        'nome': 'Eating Habits',
        'icone': '🍽️',
        'pares': [
            ('🦁', 'Lion – Carnivore'), ('🐺', 'Wolf – Carnivore'), ('🦈', 'Shark – Carnivore'),
            ('🐰', 'Rabbit – Herbivore'), ('🐄', 'Cow – Herbivore'), ('🦒', 'Giraffe – Herbivore'),
            ('🐻', 'Bear – Omnivore'), ('🐷', 'Pig – Omnivore'), ('🐔', 'Chicken – Omnivore'),
        ],
    },
}


@login_required(login_url='/')
def ingles_science_hive_view(request, tema):
    """
    Jogo de colmeia genérico, reaproveitado pelos 4 temas de Science em
    Inglês (mesma mecânica da Colmeia da Multiplicação: clica no bicho,
    depois no rótulo certo, os dois ficam da mesma cor).
    """
    config = TEMAS_SCIENCE_HIVE.get(tema)
    if config is None:
        return redirect('menu_ingles_science')

    pool = config['pares']
    pares_sorteados = random.sample(pool, min(8, len(pool)))
    pares_formatados = [{'esquerda': emoji, 'direita': rotulo} for emoji, rotulo in pares_sorteados]

    return render(request, 'colmeia_science.html', {
        'pares_json': json.dumps(pares_formatados),
        'tema': tema,
        'nome_tema': config['nome'],
        'icone_tema': config['icone'],
    })


# ─────────────────────────────────────────────
# CIÊNCIAS — 5 módulos (mesmo padrão genérico)
# ─────────────────────────────────────────────

MODULOS_CIENCIAS = {
    'plantas': ('Plantas', '🌱'),
    'sons': ('Sons', '🔊'),
    'solo': ('Solo', '🪨'),
    'petroleo': ('Petróleo', '🛢️'),
    'sistema_solar': ('Sistema Solar', '🪐'),
    'diversidade_modos_vida': ('Diversidade de Modos de Vida', '🐾'),
    'vertebrados_invertebrados': ('Vertebrados e Invertebrados', '🦴'),
}


@login_required(login_url='/')
def menu_ciencias(request):
    """Tela com os 5 módulos de Ciências."""
    return render(request, 'menu_ciencias.html')


@login_required(login_url='/')
def ciencias_quiz(request, modulo):
    """Quiz genérico, reaproveitado pelos 5 módulos de Ciências."""
    nome_modulo, icone_modulo = MODULOS_CIENCIAS.get(modulo, (modulo.title(), '🔬'))

    todas = list(
        BancoQuestao.objects.filter(disciplina__nome='ciencias', modulo=modulo, ativo=True)
        .values('enunciado', 'resposta_correta', 'dados_extras')
    )
    banco = [
        {'pergunta': q['enunciado'], 'resposta': q['resposta_correta'], 'opcoes': list(q['dados_extras'].get('opcoes', []))}
        for q in todas
    ]
    itens_jogo = random.sample(banco, min(10, len(banco)))
    for item in itens_jogo:
        random.shuffle(item['opcoes'])

    return render(request, 'ciencias_quiz.html', {
        'questoes_json': json.dumps(itens_jogo),
        'modulo': modulo,
        'nome_modulo': nome_modulo,
        'icone_modulo': icone_modulo,
    })


# ─────────────────────────────────────────────
# HISTÓRIA — 5 módulos (mesmo padrão genérico)
# ─────────────────────────────────────────────

MODULOS_HISTORIA = {
    'primeiras_vilas': ('Primeiras Vilas do Brasil', '🏘️'),
    'ciclo_do_ouro': ('Ciclo do Ouro', '⛏️'),
    'capitais_brasil': ('Capitais do Brasil', '🏙️'),
    'crescimento_cidades': ('Crescimento das Cidades', '🏭'),
    'cidadania': ('Cidadania', '⚖️'),
    'cultura_brasileira': ('Cultura Brasileira', '🎭'),
}


@login_required(login_url='/')
def menu_historia(request):
    """Tela com os 5 módulos de História."""
    return render(request, 'menu_historia.html')


@login_required(login_url='/')
def historia_quiz(request, modulo):
    """Quiz genérico, reaproveitado pelos 5 módulos de História."""
    nome_modulo, icone_modulo = MODULOS_HISTORIA.get(modulo, (modulo.title(), '🏛️'))

    todas = list(
        BancoQuestao.objects.filter(disciplina__nome='historia', modulo=modulo, ativo=True)
        .values('enunciado', 'resposta_correta', 'dados_extras')
    )
    banco = [
        {'pergunta': q['enunciado'], 'resposta': q['resposta_correta'], 'opcoes': list(q['dados_extras'].get('opcoes', []))}
        for q in todas
    ]
    itens_jogo = random.sample(banco, min(10, len(banco)))
    for item in itens_jogo:
        random.shuffle(item['opcoes'])

    return render(request, 'historia_quiz.html', {
        'questoes_json': json.dumps(itens_jogo),
        'modulo': modulo,
        'nome_modulo': nome_modulo,
        'icone_modulo': icone_modulo,
    })


# ─────────────────────────────────────────────
# MATEMÁTICA — MENU DE OPERAÇÕES (completo: 6 operações)
# ─────────────────────────────────────────────

NOMES_OPERACOES_MATEMATICA = {
    'adicao': ('Adição', '➕'),
    'subtracao': ('Subtração', '➖'),
    'multiplicacao': ('Multiplicação', '✖️'),
    'divisao': ('Divisão', '➗'),
    'potenciacao': ('Potenciação', '🔺'),
    'radiciacao': ('Radiciação', '√'),
}


@login_required(login_url='/')
def menu_matematica(request):
    """
    Hub de Matemática: por enquanto tem 2 frentes — Operações (as 4
    operações + potenciação/radiciação) e Sistema de Numeração (quiz
    baseado nas provas). Cada uma pode crescer de forma independente.
    """
    return render(request, 'menu_matematica.html')


@login_required(login_url='/')
def menu_operacoes(request):
    """Tela com as 6 operações. Radiciação vai direto pro jogo (só tem 1 nível)."""
    return render(request, 'menu_operacoes.html')


@login_required(login_url='/')
def numeracao_quiz(request):
    """
    Quiz de Sistema de Numeração (valor posicional, sucessor/antecessor,
    decomposição, comparação, escrita por extenso etc.), usando o banco
    de questões (BancoQuestao) populado a partir da prova real.
    """
    todas = list(
        BancoQuestao.objects.filter(disciplina__nome='matematica', modulo='sistema_numeracao', ativo=True)
        .values('enunciado', 'resposta_correta', 'dados_extras')
    )
    banco = [
        {'pergunta': q['enunciado'], 'resposta': q['resposta_correta'], 'opcoes': list(q['dados_extras'].get('opcoes', []))}
        for q in todas
    ]
    itens_jogo = random.sample(banco, min(10, len(banco)))
    for item in itens_jogo:
        random.shuffle(item['opcoes'])
    return render(request, 'numeracao_quiz.html', {'questoes_json': json.dumps(itens_jogo)})


@login_required(login_url='/')
def desafios_calculo_quiz(request):
    """
    Quiz de Desafios de Cálculo (expressões numéricas, cálculo mental,
    multiplicação/divisão armada, valor posicional, situações-problema),
    usando o banco de questões (BancoQuestao) populado a partir das
    provas reais de matemática. Mesmo formato do numeracao_quiz, só que
    numa rota própria — sem mexer no que já existia.
    """
    todas = list(
        BancoQuestao.objects.filter(disciplina__nome='matematica', modulo='desafios_calculo', ativo=True)
        .values('enunciado', 'resposta_correta', 'dados_extras')
    )
    banco = [
        {'pergunta': q['enunciado'], 'resposta': q['resposta_correta'], 'opcoes': list(q['dados_extras'].get('opcoes', []))}
        for q in todas
    ]
    itens_jogo = random.sample(banco, min(10, len(banco)))
    for item in itens_jogo:
        random.shuffle(item['opcoes'])
    return render(request, 'desafios_calculo_quiz.html', {'questoes_json': json.dumps(itens_jogo)})


@login_required(login_url='/')
def tabuada_6_a_9_quiz(request):
    """
    Quiz de Tabuada do 6 ao 9, usando o banco de questões (BancoQuestao)
    — diferente da tabuada de 'Operações Matemáticas' (que sorteia os
    números na hora, em JavaScript, sem nunca gravar a pergunta), aqui
    as perguntas ficam salvas de verdade, o que permite elas entrarem
    também na Prova Multidisciplinar.
    """
    todas = list(
        BancoQuestao.objects.filter(disciplina__nome='matematica', modulo='tabuada_6_a_9', ativo=True)
        .values('enunciado', 'resposta_correta', 'dados_extras')
    )
    banco = [
        {'pergunta': q['enunciado'], 'resposta': q['resposta_correta'], 'opcoes': list(q['dados_extras'].get('opcoes', []))}
        for q in todas
    ]
    itens_jogo = random.sample(banco, min(10, len(banco)))
    for item in itens_jogo:
        random.shuffle(item['opcoes'])
    return render(request, 'tabuada_6_a_9_quiz.html', {'questoes_json': json.dumps(itens_jogo)})


@login_required(login_url='/')
def colmeia_multiplicacao_view(request):
    """
    Jogo 'Colmeia da Multiplicação': o aluno associa cada conta de
    multiplicação (ex: 7 x 8) ao seu resultado correto (56), e as duas
    células ficam coloridas com a mesma cor ao acertar — inspirado na
    folha de atividade em papel, só que interativo.

    Sorteia pares novos a cada partida, na tabuada de 0 a 12, sem
    produtos repetidos (senão duas contas diferentes poderiam "casar"
    com a mesma célula de resultado).
    """
    pares = []
    produtos_usados = set()
    pares_usados = set()
    tentativas = 0
    while len(pares) < 8 and tentativas < 500:
        tentativas += 1
        a = random.randint(0, 12)
        b = random.randint(1, 12)
        produto = a * b
        if produto in produtos_usados or (a, b) in pares_usados:
            continue
        produtos_usados.add(produto)
        pares_usados.add((a, b))
        pares.append({'a': a, 'b': b, 'produto': produto})

    return render(request, 'colmeia.html', {'pares_json': json.dumps(pares)})


@login_required(login_url='/')
def niveis_operacao(request, operacao):
    """
    Tela de escolha de nível. Adição/Subtração/Multiplicação/Divisão têm
    3 níveis (unidades/dezenas/centenas); Potenciação tem outros 3
    (quadrados/cubos/potências). Radiciação não usa esta tela.
    """
    if operacao == 'potenciacao':
        niveis = [
            ('quadrados', 'Quadrados (n²)'),
            ('cubos', 'Cubos (n³)'),
            ('potencias', 'Potências (n⁴ e n⁵)'),
        ]
    else:
        niveis = [
            ('unidades', 'Unidades'),
            ('dezenas', 'Dezenas'),
            ('centenas', 'Centenas'),
        ]

    nome, icone = NOMES_OPERACOES_MATEMATICA.get(operacao, (operacao.title(), '🧮'))
    return render(request, 'niveis_operacao.html', {
        'operacao': operacao,
        'nome_operacao': nome,
        'icone_operacao': icone,
        'niveis': niveis,
    })


@login_required(login_url='/')
def jogo_tabuada(request, operacao, nivel):
    """
    Tela do jogo em si. Os números são sorteados no JavaScript (não
    precisam de banco de dados) de acordo com a operação e o nível.
    """
    nome, icone = NOMES_OPERACOES_MATEMATICA.get(operacao, (operacao.title(), '🧮'))
    return render(request, 'jogo.html', {
        'operacao': operacao,
        'nivel': nivel,
        'nome_operacao': nome,
    })


@csrf_exempt
def salvar_jogada(request):
    """
    Endpoint chamado pelo JavaScript do jogo a cada resposta do aluno.
    Sempre exige sessão autenticada — se não houver, recusa com um erro
    claro (em vez de salvar silenciosamente sem dono, como acontecia no
    projeto antigo e fazia sumir dados do relatório).
    """
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)

            if not request.user.is_authenticated:
                logger.warning(
                    "salvar_jogada recebida sem usuário autenticado. Dados: %s", dados
                )
                return JsonResponse({
                    'status': 'erro',
                    'mensagem': 'Sessão expirada. Faça login novamente para salvar seu progresso.'
                }, status=401)

            RegistroJogada.objects.create(
                jogador=request.user,
                operacao=dados.get('operacao', 'multiplicacao'),
                nivel=dados.get('nivel', 'unidades'),
                numero_1=dados.get('numero_1', 0),
                numero_2=dados.get('numero_2', 0),
                resposta_aluno=dados.get('resposta_aluno', '0'),
                acertou=dados.get('acertou', True),
                tempo_segundos=dados.get('tempo_segundos', 0),
            )
            return JsonResponse({'status': 'sucesso'})
        except Exception as e:
            logger.exception("Falha ao salvar jogada: %s", e)
            return JsonResponse({'status': 'erro', 'mensagem': str(e)}, status=400)

    return JsonResponse({'status': 'metodo_invalido'}, status=405)


def montar_estatisticas_aluno(usuario):
    """
    Monta o relatório de desempenho de UM aluno, agrupado por matéria,
    na ordem: Matemática, Português, Inglês, Ciências, Geografia, História.
    Reaproveitada tanto pelo "Meu Relatório" quanto pelo Painel do Professor.
    """
    jogadas_todas = RegistroJogada.objects.filter(jogador=usuario)
    total_geral = jogadas_todas.count()

    materias = OrderedDict([
        ('Matemática', []), ('Português', []), ('Inglês', []),
        ('Ciências', []), ('Geografia', []), ('História', []),
        ('Prova Multidisciplinar', []),
    ])

    def _adicionar(materia, nome, icone, jogadas_filtradas):
        if jogadas_filtradas.count() > 0:
            acertos = jogadas_filtradas.filter(acertou=True).count()
            tempo_medio = jogadas_filtradas.aggregate(Avg('tempo_segundos'))['tempo_segundos__avg']
            materias[materia].append({
                'nome': nome, 'icone': icone,
                'total': jogadas_filtradas.count(), 'acertos': acertos,
                'erros': jogadas_filtradas.count() - acertos,
                'taxa_acerto': round((acertos / jogadas_filtradas.count()) * 100, 1),
                'tempo_medio': round(tempo_medio, 1) if tempo_medio else 0,
            })

    # Matemática: 6 operações + Sistema de Numeração
    for op_id, (nome, icone) in NOMES_OPERACOES_MATEMATICA.items():
        _adicionar('Matemática', nome, icone, jogadas_todas.filter(operacao=op_id))
    _adicionar('Matemática', 'Sistema de Numeração', '🔢',
               jogadas_todas.filter(operacao='matematica_numeracao', nivel='numeracao_questao'))
    _adicionar('Matemática', 'Desafios de Cálculo', '🧠',
               jogadas_todas.filter(operacao='matematica_desafios_calculo', nivel='desafios_calculo_questao'))
    _adicionar('Matemática', 'Tabuada do 6 ao 9', '✖️',
               jogadas_todas.filter(operacao='matematica_tabuada_6_a_9', nivel='tabuada_6_a_9_questao'))
    _adicionar('Matemática', 'Colmeia da Multiplicação', '🐝',
               jogadas_todas.filter(operacao='matematica_colmeia', nivel='colmeia_par'))

    # Português, Inglês, Ciências, Geografia, História: módulos de quiz
    for materia, modulos, prefixo in [
        ('Português', MODULOS_PORTUGUES, 'portugues'),
        ('Inglês', MODULOS_INGLES, 'ingles'),
        ('Ciências', MODULOS_CIENCIAS, 'ciencias'),
        ('Geografia', MODULOS_GEOGRAFIA, 'geografia'),
        ('História', MODULOS_HISTORIA, 'historia'),
    ]:
        for modulo_id, (nome_modulo, icone_modulo) in modulos.items():
            _adicionar(materia, nome_modulo, icone_modulo,
                       jogadas_todas.filter(operacao=f'{prefixo}_{modulo_id}', nivel=f'{modulo_id}_questao'))

    # Inglês › Science: as 4 colmeias temáticas (não usam o padrão genérico
    # acima porque a "operacao" delas é dinâmica por tema, não por módulo).
    for tema_id, config in TEMAS_SCIENCE_HIVE.items():
        _adicionar('Inglês', f"{config['nome']} Hive", '🐝',
                   jogadas_todas.filter(operacao=f'ingles_science_hive_{tema_id}', nivel='science_hive_par'))

    # Prova Multidisciplinar: como cada prova mistura várias matérias, ela
    # entra como uma frente própria no relatório, sem detalhar por matéria.
    _adicionar('Prova Multidisciplinar', 'Provas Realizadas', '📝',
               jogadas_todas.filter(operacao='prova_multidisciplinar', nivel='prova_questao'))

    return materias, total_geral


# ─────────────────────────────────────────────
# RANKING GERAL — pontuação com peso por matéria
# ─────────────────────────────────────────────

PESO_MATERIA = {
    'Matemática': 1.5,
    'Português': 1.5,
    'Inglês': 1.5,
    'Ciências': 1.0,
    'Geografia': 1.0,
    'História': 1.0,
}


def _materia_da_jogada(operacao):
    """
    Descobre a matéria de uma jogada a partir do campo 'operacao' do
    RegistroJogada. As 6 operações de cálculo puro (adição, subtração
    etc.) não têm prefixo — são um caso especial de Matemática.
    """
    if operacao in NOMES_OPERACOES_MATEMATICA:
        return 'Matemática'
    prefixos = {
        'matematica_': 'Matemática',
        'portugues_': 'Português',
        'ingles_': 'Inglês',
        'ciencias_': 'Ciências',
        'geografia_': 'Geografia',
        'historia_': 'História',
    }
    for prefixo, materia in prefixos.items():
        if operacao.startswith(prefixo):
            return materia
    return None  # não deveria acontecer, mas por segurança


@login_required(login_url='/')
def ranking_view(request):
    """
    Ranking geral entre os alunos: cada acerto soma o peso da matéria em
    pontos, cada erro subtrai o mesmo peso (Matemática, Português e
    Inglês valem 1,5; as demais matérias valem 1).

    TOP_N controla quantos alunos aparecem na lista — pra mostrar Top 20
    ou Top 30 em vez de Top 10, só trocar o número abaixo.
    """
    TOP_N = 10

    jogadas = RegistroJogada.objects.filter(jogador__is_staff=False).values(
        'jogador_id', 'jogador__first_name', 'jogador__username', 'operacao', 'acertou'
    )

    pontos_por_aluno = {}
    nomes_por_aluno = {}
    for j in jogadas:
        materia = _materia_da_jogada(j['operacao'])
        peso = PESO_MATERIA.get(materia, 1.0)
        delta = peso if j['acertou'] else -peso
        aluno_id = j['jogador_id']
        pontos_por_aluno[aluno_id] = pontos_por_aluno.get(aluno_id, 0.0) + delta
        nomes_por_aluno[aluno_id] = j['jogador__first_name'] or j['jogador__username']

    lista_completa = sorted(
        (
            {'aluno_id': aid, 'nome': nomes_por_aluno[aid], 'pontos': round(pontos, 1)}
            for aid, pontos in pontos_por_aluno.items()
        ),
        key=lambda item: item['pontos'], reverse=True
    )

    ranking_top = [
        {'posicao': i + 1, 'nome': item['nome'], 'pontos': item['pontos']}
        for i, item in enumerate(lista_completa[:TOP_N])
    ]

    minha_posicao = None
    for i, item in enumerate(lista_completa):
        if item['aluno_id'] == request.user.id:
            minha_posicao = {'posicao': i + 1, 'pontos': item['pontos']}
            break

    return render(request, 'ranking.html', {
        'ranking': ranking_top,
        'top_n': TOP_N,
        'minha_posicao': minha_posicao,
        'dentro_do_top': minha_posicao is not None and minha_posicao['posicao'] <= TOP_N,
    })


# ─────────────────────────────────────────────
# PROVA MULTIDISCIPLINAR
# ─────────────────────────────────────────────

# Matemática não tem um MODULOS_MATEMATICA como as outras matérias (cada
# frente dela tem sua própria view dedicada), então criamos aqui só a
# lista dos módulos que TÊM perguntas salvas no banco (as 6 operações
# básicas não têm — são geradas na hora, em JavaScript, então não podem
# entrar na prova).
MODULOS_MATEMATICA_BANCO = {
    'sistema_numeracao': ('Sistema de Numeração', '🔢'),
    'desafios_calculo': ('Desafios de Cálculo', '🧠'),
    'tabuada_6_a_9': ('Tabuada do 6 ao 9', '✖️'),
}

# Catálogo geral: toda matéria/módulo que tem perguntas no BancoQuestao
# pode entrar na Prova Multidisciplinar. 'disciplina_bd' é o nome salvo
# no campo Disciplina.nome (pode ser diferente da chave usada aqui).
PROVA_CATALOGO = {
    'matematica': {'nome': 'Matemática', 'icone': '🧮', 'disciplina_bd': 'matematica', 'modulos': MODULOS_MATEMATICA_BANCO},
    'portugues': {'nome': 'Português', 'icone': '📚', 'disciplina_bd': 'portugues', 'modulos': MODULOS_PORTUGUES},
    'ciencias': {'nome': 'Ciências', 'icone': '🔬', 'disciplina_bd': 'ciencias', 'modulos': MODULOS_CIENCIAS},
    'geografia': {'nome': 'Geografia', 'icone': '🌎', 'disciplina_bd': 'geografia', 'modulos': MODULOS_GEOGRAFIA},
    'historia': {'nome': 'História', 'icone': '🏛️', 'disciplina_bd': 'historia', 'modulos': MODULOS_HISTORIA},
    'ingles': {'nome': 'Inglês', 'icone': '🇬🇧', 'disciplina_bd': 'ingles', 'modulos': MODULOS_INGLES},
}


def _montar_catalogo_com_contagem():
    """
    Monta o catálogo da Prova Multidisciplinar já com a quantidade de
    questões disponíveis em cada assunto (pra mostrar na tela e pra
    limitar quanto o aluno/professor pode pedir de cada um).
    """
    catalogo = OrderedDict()
    for materia_id, config in PROVA_CATALOGO.items():
        modulos_lista = []
        for modulo_id, (nome_modulo, icone_modulo) in config['modulos'].items():
            total = BancoQuestao.objects.filter(
                disciplina__nome=config['disciplina_bd'], modulo=modulo_id, ativo=True
            ).count()
            modulos_lista.append({
                'id': modulo_id, 'nome': nome_modulo, 'icone': icone_modulo, 'total_disponivel': total,
            })
        catalogo[materia_id] = {'nome': config['nome'], 'icone': config['icone'], 'modulos': modulos_lista}
    return catalogo


@login_required(login_url='/')
def prova_config_view(request):
    """Tela onde o aluno/professor escolhe QUANTAS questões de CADA assunto entram na prova."""
    return render(request, 'prova_config.html', {'catalogo': _montar_catalogo_com_contagem()})


@login_required(login_url='/')
def prova_gerar_view(request):
    """
    Monta a Prova Multidisciplinar: para cada assunto, pega exatamente a
    quantidade de questões pedida (campo 'qtd__<materia>__<modulo>' no
    formulário), sorteando quais delas entram. Cada questão é reduzida
    de 4 para 3 alternativas (a certa + 2 erradas sorteadas).
    """
    if request.method != 'POST':
        return redirect('prova_config')

    itens_prova = []

    for chave, valor in request.POST.items():
        if not chave.startswith('qtd__'):
            continue
        try:
            _, materia_id, modulo_id = chave.split('__', 2)
            quantidade_pedida = int(valor)
        except ValueError:
            continue
        if quantidade_pedida <= 0:
            continue

        config_materia = PROVA_CATALOGO.get(materia_id)
        if not config_materia or modulo_id not in config_materia['modulos']:
            continue  # ignora valores inesperados (ex: formulário adulterado)

        questoes = list(BancoQuestao.objects.filter(
            disciplina__nome=config_materia['disciplina_bd'], modulo=modulo_id, ativo=True
        ).values('enunciado', 'resposta_correta', 'dados_extras'))

        quantidade_final = min(quantidade_pedida, len(questoes))
        selecionadas = random.sample(questoes, quantidade_final)

        for q in selecionadas:
            opcoes_originais = list(q['dados_extras'].get('opcoes', []))
            erradas = [o for o in opcoes_originais if o != q['resposta_correta']]
            if len(erradas) < 2:
                continue  # segurança: precisa de pelo menos 2 opções erradas pra formar 3 alternativas
            opcoes_prova = random.sample(erradas, 2) + [q['resposta_correta']]
            random.shuffle(opcoes_prova)
            itens_prova.append({
                'pergunta': q['enunciado'],
                'resposta': q['resposta_correta'],
                'opcoes': opcoes_prova,
                'materia': config_materia['nome'],
            })

    if not itens_prova:
        return render(request, 'prova_config.html', {
            'catalogo': _montar_catalogo_com_contagem(),
            'erro': 'Nenhuma questão foi selecionada. Digite uma quantidade maior que zero em pelo menos um assunto.',
        })

    random.shuffle(itens_prova)  # embaralha a ordem das matérias na prova

    return render(request, 'prova_quiz.html', {
        'questoes_json': json.dumps(itens_prova),
    })


@login_required(login_url='/')
def relatorio_view(request):
    """Tela 'Meu Relatório' — o próprio aluno vendo seu desempenho."""
    materias, total_geral = montar_estatisticas_aluno(request.user)
    return render(request, 'relatorio.html', {
        'materias': materias,
        'total_geral': total_geral,
        'nome_aluno': None,  # None = é o próprio aluno vendo o relatório dele
    })


def professor_obrigatorio(view_func):
    """
    Decorator que só deixa passar usuários marcados como 'Equipe técnica'
    (is_staff) no Django Admin — é assim que definimos quem é professor.
    """
    @wraps(view_func)
    @login_required(login_url='/')
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper


@professor_obrigatorio
def painel_professor_view(request):
    """
    Painel do Professor: lista todos os alunos cadastrados, com um resumo
    rápido, e um link para o relatório completo de cada um. Qualquer
    usuário marcado como 'Equipe técnica' no admin pode acessar — dá pra
    ter vários professores com acesso ao mesmo tempo.
    """
    alunos = User.objects.filter(is_staff=False).order_by('first_name', 'username')
    lista_alunos = []
    for aluno in alunos:
        jogadas = RegistroJogada.objects.filter(jogador=aluno)
        total = jogadas.count()
        acertos = jogadas.filter(acertou=True).count()
        taxa = round((acertos / total) * 100, 1) if total > 0 else 0
        lista_alunos.append({
            'aluno': aluno,
            'nome': aluno.first_name or aluno.username,
            'total_jogadas': total,
            'taxa_acerto': taxa,
        })
    return render(request, 'painel_professor.html', {'lista_alunos': lista_alunos})


@professor_obrigatorio
def relatorio_aluno_view(request, aluno_id):
    """Relatório completo de UM aluno específico, visto pelo professor."""
    aluno = get_object_or_404(User, id=aluno_id)
    materias, total_geral = montar_estatisticas_aluno(aluno)
    return render(request, 'relatorio.html', {
        'materias': materias,
        'total_geral': total_geral,
        'nome_aluno': aluno.first_name or aluno.username,  # preenchido = professor vendo relatório de outro aluno
    })


@professor_obrigatorio
def excluir_aluno_view(request, aluno_id):
    """
    Exclui um aluno e TODAS as jogadas dele (apagar o usuário já apaga as
    jogadas juntas, por causa do 'on_delete=CASCADE' no modelo). Só aceita
    POST de propósito — assim um clique/link acidental (GET) nunca apaga
    ninguém; é preciso confirmar de verdade, através de um formulário.
    """
    aluno = get_object_or_404(User, id=aluno_id)

    if aluno.is_staff:
        # Proteção extra: nunca deixa apagar outro professor por engano
        # nem a si mesmo por aqui.
        return redirect('painel_professor')

    if request.method == 'POST':
        nome_removido = aluno.first_name or aluno.username
        aluno.delete()
        logger.info("Aluno excluído pelo professor %s: %s", request.user.username, nome_removido)
        return redirect('painel_professor')

    # Se alguém tentar acessar por GET (ex: digitando a URL direto),
    # só mostra a tela de confirmação, sem apagar nada ainda.
    return render(request, 'confirmar_exclusao.html', {'aluno': aluno})


def _gerar_senha_temporaria():
    """
    Gera uma senha temporária numérica de 6 dígitos, fácil de ler e
    repassar verbalmente a uma criança (ex: ao telefone ou em sala de
    aula). Usa o módulo 'secrets' (e não 'random') porque, mesmo sendo
    uma senha temporária, ela concede acesso à conta — 'secrets' é a
    escolha adequada do Python sempre que o valor gerado tem função de
    segurança/autenticação.
    """
    return ''.join(secrets.choice(string.digits) for _ in range(6))


@professor_obrigatorio
def redefinir_senha_aluno_view(request, aluno_id):
    """
    Permite ao professor gerar uma nova senha temporária para um aluno,
    sem precisar saber (nem poder ver) a senha antiga — o Django nunca
    guarda senhas em texto puro, então redefinir é a única forma de
    ajudar um aluno que esqueceu a senha.

    Só aceita POST de propósito (mesmo padrão de excluir_aluno_view):
    um clique/link acidental (GET) nunca troca a senha de ninguém sem
    confirmação explícita do professor.
    """
    aluno = get_object_or_404(User, id=aluno_id)

    if aluno.is_staff:
        # Proteção extra: nunca deixa redefinir a senha de outro
        # professor por engano nem a de si mesmo por aqui.
        return redirect('painel_professor')

    if request.method == 'POST':
        nova_senha = _gerar_senha_temporaria()
        aluno.set_password(nova_senha)
        aluno.save()
        logger.info(
            "Senha redefinida pelo professor %s para o aluno: %s",
            request.user.username, aluno.first_name or aluno.username
        )
        return render(request, 'senha_redefinida.html', {
            'aluno': aluno,
            'nova_senha': nova_senha,
        })

    # Se alguém tentar acessar por GET (ex: digitando a URL direto),
    # só mostra a tela de confirmação, sem trocar a senha ainda.
    return render(request, 'confirmar_redefinir_senha.html', {'aluno': aluno})
