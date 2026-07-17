import json
import logging
import random
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


# ─────────────────────────────────────────────
# CIÊNCIAS — 5 módulos (mesmo padrão genérico)
# ─────────────────────────────────────────────

MODULOS_CIENCIAS = {
    'plantas': ('Plantas', '🌱'),
    'sons': ('Sons', '🔊'),
    'solo': ('Solo', '🪨'),
    'petroleo': ('Petróleo', '🛢️'),
    'sistema_solar': ('Sistema Solar', '🪐'),
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

    return materias, total_geral


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
