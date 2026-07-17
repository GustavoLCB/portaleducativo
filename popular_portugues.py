"""
popular_portugues.py
----------------------
Execute na raiz do projeto:
    python popular_portugues.py

Popula o banco com questões de Português em 5 módulos:
  - ortografia (C, SS, XC, S, SC, G, J...)
  - sinonimos_antonimos
  - encontros_vocalicos (ditongo, hiato, tritongo)
  - digrafos
  - classificacao_silabica (tonicidade e número de sílabas)

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
    obj, criado = BancoQuestao.objects.get_or_create(
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
    status = "✅" if criado else "⏭️ "
    print(f"  {status} {enunciado[:65]}")


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
    ('PROFE___OR (o ___ da turma é gentil)', 'SS', ['SS', 'S', 'C', 'Ç']),
    ('A___ADO (o menino ficou muito a___ado)', 'SS', ['SS', 'S', 'C', 'X']),
    ('VIA___EM (fizemos uma linda via___em)', 'G', ['G', 'J', 'X', 'CH']),
    ('JI___OIA (a ji___oia é um réptil)', 'B', ['B', 'V', 'P', 'F']),
    ('EN___AME (o en___ame de abelhas voou)', 'X', ['X', 'CH', 'S', 'Z']),
    ('___ARRAFA (a ___arrafa é um animal alto)', 'G', ['G', 'J', 'X', 'C']),
    ('CO___EGAR (vamos co___egar a atividade)', 'M', ['M', 'N', 'MB', 'NH']),
    ('___ÍCARA (tomei leite na ___ícara)', 'X', ['X', 'CH', 'S', 'SS']),
    ('DE___ER (é gostoso o de___er de chocolate)', 'SS', ['SS', 'S', 'C', 'Ç']),
    ('EMBAI___ADA (a bola ficou embai___ada)', 'X', ['X', 'CH', 'SS', 'S']),
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
]:
    total = BancoQuestao.objects.filter(disciplina=portugues, modulo=modulo).count()
    print(f"   {nome:.<32} {total}")
