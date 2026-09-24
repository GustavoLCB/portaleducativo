"""
popular_ingles_prova_3periodo.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ingles_prova_3periodo.py

Popula o banco com o novo card de Inglês:
  - prova_3periodo (ING - Prova 3º Período)

Baseado na ENGLISH EXAM - 3rd term (14/09/2026) da Profª Sônia Fonseca:
  - Texto "This is Mike" (rotina diária) — perguntas de interpretação
  - Horários da rotina do Mike — o aluno DIGITA o horário com número
    (ex.: "At 8:00 a.m.")
  - Completar frases com BREAKFAST / FAMILY / GUITAR / HOME / SINGER (digitar)
  - Casa do Mike: Where is...? It's... / Where are...? They're...
  - Questão 5: cenas desenhadas em SVG → o aluno DIGITA a atividade
  - Questão 6: relógios em SVG → o aluno DIGITA "It's ... o'clock"
  - Questão 7 (adaptada): "What time...?" com relógio → resposta com AT

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'prova_3periodo'


def criar_questao(disciplina, enunciado, resposta, opcoes, modo='multipla_escolha', aceitas=None, svg='', banco=None):
    extras = {'opcoes': opcoes}
    if modo == 'digitar':
        extras['modo'] = 'digitar'
        extras['banco'] = list(banco if banco is not None else opcoes)
    if aceitas:
        extras['aceitas'] = aceitas
    if svg:
        extras['svg'] = svg
    obj, criado = BancoQuestao.objects.update_or_create(
        disciplina=disciplina, modulo=MODULO, enunciado=enunciado,
        defaults={
            'tipo': 'completar_frase' if modo == 'digitar' else 'multipla_escolha',
            'resposta_correta': resposta,
            'dados_extras': extras,
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "🔄 Atualizado"
    marca = "⌨️ " if modo == 'digitar' else "🔘"
    print(f"  {status} {marca} {enunciado.splitlines()[0][:60]}")


def formas_do_horario(hora, periodo):
    """Outras formas aceitas para 'At 8:00 a.m.' (8 o'clock, 8 am, ...)."""
    return [
        f"At {hora}:00 {periodo}", f"At {hora} {periodo}", f"At {hora} o'clock",
        f"At {hora} o'clock {periodo}", f"At {hora}:00 o'clock {periodo}", f"At {hora}:00",
    ]


print("\n🇬🇧 Garantindo disciplina Inglês...")
ingles, _ = Disciplina.objects.get_or_create(nome='ingles', defaults={'nome_exibicao': 'Inglês'})
print("  ✅ Inglês pronto.")

TEXTO = '(Text: "This is Mike")\n'

# ══════════════════════════════════════════════════════════════════
# 1) INTERPRETAÇÃO DO TEXTO "This is Mike" — múltipla escolha
# ══════════════════════════════════════════════════════════════════
print("\n📖 Texto 'This is Mike'...")
texto_mike = [
    (TEXTO + 'How old is Mike?', "He is eight years old.",
     ["He is eight years old.", "He is nine years old.", "He is seven years old.", "He is ten years old."]),
    (TEXTO + 'Mike is a famous...', "singer",
     ["singer", "teacher", "soccer player", "doctor"]),
    (TEXTO + 'What color is Mike\'s favorite t-shirt?', "Blue",
     ["Blue", "Red", "Green", "Yellow"]),
    (TEXTO + 'What does Mike eat for breakfast?', "Milk and cereal",
     ["Milk and cereal", "Chicken salad", "Pizza", "Bread and juice"]),
    (TEXTO + 'How does Mike go to school?', "By bus",
     ["By bus", "By car", "By bike", "On foot"]),
    (TEXTO + 'What is Mike\'s favorite class?', "Music class",
     ["Music class", "Math class", "Science class", "English class"]),
    (TEXTO + 'What does Mike love to eat at lunch?', "Chicken salad",
     ["Chicken salad", "Milk and cereal", "Hamburger", "Soup"]),
    (TEXTO + 'What musical instrument does Mike play at home?', "The guitar",
     ["The guitar", "The piano", "The drums", "The violin"]),
    (TEXTO + 'What does Mike dream about?', "Big concerts",
     ["Big concerts", "Big cars", "Soccer games", "Video games"]),
    (TEXTO + 'Which sentence is TRUE?', "He goes to school by bus.",
     ["He goes to school by bus.", "He loves a red t-shirt.", "He eats lunch at home.", "He plays the piano after school."]),
    (TEXTO + 'Which sentence is FALSE?', "He eats lunch at home.",
     ["He eats lunch at home.", "Mike is a singer.", "He goes to school by bus.", "He eats dinner with his family."]),
]
for enunciado, resposta, opcoes in texto_mike:
    criar_questao(ingles, enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# 2) HORÁRIOS DO MIKE — DIGITAR com número (ex.: "At 8:00 a.m.")
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Horários do Mike (digitar)...")
horarios = [
    ('What time does Mike get up?', 7, 'a.m.', [(8, 'a.m.'), (9, 'p.m.')]),
    ('What time does Mike go to school?', 8, 'a.m.', [(7, 'a.m.'), (3, 'p.m.')]),
    ('What time does Mike eat lunch?', 12, 'p.m.', [(8, 'a.m.'), (7, 'p.m.')]),
    ('What time does Mike play with his friends?', 2, 'p.m.', [(12, 'p.m.'), (9, 'p.m.')]),
    ('What time does Mike go home?', 3, 'p.m.', [(2, 'p.m.'), (8, 'a.m.')]),
    ('What time does Mike eat dinner with his family?', 7, 'p.m.', [(7, 'a.m.'), (12, 'p.m.')]),
    ('What time does Mike go to bed?', 9, 'p.m.', [(9, 'a.m.'), (3, 'p.m.')]),
]
for pergunta, hora, periodo, erradas in horarios:
    resposta = f"At {hora}:00 {periodo}"
    opcoes = [resposta] + [f"At {h}:00 {p}" for h, p in erradas]
    criar_questao(ingles, TEXTO + pergunta + '\nType the time with NUMBERS.', resposta, opcoes,
                  modo='digitar', aceitas=formas_do_horario(hora, periodo))


# ══════════════════════════════════════════════════════════════════
# 3) COMPLETAR FRASES — BREAKFAST / FAMILY / GUITAR / HOME / SINGER (digitar)
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Completar frases (digitar)...")
BANCO_Q3 = ["breakfast", "family", "guitar", "home", "singer"]
completar = [
    ('Complete the sentence about Mike:\nMike is a famous ______.', "singer"),
    ('Complete the sentence about Mike:\nHe eats ______ in the morning.', "breakfast"),
    ('Complete the sentence about Mike:\nAfter school, he comes back ______.', "home"),
    ('Complete the sentence about Mike:\nIn the afternoon, he plays the ______.', "guitar"),
    ('Complete the sentence about Mike:\nHe has dinner with his ______.', "family"),
]
for enunciado, resposta in completar:
    opcoes = [resposta] + [p for p in BANCO_Q3 if p != resposta][:3]
    criar_questao(ingles, enunciado, resposta, opcoes, modo='digitar', banco=BANCO_Q3)


# ══════════════════════════════════════════════════════════════════
# 4) A CASA DO MIKE — Where is...? It's... / Where are...? They're...
# ══════════════════════════════════════════════════════════════════
print("\n🏠 Casa do Mike...")
casa = [
    ("In Mike's house: Where are the stairs?", "They're in the living room.",
     ["They're in the living room.", "They're in the kitchen.", "It's in the living room.", "They're in the bedroom."]),
    ("In Mike's house: Where are the toys?", "They're in the bedroom.",
     ["They're in the bedroom.", "It's in the bedroom.", "They're in the bathroom.", "They're in the kitchen."]),
    ("In Mike's house: Where is the soccer ball?", "It's in the kitchen.",
     ["It's in the kitchen.", "They're in the kitchen.", "It's in the bathroom.", "It's in the bedroom."]),
    ("In Mike's house: Where is the guitar?", "It's in the bedroom.",
     ["It's in the bedroom.", "They're in the bedroom.", "It's in the kitchen.", "It's in the bathroom."]),
    ("In Mike's house: Where are the chairs?", "They're in the kitchen.",
     ["They're in the kitchen.", "It's in the kitchen.", "They're in the living room.", "They're in the bathroom."]),
    ("In Mike's house: Where is the tub?", "It's in the bathroom.",
     ["It's in the bathroom.", "They're in the bathroom.", "It's in the kitchen.", "It's in the living room."]),
    ('Where IS the sofa? — The answer starts with...', "It's",
     ["It's", "They're", "We're", "I'm"]),
    ('Where ARE the beds? — The answer starts with...', "They're",
     ["They're", "It's", "He's", "I'm"]),
]
for enunciado, resposta, opcoes in casa:
    criar_questao(ingles, enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# 5) QUESTÃO 5 — ATIVIDADES COM CENAS EM SVG (digitar)
# ══════════════════════════════════════════════════════════════════
print("\n🖼️  Atividades com figuras (digitar)...")
atividades = [
    ('brush_teeth', "brush teeth", ["brush my teeth", "brush his teeth", "brush her teeth", "brush the teeth", "brushing teeth"],
     ["wash face", "get dressed", "go to bed"]),
    ('wash_face', "wash face", ["wash my face", "wash his face", "wash her face", "wash the face", "washing face"],
     ["brush teeth", "get dressed", "eat breakfast"]),
    ('get_dressed', "get dressed", ["getting dressed"],
     ["wash face", "go to school", "brush teeth"]),
    ('play_video_games', "play video games", ["play videogames", "play video game", "play videogame", "playing video games"],
     ["play the guitar", "play soccer", "go to bed"]),
    ('go_to_bed', "go to bed", ["going to bed"],
     ["get dressed", "go to school", "play video games"]),
    ('eat_breakfast', "eat breakfast", ["have breakfast", "eating breakfast"],
     ["go to bed", "wash face", "go to school"]),
    ('go_to_school', "go to school", ["going to school", "go to school by bus"],
     ["go to bed", "eat breakfast", "play soccer"]),
    ('play_the_guitar', "play the guitar", ["play guitar", "playing the guitar"],
     ["play soccer", "play video games", "brush teeth"]),
    ('play_soccer', "play soccer", ["play football", "playing soccer"],
     ["play the guitar", "go to school", "play video games"]),
]
for i, (cena, resposta, aceitas, erradas) in enumerate(atividades, start=1):
    enunciado = f'Picture {i}: Write the activity according to the picture.'
    criar_questao(ingles, enunciado, resposta, [resposta] + erradas, modo='digitar',
                  aceitas=aceitas, svg='cena:' + cena)


# ══════════════════════════════════════════════════════════════════
# 6) QUESTÃO 6 — RELÓGIOS EM SVG: "What time is it?" (digitar)
# ══════════════════════════════════════════════════════════════════
print("\n🕘 Relógios (digitar)...")
NOMES_HORAS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
               8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}
relogios = [
    ('A', 'relogio:9:00', 9), ('B', 'relogio:2:00', 2), ('C', 'digital:11:00', 11),
    ('D', 'digital:12:00', 12), ('E', 'relogio:5:00', 5), ('F', 'relogio:3:00', 3), ('G', 'digital:7:00', 7),
]
for letra, svg, hora in relogios:
    nome = NOMES_HORAS[hora]
    resposta = f"It's {nome} o'clock."
    aceitas = [f"It's {hora} o'clock", f"It's {hora}:00", f"It's {hora}", f"{nome} o'clock", f"{hora} o'clock", f"{hora}:00"]
    erradas = [f"It's {NOMES_HORAS[(hora % 12) + 1]} o'clock.", f"It's {NOMES_HORAS[((hora + 5) % 12) + 1]} o'clock."]
    criar_questao(ingles, f'Clock {letra}: What time is it?', resposta, [resposta] + erradas,
                  modo='digitar', aceitas=aceitas, svg=svg)

# Diferença entre "What time is it?" (It's...) e "When / What time do you...?" (At...)
print("\n🔘 It's x At...")
its_x_at = [
    ('"What time is it?" — Choose the correct answer:', "It's nine o'clock.",
     ["It's nine o'clock.", "At nine o'clock a.m.", "At nine.", "In nine o'clock."]),
    ('"When do you play with friends?" — Choose the correct answer:', "At two o'clock p.m.",
     ["At two o'clock p.m.", "It's two o'clock.", "Two it's o'clock.", "In two o'clock."]),
    ('"When does he go to bed on Saturdays?" — Choose the correct answer:', "At eleven o'clock p.m.",
     ["At eleven o'clock p.m.", "It's eleven o'clock.", "Eleven at o'clock.", "On eleven o'clock."]),
    ('"What time does she have lunch?" — Choose the correct answer:', "At twelve o'clock p.m.",
     ["At twelve o'clock p.m.", "It's twelve o'clock.", "In twelve o'clock.", "Twelve it's."]),
]
for enunciado, resposta, opcoes in its_x_at:
    criar_questao(ingles, enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# 7) QUESTÃO 7 (adaptada) — rotina do Lucas: relógio + resposta com AT (digitar)
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Rotina com relógio (digitar)...")
rotina = [
    ('Look at the clock. It\'s Saturday and it\'s the afternoon.\nWhat time does Lucas eat lunch?\nAnswer with AT and NUMBERS.', 'digital:1:00', 1, 'p.m.'),
    ('Look at the clock. It\'s Wednesday morning.\nWhat time does Lucas get up?\nAnswer with AT and NUMBERS.', 'relogio:6:00', 6, 'a.m.'),
    ('Look at the clock. It\'s Monday morning.\nWhat time does Lucas go to school?\nAnswer with AT and NUMBERS.', 'relogio:7:00', 7, 'a.m.'),
    ('Look at the clock. It\'s night.\nWhat time does Lucas go to bed?\nAnswer with AT and NUMBERS.', 'digital:9:00', 9, 'p.m.'),
]
for enunciado, svg, hora, periodo in rotina:
    resposta = f"At {hora}:00 {periodo}"
    outro = 'p.m.' if periodo == 'a.m.' else 'a.m.'
    opcoes = [resposta, f"At {hora}:00 {outro}", f"At {(hora % 12) + 1}:00 {periodo}"]
    criar_questao(ingles, enunciado, resposta, opcoes, modo='digitar',
                  aceitas=formas_do_horario(hora, periodo), svg=svg)

total = BancoQuestao.objects.filter(disciplina=ingles, modulo=MODULO).count()
print(f"\n🎉 Pronto! O card 'ING - Prova 3º Período' tem {total} questões.")
