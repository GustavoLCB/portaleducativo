"""
popular_portugues.py
----------------------
Execute na raiz do projeto:
    python popular_portugues.py

Popula o banco com questões de Português em 11 módulos:
  - ortografia (C, SS, XC, S, SC, G, J...)
  - sinonimos_antonimos
  - encontros_vocalicos (ditongo, hiato, tritongo)
  - digrafos
  - classificacao_silabica (tonicidade e número de sílabas)
  - encontros_consonantais
  - substantivos_adjetivos
  - tipos_de_frase
  - tempos_verbais (presente, pretérito e futuro)
  - substantivos_singular_plural (regras de formação do plural)
  - artigos (definidos e indefinidos)

Baseado nos temas cobrados na Avaliação de Língua Portuguesa do 2º
Período (Colégio Santo Agostinho, 3º ano) e em conteúdo adicional do
mesmo nível de dificuldade.

Pode rodar de novo sem problema — não duplica questões já existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_questao(disciplina, modulo, tipo, enunciado, resposta, opcoes):
    obj, criado = BancoQuestao.objects.update_or_create(
        disciplina=disciplina,
        modulo=modulo,
        enunciado=enunciado,
        defaults={
            'tipo': tipo,
            'resposta_correta': resposta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "🔄 Atualizado"
    print(f"  {status}: {enunciado[:65]}")


print("\n📚 Criando disciplina Português...")
portugues, _ = Disciplina.objects.get_or_create(
    nome='portugues', defaults={'nome_exibicao': 'Português'}
)
print("  ✅ Português pronto.")


# ══════════════════════════════════════════════════════════════════
# MÓDULO 1 — ORTOGRAFIA (C, SS, XC, S, SC, G, J...)
# ══════════════════════════════════════════════════════════════════
print("\n✏️  Populando: Português › Ortografia...")

ortografia = [
    ('E___ELENTE (a prova foi e___elente)', 'XC', ['C', 'SS', 'XC', 'S']),
    ('NA___ER (toda criança precisa na___er)', 'SC', ['SC', 'SS', 'C', 'X']),
    ('CRE___A (é importante cre___er sempre)', 'SC', ['SC', 'SS', 'C', 'Ç']),
    ('PROFE___OR (o profe___or da turma é gentil)', 'SS', ['SS', 'S', 'C', 'Ç']),
    ('PEI___E ( o pei__e nada muito rápido no rio)', 'X', ['S','X','SC','C']),
    ('CORA___ÃO ( Eu sinto muito amor no meu cora__ão)', 'Ç', ['S','X','SC','Ç']),
    ('___ANELA (a __anela da cozinha está aberta)', 'J', ['S','J','G','C']),
    ('E___EÇÃ0 (esta regra tem uma exceção)', 'XC', ['SS','XC','SC','C']),
    ('___OL (O __ol vai nascer logo)', 'S', ['S','X','SC','C']),
    ('___EBRA (a __ebra come capim no campo)', 'Z', ['S','Z','SC','G']),
    ('O___O (o cachorro gosta de roer o o____o)', 'SS', ['S','Z','SS','C']),
    ('FA___ENDA (a fa___enda tem uma porta de madeira azul)', 'Z', ['Z','X','SC','C']),
    ('LAPI___EIRA (a lapi__eira tem ponta fina)', 'S', ['S','Z','J','C']),
    ('A___ADO (o menino ficou muito a___ado)', 'SS', ['SS', 'S', 'C', 'X']),
    ('VIA___EM (fizemos uma linda via___em)', 'G', ['G', 'J', 'X', 'CH']),
    ('JI___OIA (a ji___oia é um réptil)', 'B', ['B', 'V', 'P', 'F']),
    ('EN___AME (o en___ame de abelhas voou)', 'X', ['X', 'CH', 'S', 'Z']),
    ('MÁ___IMO (nossa professora é o má___imo)', 'X', ['X', 'CH', 'S', 'Z']),
    ('___IRAFA (a ___irafa é um animal alto)', 'G', ['G', 'J', 'X', 'C']),
    ('CO___EÇAR (vamos co___eçar a atividade)', 'M', ['M', 'N', 'MB', 'NH']),
    ('___ÍCARA (tomei leite na ___ícara)', 'X', ['X', 'CH', 'S', 'SS']),
    ('DO___E (é gostoso o do___e de chocolate)', 'C', ['SS', 'S', 'C', 'Ç']),
    ('EMBAI___ADA (o menino fez embai___ada com a bola)', 'X', ['X', 'CH', 'SS', 'S']),
    ('PI___AMA (coloquei o pi___ama para dormir)', 'J', ['J', 'G', 'X', 'CH']),
    ('BEBE___OURO (o pássaro é um bebe___ouro)', 'D', ['D', 'T', 'DJ', 'J']),
    ('CAN___ADO (fiquei muito can___ado hoje)', 'S', ['S', 'SS', 'C', 'Ç']),
    ('MA___ÃS (comprei duas ma___ãs vermelhas)', 'Ç', ['Ç', 'SS', 'S', 'C']),
]
for enunciado, resposta, opcoes in ortografia:
    criar_questao(portugues, 'ortografia', 'completar_frase', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 2 — SINÔNIMOS E ANTÔNIMOS
# ══════════════════════════════════════════════════════════════════
print("\n🔄 Populando: Português › Sinônimos e Antônimos...")

sinonimos_antonimos = [
    ('Qual é o SINÔNIMO de "feliz"?', 'Alegre', ['Alegre', 'Triste', 'Bravo', 'Cansado']),
    ('Qual é o SINÔNIMO de "grande"?', 'Enorme', ['Enorme', 'Pequeno', 'Baixo', 'Fraco']),
    ('Qual é o SINÔNIMO de "rápido"?', 'Veloz', ['Veloz', 'Lento', 'Devagar', 'Parado']),
    ('Qual é o SINÔNIMO de "bonito"?', 'Belo', ['Belo', 'Feio', 'Estranho', 'Simples']),
    ('Qual é o SINÔNIMO de "guardar"?', 'Economizar', ['Economizar', 'Gastar', 'Perder', 'Jogar']),
    ('Qual é o SINÔNIMO de "corajoso"?', 'Valente', ['Valente', 'Medroso', 'Tímido', 'Fraco']),
    ('Qual é o ANTÔNIMO de "alegria"?', 'Tristeza', ['Tristeza', 'Felicidade', 'Diversão', 'Alívio']),
    ('Qual é o ANTÔNIMO de "grande"?', 'Pequeno', ['Pequeno', 'Enorme', 'Gigante', 'Imenso']),
    ('Qual é o ANTÔNIMO de "começar"?', 'Terminar', ['Terminar', 'Iniciar', 'Abrir', 'Criar']),
    ('Qual é o ANTÔNIMO de "subir"?', 'Descer', ['Descer', 'Levantar', 'Elevar', 'Pular']),
    ('Qual é o ANTÔNIMO de "dia"?', 'Noite', ['Noite', 'Tarde', 'Manhã', 'Sol']),
    ('Qual é o ANTÔNIMO de "quente"?', 'Frio', ['Frio', 'Morno', 'Fervendo', 'Ardente']),
    ('Qual é o SINÔNIMO de "amigo"?', 'Companheiro', ['Companheiro', 'Inimigo', 'Estranho', 'Rival']),
    ('Qual é o ANTÔNIMO de "abrir"?', 'Fechar', ['Fechar', 'Destrancar', 'Puxar', 'Girar']),
    ('Qual é o SINÔNIMO de "triste"?', 'Chateado', ['Chateado', 'Feliz', 'Animado', 'Contente']),
    ('Qual é o ANTÔNIMO de "gigante"?', 'Minúsculo', ['Minúsculo', 'Enorme', 'Alto', 'Largo']),
    ('Qual é o SINÔNIMO de "sincero"?', 'Verdadeiro', ['Verdadeiro', 'Mentiroso', 'Falso', 'Duvidoso']),
    ('Qual é o ANTÔNIMO de "fácil"?', 'Difícil', ['Difícil', 'Simples', 'Rápido', 'Claro']),
]
for enunciado, resposta, opcoes in sinonimos_antonimos:
    criar_questao(portugues, 'sinonimos_antonimos', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 3 — ENCONTROS VOCÁLICOS (ditongo, hiato, tritongo)
# ══════════════════════════════════════════════════════════════════
print("\n🔤 Populando: Português › Encontros Vocálicos...")

encontros_vocalicos = [
    ('Na palavra "história", o encontro "ia" é um:', 'Hiato', ['Hiato', 'Ditongo', 'Tritongo', 'Dígrafo']),
    ('Na palavra "pai", o encontro "ai" é um:', 'Ditongo', ['Ditongo', 'Hiato', 'Tritongo', 'Dígrafo']),
    ('Na palavra "saguão", o encontro "uão" é um:', 'Tritongo', ['Tritongo', 'Ditongo', 'Hiato', 'Dígrafo']),
    ('Na palavra "saúde", o encontro "aú" é um:', 'Hiato', ['Hiato', 'Ditongo', 'Tritongo', 'Dígrafo']),
    ('Na palavra "cadeira", o encontro "ei" é um:', 'Ditongo', ['Ditongo', 'Hiato', 'Tritongo', 'Dígrafo']),
    ('Na palavra "poesia", o encontro "oe" é um:', 'Hiato', ['Hiato', 'Ditongo', 'Tritongo', 'Dígrafo']),
    ('Na palavra "Paraguai", o encontro "uai" é um:', 'Tritongo', ['Tritongo', 'Ditongo', 'Hiato', 'Dígrafo']),
    ('Na palavra "chapéu", o encontro "éu" é um:', 'Ditongo', ['Ditongo', 'Hiato', 'Tritongo', 'Dígrafo']),
    ('Na palavra "juiz", o encontro "ui" é um:', 'Hiato', ['Hiato', 'Ditongo', 'Tritongo', 'Dígrafo']),
    ('Na palavra "quais", o encontro "uai" é um:', 'Tritongo', ['Tritongo', 'Ditongo', 'Hiato', 'Dígrafo']),
    ('Na palavra "égua", o encontro "gua" é um:', 'Ditongo', ['Ditongo', 'Hiato', 'Tritongo', 'Dígrafo']),
    ('Na palavra "baú", o encontro "aú" é um:', 'Hiato', ['Hiato', 'Ditongo', 'Tritongo', 'Dígrafo']),
    ('Na palavra "série", o encontro "ie" é um:', 'Ditongo', ['Ditongo', 'Hiato', 'Tritongo', 'Dígrafo']),
    ('Na frase "Antônio era um menino magrinho e de óculos", a palavra com ditongo é:', 'Antônio', ['Antônio', 'menino', 'de', 'e']),
]
for enunciado, resposta, opcoes in encontros_vocalicos:
    criar_questao(portugues, 'encontros_vocalicos', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 4 — DÍGRAFOS
# ══════════════════════════════════════════════════════════════════
print("\n🔠 Populando: Português › Dígrafos...")

digrafos = [
    ('Qual das palavras abaixo tem um DÍGRAFO?', 'Passeio', ['Passeio', 'Bola', 'Janela', 'Sapato']),
    ('Na palavra "carro", qual é o dígrafo?', 'RR', ['RR', 'CA', 'AR', 'RO']),
    ('Na palavra "chuva", qual é o dígrafo?', 'CH', ['CH', 'UV', 'HU', 'VA']),
    ('Na palavra "ninho", qual é o dígrafo?', 'NH', ['NH', 'NI', 'HO', 'IN']),
    ('Na palavra "filho", qual é o dígrafo?', 'LH', ['LH', 'FI', 'HO', 'IL']),
    ('Na palavra "queijo", qual é o dígrafo?', 'QU', ['QU', 'EI', 'JO', 'UE']),
    ('Na palavra "guerra", qual é o dígrafo que representa o som de "g"?', 'GU', ['GU', 'RR', 'ER', 'GE']),
    ('Na palavra "nascer", qual é o dígrafo?', 'SC', ['SC', 'NA', 'CE', 'ER']),
    ('Na palavra "excesso", qual é o dígrafo?', 'XC', ['XC', 'SS', 'ES', 'CE']),
    ('Qual das palavras abaixo NÃO tem dígrafo?', 'Janela', ['Janela', 'Carro', 'Chuva', 'Ninho']),
    ('Na palavra "assunto", qual é o dígrafo?', 'SS', ['SS', 'AS', 'UN', 'TO']),
    ('Na palavra "quilo", qual é o dígrafo?', 'QU', ['QU', 'IL', 'LO', 'UI']),
    ('Classifique a palavra "digrafo" quanto à quantidade de sons representados pelo par de letras "CH", "LH" e "NH": eles formam um único:', 'Som', ['Som', 'Sílaba', 'Ditongo', 'Hiato']),
]
for enunciado, resposta, opcoes in digrafos:
    criar_questao(portugues, 'digrafos', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 5 — CLASSIFICAÇÃO SILÁBICA (tonicidade e nº de sílabas)
# ══════════════════════════════════════════════════════════════════
print("\n🎵 Populando: Português › Classificação Silábica...")

classificacao_silabica = [
    ('A palavra "futebol" é classificada, quanto à tonicidade, como:', 'Oxítona', ['Oxítona', 'Paroxítona', 'Proparoxítona', 'Monossílaba']),
    ('A palavra "árvore" é classificada, quanto à tonicidade, como:', 'Proparoxítona', ['Proparoxítona', 'Oxítona', 'Paroxítona', 'Monossílaba']),
    ('A palavra "casa" é classificada, quanto à tonicidade, como:', 'Paroxítona', ['Paroxítona', 'Oxítona', 'Proparoxítona', 'Monossílaba']),
    ('A palavra "café" é classificada, quanto à tonicidade, como:', 'Oxítona', ['Oxítona', 'Paroxítona', 'Proparoxítona', 'Monossílaba']),
    ('A palavra "médico" é classificada, quanto à tonicidade, como:', 'Proparoxítona', ['Proparoxítona', 'Oxítona', 'Paroxítona', 'Monossílaba']),
    ('A palavra "futebol" é classificada quanto ao número de sílabas como:', 'Trissílaba', ['Trissílaba', 'Dissílaba', 'Monossílaba', 'Polissílaba']),
    ('A palavra "sol" é classificada quanto ao número de sílabas como:', 'Monossílaba', ['Monossílaba', 'Dissílaba', 'Trissílaba', 'Polissílaba']),
    ('A palavra "bola" é classificada quanto ao número de sílabas como:', 'Dissílaba', ['Dissílaba', 'Monossílaba', 'Trissílaba', 'Polissílaba']),
    ('A palavra "borboleta" é classificada quanto ao número de sílabas como:', 'Polissílaba', ['Polissílaba', 'Dissílaba', 'Trissílaba', 'Monossílaba']),
    ('A palavra "magrinho" é classificada quanto ao número de sílabas como:', 'Trissílaba', ['Trissílaba', 'Dissílaba', 'Monossílaba', 'Polissílaba']),
    ('Quantas sílabas tem a palavra "computador"?', '4', ['4', '3', '2', '5']),
    ('Quantas sílabas tem a palavra "pão"?', '1', ['1', '2', '3', '4']),
    ('A palavra "relógio" é classificada, quanto à tonicidade, como:', 'Paroxítona', ['Paroxítona', 'Oxítona', 'Proparoxítona', 'Monossílaba']),
]
for enunciado, resposta, opcoes in classificacao_silabica:
    criar_questao(portugues, 'classificacao_silabica', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 6 — ENCONTROS CONSONANTAIS (novo, a partir das folhas novas)
# ══════════════════════════════════════════════════════════════════
print("\n🔤 Populando: Português › Encontros Consonantais...")

encontros_consonantais = [
    ('Qual é o encontro consonantal na palavra "FLAUTA"?', 'FL', ['FL', 'AU', 'TA', 'LA']),
    ('Qual é o encontro consonantal na palavra "PRATO"?', 'PR', ['PR', 'AT', 'TO', 'RA']),
    ('Qual é o encontro consonantal na palavra "GRAMA"?', 'GR', ['GR', 'AM', 'MA', 'RA']),
    ('Qual é o encontro consonantal na palavra "CLASSE"?', 'CL', ['CL', 'AS', 'SE', 'LA']),
    ('Qual é o encontro consonantal na palavra "TRAVA"?', 'TR', ['TR', 'AV', 'VA', 'RA']),
    ('Quantos encontros consonantais há na palavra "PROBLEMA"?', '2', ['2', '1', '3', '0']),
    ('Quantos encontros consonantais há na palavra "PLANALTO"?', '1', ['1', '2', '3', '0']),
    ('Qual das palavras abaixo tem um encontro consonantal?', 'Prato', ['Prato', 'Bola', 'Mesa', 'Sapato']),
    ('Qual das palavras abaixo NÃO tem encontro consonantal?', 'Mesa', ['Mesa', 'Prato', 'Grama', 'Flauta']),
    ('Na palavra "BRINCO", qual é o encontro consonantal?', 'BR', ['BR', 'IN', 'CO', 'RI']),
    ('Na palavra "CREME", qual é o encontro consonantal?', 'CR', ['CR', 'EM', 'ME', 'RE']),
    ('Na palavra "DRAGÃO", qual é o encontro consonantal?', 'DR', ['DR', 'AG', 'ÃO', 'RA']),
    ('Na palavra "GLOBO", qual é o encontro consonantal?', 'GL', ['GL', 'OB', 'BO', 'LO']),
    ('O encontro consonantal acontece quando duas ___ aparecem juntas na mesma sílaba, e cada uma faz seu som.', 'consoantes',
     ['consoantes', 'vogais', 'sílabas', 'letras']),
    ('Na palavra "ATLETA", qual é o encontro consonantal?', 'TL', ['TL', 'AT', 'LE', 'TA']),
]
for enunciado, resposta, opcoes in encontros_consonantais:
    criar_questao(portugues, 'encontros_consonantais', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 7 — SUBSTANTIVOS E ADJETIVOS (novo)
# ══════════════════════════════════════════════════════════════════
print("\n🏷️  Populando: Português › Substantivos e Adjetivos...")

substantivos_adjetivos = [
    ('Na frase "O peixe azul enfeita o aquário redondo", qual é o adjetivo que descreve "peixe"?', 'Azul',
     ['Azul', 'Redondo', 'Aquário', 'Enfeita']),
    ('Na frase "O peixe azul enfeita o aquário redondo", qual é o adjetivo que descreve "aquário"?', 'Redondo',
     ['Redondo', 'Azul', 'Peixe', 'Enfeita']),
    ('Na frase "A geladeira branca estava cheia de comidas gostosas", qual é o adjetivo de "geladeira"?', 'Branca',
     ['Branca', 'Gostosas', 'Cheia', 'Comidas']),
    ('Na frase "A geladeira branca estava cheia de comidas gostosas", qual é o adjetivo de "comidas"?', 'Gostosas',
     ['Gostosas', 'Branca', 'Cheia', 'Geladeira']),
    ('"Gabriel" é um substantivo:', 'Próprio', ['Próprio', 'Comum', 'Coletivo', 'Abstrato']),
    ('"Menino" é um substantivo:', 'Comum', ['Comum', 'Próprio', 'Coletivo', 'Abstrato']),
    ('Na frase "Os meninos Gabriel e Lucas cuidam dos seus velhos brinquedos", cite um substantivo próprio:', 'Gabriel',
     ['Gabriel', 'Meninos', 'Brinquedos', 'Velhos']),
    ('Qual é o adjetivo na frase "O velho marinheiro misterioso carregava um baú"?', 'Misterioso',
     ['Misterioso', 'Marinheiro', 'Baú', 'Carregava']),
    ('Substantivos próprios sempre começam com:', 'Letra maiúscula', ['Letra maiúscula', 'Letra minúscula', 'Número', 'Acento']),
    ('"Cidade" é um substantivo:', 'Comum', ['Comum', 'Próprio', 'Coletivo', 'Abstrato']),
    ('"Brasil" é um substantivo:', 'Próprio', ['Próprio', 'Comum', 'Coletivo', 'Abstrato']),
    ('Na frase "A mamãe Joana canta triste dentro da gaiola fria", qual é o substantivo próprio?', 'Joana',
     ['Joana', 'Mamãe', 'Gaiola', 'Triste']),
    ('Qual é o adjetivo que caracteriza "gaiola" na frase "A mamãe Joana canta triste dentro da gaiola fria"?', 'Fria',
     ['Fria', 'Joana', 'Mamãe', 'Canta']),
    ('"Professora" é um substantivo:', 'Comum', ['Comum', 'Próprio', 'Coletivo', 'Abstrato']),
    ('"Machado de Assis" é um substantivo:', 'Próprio', ['Próprio', 'Comum', 'Coletivo', 'Abstrato']),
]
for enunciado, resposta, opcoes in substantivos_adjetivos:
    criar_questao(portugues, 'substantivos_adjetivos', 'multipla_escolha', enunciado, resposta, opcoes)

# ── Bloco novo (06/08): gênero (feminino) e classe gramatical
substantivos_adjetivos_novo = [
    ('Qual é o feminino de "rei"?', 'Rainha', ['Rainha', 'Reia', 'Reína', 'Reisa']),
    ('Reescrevendo a frase "No tabuleiro do jogo de xadrez havia um rei." trocando "rei" para o feminino, ela fica:', 'No tabuleiro do jogo de xadrez havia uma rainha.',
     ['No tabuleiro do jogo de xadrez havia uma rainha.', 'No tabuleiro do jogo de xadrez havia um reia.',
      'No tabuleiro do jogo de xadrez havia uma reína.', 'No tabuleiro do jogo de xadrez havia um rei.']),
    ('Qual é o feminino de "padrasto"?', 'Madrasta', ['Madrasta', 'Padrasta', 'Padastra', 'Madastra']),
    ('Na frase "Nem um fiozinho dourado de cabelo aparecia no berço do Sol", a palavra "fiozinho" é um:', 'Substantivo comum',
     ['Substantivo comum', 'Substantivo próprio', 'Adjetivo', 'Verbo']),
    ('Na frase "Nem um fiozinho dourado de cabelo aparecia no berço do Sol", a palavra "dourado" é um:', 'Adjetivo',
     ['Adjetivo', 'Substantivo comum', 'Substantivo próprio', 'Artigo']),
    ('Na frase "Nem um fiozinho dourado de cabelo aparecia no berço do Sol", a palavra "Sol" é um:', 'Substantivo próprio',
     ['Substantivo próprio', 'Substantivo comum', 'Adjetivo', 'Verbo']),
    ('Na frase "...entre as montanhas imensas", a palavra "montanhas" é um:', 'Substantivo comum',
     ['Substantivo comum', 'Substantivo próprio', 'Adjetivo', 'Artigo']),
    ('Na frase "...entre as montanhas imensas", a palavra "imensas" é um:', 'Adjetivo',
     ['Adjetivo', 'Substantivo comum', 'Substantivo próprio', 'Verbo']),
]
for enunciado, resposta, opcoes in substantivos_adjetivos_novo:
    criar_questao(portugues, 'substantivos_adjetivos', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 8 — TIPOS DE FRASE (novo)
# ══════════════════════════════════════════════════════════════════
print("\n💬 Populando: Português › Tipos de Frase...")

tipos_de_frase = [
    ('"Você viu o gato?" é uma frase:', 'Interrogativa', ['Interrogativa', 'Exclamativa', 'Declarativa', 'Imperativa']),
    ('"Que dia lindo!" é uma frase:', 'Exclamativa', ['Exclamativa', 'Interrogativa', 'Declarativa', 'Imperativa']),
    ('"O sol nasce no leste." é uma frase:', 'Declarativa', ['Declarativa', 'Interrogativa', 'Exclamativa', 'Imperativa']),
    ('"Feche a porta, por favor." é uma frase:', 'Imperativa', ['Imperativa', 'Declarativa', 'Interrogativa', 'Exclamativa']),
    ('"Como você está?" é uma frase:', 'Interrogativa', ['Interrogativa', 'Exclamativa', 'Declarativa', 'Imperativa']),
    ('"Que susto!" é uma frase:', 'Exclamativa', ['Exclamativa', 'Interrogativa', 'Declarativa', 'Imperativa']),
    ('"As flores são bonitas." é uma frase:', 'Declarativa', ['Declarativa', 'Interrogativa', 'Exclamativa', 'Imperativa']),
    ('"Guarde seus brinquedos agora." é uma frase:', 'Imperativa', ['Imperativa', 'Declarativa', 'Interrogativa', 'Exclamativa']),
    ('"Onde você mora?" é uma frase:', 'Interrogativa', ['Interrogativa', 'Exclamativa', 'Declarativa', 'Imperativa']),
    ('"Nossa, que surpresa incrível!" é uma frase:', 'Exclamativa', ['Exclamativa', 'Interrogativa', 'Declarativa', 'Imperativa']),
    ('"O cachorro late muito." é uma frase:', 'Declarativa', ['Declarativa', 'Interrogativa', 'Exclamativa', 'Imperativa']),
    ('"Escreva seu nome na folha." é uma frase:', 'Imperativa', ['Imperativa', 'Declarativa', 'Interrogativa', 'Exclamativa']),
    ('"Quantos anos você tem?" é uma frase:', 'Interrogativa', ['Interrogativa', 'Exclamativa', 'Declarativa', 'Imperativa']),
    ('"Que dia terrível!" é uma frase:', 'Exclamativa', ['Exclamativa', 'Interrogativa', 'Declarativa', 'Imperativa']),
    ('"A escola começa às sete horas." é uma frase:', 'Declarativa', ['Declarativa', 'Interrogativa', 'Exclamativa', 'Imperativa']),
]
for enunciado, resposta, opcoes in tipos_de_frase:
    criar_questao(portugues, 'tipos_de_frase', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 9 — TEMPOS VERBAIS (novo)
# ══════════════════════════════════════════════════════════════════
print("\n⏰ Populando: Português › Tempos Verbais...")

tempos_verbais = [
    ('Na frase "Larguei a mão da minha avó e entrei na sala", os verbos destacados estão no:', 'Pretérito (passado)',
     ['Pretérito (passado)', 'Presente', 'Futuro', 'Imperativo']),
    ('Complete com o verbo no PRESENTE: "Hoje eu ___ na escola." (estudar)', 'estudo',
     ['estudo', 'estudei', 'estudarei', 'estudava']),
    ('Complete com o verbo no PRETÉRITO (passado): "Ontem eu ___ na escola." (estudar)', 'estudei',
     ['estudei', 'estudo', 'estudarei', 'estudava']),
    ('Complete com o verbo no FUTURO: "Amanhã eu ___ na escola." (estudar)', 'estudarei',
     ['estudarei', 'estudei', 'estudo', 'estudava']),
    ('A frase "Eu brinco no parque todos os dias" está no tempo:', 'Presente',
     ['Presente', 'Pretérito', 'Futuro', 'Imperativo']),
    ('A frase "Eu brinquei no parque ontem" está no tempo:', 'Pretérito (passado)',
     ['Pretérito (passado)', 'Presente', 'Futuro', 'Imperativo']),
    ('A frase "Eu vou brincar no parque amanhã" está no tempo:', 'Futuro',
     ['Futuro', 'Presente', 'Pretérito', 'Imperativo']),
    ('Qual palavra indica que a frase está no PASSADO?', 'Ontem', ['Ontem', 'Hoje', 'Amanhã', 'Agora']),
    ('Qual palavra indica que a frase está no FUTURO?', 'Amanhã', ['Amanhã', 'Ontem', 'Hoje', 'Já']),
    ('Qual palavra indica que a frase está no PRESENTE?', 'Agora', ['Agora', 'Ontem', 'Amanhã', 'Antigamente']),
    ('Complete com o verbo no PRETÉRITO: "Ele ___ muito aflito quando chegou à escola." (estar)', 'estava',
     ['estava', 'está', 'estará', 'esteja']),
    ('Na frase "Reparei que já tinham caído dois dentes dele", o verbo "reparei" indica uma ação:', 'Que já aconteceu',
     ['Que já aconteceu', 'Que está acontecendo agora', 'Que ainda vai acontecer', 'Que nunca aconteceu']),
    ('Complete com o verbo no FUTURO: "No ano que vem, nós ___ para o 4º ano." (ir)', 'iremos',
     ['iremos', 'fomos', 'vamos', 'íamos']),
    ('A frase "Nós brincaremos no recreio" está no tempo:', 'Futuro', ['Futuro', 'Presente', 'Pretérito', 'Imperativo']),
    ('A frase "Nós brincamos no recreio ontem" está no tempo:', 'Pretérito (passado)',
     ['Pretérito (passado)', 'Presente', 'Futuro', 'Imperativo']),
]
for enunciado, resposta, opcoes in tempos_verbais:
    criar_questao(portugues, 'tempos_verbais', 'multipla_escolha', enunciado, resposta, opcoes)

# ── Bloco novo (06/08): infinitivo, conjugação e terminações -ram/-rão
tempos_verbais_novo = [
    ('O verbo "prenderam" está em qual tempo verbal?', 'Pretérito (passado)', ['Pretérito (passado)', 'Presente', 'Futuro', 'Imperativo']),
    ('Qual é o infinitivo do verbo "prenderam"?', 'Prender', ['Prender', 'Prendeu', 'Prendendo', 'Prendido']),
    ('O verbo "prender" pertence a qual conjugação?', '2ª conjugação (terminado em -ER)', ['2ª conjugação (terminado em -ER)', '1ª conjugação (terminado em -AR)', '3ª conjugação (terminado em -IR)', 'Não tem conjugação']),
    ('Reescrevendo a frase "E por que te prenderam?" com o verbo no futuro, ela fica:', 'E por que te prenderão?', ['E por que te prenderão?', 'E por que te prendem?', 'E por que te prendia?', 'E por que te prendeste?']),
    ('Usamos a terminação verbal "-RAM" para indicar o tempo:', 'Passado (pretérito)', ['Passado (pretérito)', 'Presente', 'Futuro', 'Imperativo']),
    ('Usamos a terminação verbal "-RÃO" para indicar o tempo:', 'Futuro', ['Futuro', 'Presente', 'Passado (pretérito)', 'Imperativo']),
    ('Qual destes verbos está no FUTURO?', 'Votarão', ['Votarão', 'Fugiram', 'Sorriram', 'Decidiram']),
    ('Qual destes verbos está no FUTURO?', 'Resolverão', ['Resolverão', 'Brincam', 'Pintaram', 'Aprenderam']),
    ('Qual destes verbos NÃO está no futuro?', 'Aprenderam', ['Aprenderam', 'Lerão', 'Sentirão', 'Escreverão']),
    ('Complete com o verbo correto: "No mês que vem, meus primos ___ para a Europa." (viajarão / viajaram)', 'viajarão', ['viajarão', 'viajaram', 'viajam', 'viajavam']),
    ('Complete com o verbo correto: "Ontem, os gêmeos Marcos e Lucas ___ 8 anos de idade." (completaram / completarão)', 'completaram', ['completaram', 'completarão', 'completam', 'completavam']),
    ('Complete com o verbo correto: "As crianças ___ o bolo da festa mais tarde." (comeram / comerão)', 'comerão', ['comerão', 'comeram', 'comem', 'comiam']),
    ('Um verbo é uma palavra que indica, principalmente:', 'Uma ação, um estado ou um fenômeno', ['Uma ação, um estado ou um fenômeno', 'O nome de uma pessoa ou lugar', 'Uma característica de um substantivo', 'A quantidade de algo']),
]
for enunciado, resposta, opcoes in tempos_verbais_novo:
    criar_questao(portugues, 'tempos_verbais', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 10 — SUBSTANTIVO: SINGULAR E PLURAL (novo)
# ══════════════════════════════════════════════════════════════════
print("\n🔢 Populando: Português › Substantivo Singular e Plural...")

substantivos_singular_plural = [
    ('O substantivo que indica UM ser, objeto, lugar ou animal está no:', 'Singular',
     ['Singular', 'Plural', 'Coletivo', 'Próprio']),
    ('O substantivo que indica MAIS DE UM ser, objeto, lugar ou animal está no:', 'Plural',
     ['Plural', 'Singular', 'Coletivo', 'Comum']),
    ('Qual é o plural de "barco"?', 'Barcos', ['Barcos', 'Barcões', 'Barcais', 'Barces']),
    ('Substantivos terminados em R, S e Z fazem o plural com o acréscimo de:', 'ES',
     ['ES', 'S', 'AIS', 'ÕES']),
    ('Qual é o plural de "país"?', 'Países', ['Países', 'Paíss', 'Paízes', 'Paíes']),
    ('Qual é o plural de "luz"?', 'Luzes', ['Luzes', 'Luzs', 'Luzas', 'Luz']),
    ('Substantivos terminados em AL, OL e UL fazem o plural em:', 'AIS, ÓIS e UIS',
     ['AIS, ÓIS e UIS', 'ES', 'ÕES', 'NS']),
    ('Qual é o plural de "jornal"?', 'Jornais', ['Jornais', 'Jornals', 'Jornales', 'Jornãos']),
    ('Qual é o plural de "farol"?', 'Faróis', ['Faróis', 'Farols', 'Faroles', 'Farões']),
    ('Substantivos terminados em EL fazem o plural em ÉIS ou EIS. Qual é o plural de "papel"?', 'Papéis',
     ['Papéis', 'Papels', 'Papeles', 'Papelões']),
    ('Substantivos terminados em M fazem o plural em:', 'NS', ['NS', 'MS', 'ÕES', 'ES']),
    ('Qual é o plural de "trem"?', 'Trens', ['Trens', 'Tremes', 'Tremões', 'Trems']),
    ('Substantivos terminados em ÃO podem fazer o plural em ÕES, ÃES ou ÃOS. Qual é o plural de "pão"?', 'Pães',
     ['Pães', 'Pãos', 'Pões', 'Pãoes']),
    ('Qual é o plural de "botão"?', 'Botões', ['Botões', 'Botãos', 'Botães', 'Botãoes']),
    ('Substantivos terminados em IL fazem o plural em IS ou EIS. Qual é o plural de "funil"?', 'Funis',
     ['Funis', 'Funiles', 'Funíeis', 'Funils']),
    ('Qual é o plural de "réptil"?', 'Répteis', ['Répteis', 'Reptis', 'Reptíeis', 'Répteles']),
    ('Qual é o plural de "flor"?', 'Flores', ['Flores', 'Flors', 'Florees', 'Flor']),
    ('Qual é o plural de "coração"?', 'Corações', ['Corações', 'Coraçãos', 'Coraçães', 'Coraçãoes']),
    ('Os substantivos paroxítonos terminados em S, como "tênis" e "ônibus", no plural:', 'Não mudam de forma',
     ['Não mudam de forma', 'Ganham ES', 'Ganham S', 'Perdem o S']),
    ('Qual é o plural de "ônibus"?', 'Ônibus', ['Ônibus', 'Ônibuses', 'Ônibuzes', 'Ônibuis']),
]
for enunciado, resposta, opcoes in substantivos_singular_plural:
    criar_questao(portugues, 'substantivos_singular_plural', 'multipla_escolha', enunciado, resposta, opcoes)

# ── Bloco novo (06/08): mais palavras para praticar as regras de plural
substantivos_singular_plural_novo = [
    ('Qual é o plural de "batom"?', 'Batons', ['Batons', 'Batões', 'Batomes', 'Batons']),
    ('Qual é o plural de "carretel"?', 'Carretéis', ['Carretéis', 'Carreteis', 'Carretels', 'Carreteles']),
    ('Qual é o plural de "francês"?', 'Franceses', ['Franceses', 'Francêses', 'Francezes', 'Francês']),
    ('Qual é o plural de "cão"?', 'Cães', ['Cães', 'Cãos', 'Cões', 'Cãoes']),
    ('Qual é o plural de "elevador"?', 'Elevadores', ['Elevadores', 'Elevadors', 'Elevadão', 'Elevador']),
    ('Qual é o plural de "mural"?', 'Murais', ['Murais', 'Murals', 'Murões', 'Muraizes']),
    ('Qual é o plural de "papel"?', 'Papéis', ['Papéis', 'Papels', 'Papeles', 'Papelões']),
    ('Qual é o plural de "estrela"?', 'Estrelas', ['Estrelas', 'Estrelaas', 'Estrelões', 'Estrelais']),
    ('Qual é o plural de "rapaz"?', 'Rapazes', ['Rapazes', 'Rapazs', 'Rapazãos', 'Rapaz']),
    ('Qual é o plural de "animal"?', 'Animais', ['Animais', 'Animals', 'Animales', 'Animalões']),
    ('Qual é o plural de "sol"?', 'Sóis', ['Sóis', 'Sols', 'Soles', 'Solzões']),
    ('Qual é o plural de "órgão"?', 'Órgãos', ['Órgãos', 'Órgãs', 'Orgões', 'Órgãoes']),
    ('Qual é o plural de "árvore"?', 'Árvores', ['Árvores', 'Árvors', 'Arvorezes', 'Árvore']),
    ('Qual é o plural de "parede"?', 'Paredes', ['Paredes', 'Pareds', 'Paredezes', 'Parede']),
    ('Qual é o plural de "muro"?', 'Muros', ['Muros', 'Murões', 'Murais', 'Muro']),
    ('Qual é o plural de "pudim"?', 'Pudins', ['Pudins', 'Pudis', 'Pudões', 'Pudim']),
    ('Qual é o plural de "pião"?', 'Piões', ['Piões', 'Piãos', 'Piães', 'Piãoes']),
    ('Qual é o plural de "jornal"?', 'Jornais', ['Jornais', 'Jornals', 'Jornales', 'Jornãos']),
]
for enunciado, resposta, opcoes in substantivos_singular_plural_novo:
    criar_questao(portugues, 'substantivos_singular_plural', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 11 — ARTIGOS DEFINIDOS E INDEFINIDOS (novo)
# ══════════════════════════════════════════════════════════════════
print("\n🔖 Populando: Português › Artigos...")

artigos = [
    ('Artigos são palavras que acompanham:', 'Os substantivos', ['Os substantivos', 'Os verbos', 'Os adjetivos', 'Os advérbios']),
    ('Usamos os artigos DEFINIDOS quando falamos de algo:', 'Conhecido, preciso e específico',
     ['Conhecido, preciso e específico', 'Vago e impreciso', 'Que não existe', 'Que é plural apenas']),
    ('Usamos os artigos INDEFINIDOS quando falamos de algo:', 'De modo geral, vago e impreciso',
     ['De modo geral, vago e impreciso', 'Conhecido e específico', 'Que já sabemos qual é', 'Que é singular apenas']),
    ('Quais são os artigos definidos?', 'O, a, os, as', ['O, a, os, as', 'Um, uma, uns, umas', 'Este, esta, isto', 'Meu, minha, meus']),
    ('Quais são os artigos indefinidos?', 'Um, uma, uns, umas', ['Um, uma, uns, umas', 'O, a, os, as', 'Esse, essa, isso', 'Seu, sua, seus']),
    ('Na frase "O cachorro latiu", o artigo "o" é:', 'Definido', ['Definido', 'Indefinido', 'Plural apenas', 'Feminino']),
    ('Na frase "Um gato apareceu", o artigo "um" é:', 'Indefinido', ['Indefinido', 'Definido', 'Feminino', 'Plural']),
    ('Complete: "___ maçã caiu da árvore." (uma maçã qualquer, não sabemos qual)', 'Uma', ['Uma', 'A', 'Umas', 'As']),
    ('Complete: "___ flor desabrochou." (uma flor específica, que já conhecemos)', 'A', ['A', 'Uma', 'As', 'Umas']),
    ('Complete: "___ alunos chegaram cedo." (alunos quaisquer, não sabemos quantos exatamente)', 'Uns', ['Uns', 'Os', 'Umas', 'As']),
    ('Complete: "___ livros estão na mochila." (livros específicos, que já conhecemos)', 'Os', ['Os', 'Uns', 'As', 'Umas']),
    ('O artigo deve concordar com o substantivo em:', 'Gênero e número', ['Gênero e número', 'Apenas gênero', 'Apenas número', 'Tempo verbal']),
    ('Qual é o artigo definido masculino plural?', 'Os', ['Os', 'As', 'Uns', 'O']),
    ('Qual é o artigo indefinido feminino plural?', 'Umas', ['Umas', 'Uns', 'As', 'Uma']),
    ('Na frase "As borboletas voaram", o artigo "as" é:', 'Definido, feminino e plural', ['Definido, feminino e plural', 'Indefinido, feminino e plural', 'Definido, masculino e singular', 'Indefinido, masculino e singular']),
    ('Uma boa dica para saber se o artigo é definido é perguntar: "Já sabemos qual é?". Se a resposta for SIM, o artigo é:', 'Definido',
     ['Definido', 'Indefinido', 'Plural', 'Feminino']),
]
for enunciado, resposta, opcoes in artigos:
    criar_questao(portugues, 'artigos', 'multipla_escolha', enunciado, resposta, opcoes)

# ── Bloco novo (06/08): identificação de artigos em frases
artigos_novo = [
    ('Na frase "Nem um fiozinho dourado de cabelo aparecia no berço do Sol", a palavra "um" é um:', 'Artigo indefinido',
     ['Artigo indefinido', 'Artigo definido', 'Substantivo', 'Adjetivo']),
    ('Na frase "...entre as montanhas imensas", a palavra "as" é um:', 'Artigo definido',
     ['Artigo definido', 'Artigo indefinido', 'Substantivo', 'Adjetivo']),
    ('Na frase "O meu papagaio voou sem ajuda", a palavra em destaque "O" é um artigo:', 'Definido', ['Definido', 'Indefinido', 'Plural', 'Feminino']),
    ('Na frase "O garoto comeu um hambúrguer", a palavra em destaque "um" é um artigo:', 'Indefinido', ['Indefinido', 'Definido', 'Plural', 'Feminino']),
    ('Na frase "Quando chover, eu vou usar uma capa", a palavra em destaque "uma" é um artigo:', 'Indefinido', ['Indefinido', 'Definido', 'Plural', 'Masculino']),
    ('Na frase "A escola colou um cartaz no pátio", a palavra em destaque "A" é um artigo:', 'Definido', ['Definido', 'Indefinido', 'Plural', 'Masculino']),
]
for enunciado, resposta, opcoes in artigos_novo:
    criar_questao(portugues, 'artigos', 'multipla_escolha', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 12 — INTERPRETAÇÃO DE TEXTO (novo, card criado com pouco
# material — a ideia é ir ampliando conforme novos textos/tirinhas
# forem enviados)
# ══════════════════════════════════════════════════════════════════
print("\n📖 Populando: Português › Interpretação de Texto...")

interpretacao_texto = [
    ('Na tirinha em que a planta pergunta "E por que te prenderam?", qual verbo aparece na fala da planta?', 'Prenderam',
     ['Prenderam', 'Prendeu', 'Prender', 'Prendendo']),
    ('Em que tempo verbal está o verbo "prenderam", na fala da planta?', 'Pretérito (passado)',
     ['Pretérito (passado)', 'Presente', 'Futuro', 'Imperativo']),
    ('Na tirinha do caranguejo Caranga, além do cheiro do manguezal, o que mais ele diz que adora sentir?', 'A brisa, ao som da natureza',
     ['A brisa, ao som da natureza', 'O frio da neve', 'O barulho do trânsito', 'O cheiro de fumaça']),
    ('A expressão "nosso querido lar", dita por Caranga, mostra que ele:', 'Demonstra carinho pelo lugar onde vive',
     ['Demonstra carinho pelo lugar onde vive', 'Não conhece muito bem o manguezal', 'Deseja procurar outro lugar para morar', 'Tem medo do manguezal']),
    ('Releia: "Nada como nosso querido lar! Adoro viver aqui no manguezal!". As palavras destacadas "querido", "Adoro" e "manguezal" são, respectivamente:', 'Adjetivo, verbo e substantivo',
     ['Adjetivo, verbo e substantivo', 'Substantivo, verbo e adjetivo', 'Verbo, substantivo e adjetivo', 'Adjetivo, substantivo e verbo']),
    ('Em um texto narrativo, o lugar onde os fatos ocorrem recebe o nome de:', 'Espaço',
     ['Espaço', 'Tempo', 'Personagem', 'Enredo']),
    ('Os verbos "entrei", "fui" e "reparei", destacados em um trecho de narrativa, ajudam a identificar que a narração está no:', 'Pretérito (passado)',
     ['Pretérito (passado)', 'Presente', 'Futuro', 'Imperativo']),
    ('Em um trecho de carta que menciona "um dos docinhos... e o bolo do vovô", quantos bolos haverá na festa?', 'Um bolo',
     ['Um bolo', 'Mais de um bolo', 'Nenhum bolo', 'Não é possível saber']),
    ('No mesmo trecho, quantos docinhos haverá na festa?', 'Mais de um docinho',
     ['Mais de um docinho', 'Um docinho', 'Nenhum docinho', 'Não é possível saber']),
    ('Na frase "Por que você está chorando, meu amor? — perguntou a minha avó com voz meiguinha", as palavras destacadas "meu amor" e "meiguinha" expressam:', 'Carinho, afeto',
     ['Carinho, afeto', 'O tamanho da voz da avó', 'Tristeza e irritação', 'Formalidade']),
    ('De acordo com a tirinha do caranguejo, cite uma característica do manguezal que faz Caranga gostar desse lugar.', 'O cheiro do lugar',
     ['O cheiro do lugar', 'O frio constante', 'A falta de plantas', 'O barulho de carros']),
]
for enunciado, resposta, opcoes in interpretacao_texto:
    criar_questao(portugues, 'interpretacao_texto', 'multipla_escolha', enunciado, resposta, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE PORTUGUÊS CONCLUÍDA!")
print("=" * 55)
for modulo, nome in [
    ('ortografia', 'Ortografia'),
    ('sinonimos_antonimos', 'Sinônimos e Antônimos'),
    ('encontros_vocalicos', 'Encontros Vocálicos'),
    ('digrafos', 'Dígrafos'),
    ('classificacao_silabica', 'Classificação Silábica'),
    ('encontros_consonantais', 'Encontros Consonantais'),
    ('substantivos_adjetivos', 'Substantivos e Adjetivos'),
    ('tipos_de_frase', 'Tipos de Frase'),
    ('tempos_verbais', 'Tempos Verbais'),
    ('substantivos_singular_plural', 'Substantivo Singular e Plural'),
    ('artigos', 'Artigos'),
    ('interpretacao_texto', 'Interpretação de Texto'),
]:
    total = BancoQuestao.objects.filter(disciplina=portugues, modulo=modulo).count()
    print(f"   {nome:.<32} {total}")
