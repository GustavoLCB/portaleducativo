"""
popular_ingles_story_busy_saturday.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ingles_story_busy_saturday.py

Popula o banco com o card de Inglês:
  - story_busy_saturday (ING - Story: A Busy Saturday)

O card abre com um texto curto (9 linhas, está no template
ingles_quiz.html) e depois sorteia 12 questões — pelo menos 9 delas
de DIGITAR — sobre:
  - HORÁRIOS (resposta com AT e número: "At 8:00 a.m.")
  - SENTIMENTOS (hungry, thirsty, excited, scared, happy, great, silly, tired)
  - HE'S / SHE'S / THEY'RE / YOU'RE / I'M
  - Respostas curtas: Yes, he is. / No, they aren't.
  - How are you? — I'm great!

Texto "A Busy Saturday" (criado para o Portal):
  1. It's Saturday. Tom and his sister Lily get up at 8:00 a.m.
  2. Tom is hungry, so he eats cereal and milk. Lily is thirsty. She drinks orange juice.
  3. At 10:00 a.m., they go to the park with Dad. They're very excited!
  4. Lily sees a big dog and she's scared. "Don't worry, Lily. He's friendly!" says Dad.
  5. At 12:00 p.m., they eat sandwiches under a tree. They're happy.
  6. At 3:00 p.m., Tom's friend Ben arrives. "How are you, Ben?" "I'm great, thanks!"
  7. Ben makes funny faces. He's silly! Everybody laughs.
  8. At 5:00 p.m., Dad looks at his watch. "You're tired, kids. Let's go home!"
  9. At 9:00 p.m., Tom and Lily go to bed. What a great day!

SE MUDAR O TEXTO: altere também o bloco 'story_busy_saturday' dentro
de core/templates/ingles_quiz.html.

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'story_busy_saturday'


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


# ══════════════════════════════════════════════════════════════════
# 1) HORÁRIOS — digitar com AT + número
# ══════════════════════════════════════════════════════════════════
print("\n🕘 Horários (digitar)...")
horarios = [
    ('What time do Tom and Lily get up?', 8, 'a.m.', [(10, 'a.m.'), (8, 'p.m.')]),
    ('What time do they go to the park?', 10, 'a.m.', [(8, 'a.m.'), (12, 'p.m.')]),
    ('What time do they eat sandwiches?', 12, 'p.m.', [(10, 'a.m.'), (3, 'p.m.')]),
    ('What time does Ben arrive?', 3, 'p.m.', [(5, 'p.m.'), (12, 'p.m.')]),
    ('What time does Dad look at his watch?', 5, 'p.m.', [(3, 'p.m.'), (9, 'p.m.')]),
    ('What time do Tom and Lily go to bed?', 9, 'p.m.', [(5, 'p.m.'), (8, 'a.m.')]),
]
for pergunta, hora, periodo, erradas in horarios:
    resposta = f"At {hora}:00 {periodo}"
    opcoes = [resposta] + [f"At {h}:00 {p}" for h, p in erradas]
    criar_questao(ingles, pergunta + '\nAnswer with AT and NUMBERS.', resposta, opcoes,
                  modo='digitar', aceitas=formas_do_horario(hora, periodo))

# Relógio desenhado → o que eles fazem nesse horário?
relogio_atividade = [
    ('relogio:10:00', 'Look at the clock (it\'s the morning).\nWhere do Tom and Lily go at this time?', "to the park",
     ["the park", "go to the park", "they go to the park", "park"], ["to school", "to bed"]),
    ('relogio:9:00', 'Look at the clock (it\'s the night).\nWhat do Tom and Lily do at this time?', "go to bed",
     ["they go to bed", "go to sleep", "sleep"], ["get up", "eat sandwiches"]),
    ('digital:3:00', 'Look at the clock (it\'s the afternoon).\nWho arrives at this time?', "Ben",
     ["Ben arrives", "Tom's friend Ben", "Tom's friend"], ["Dad", "Lily"]),
]
for svg, enunciado, resposta, aceitas, erradas in relogio_atividade:
    criar_questao(ingles, enunciado, resposta, [resposta] + erradas, modo='digitar',
                  aceitas=aceitas, svg=svg, banco=[])


# ══════════════════════════════════════════════════════════════════
# 2) SENTIMENTOS — digitar (word bank)
# ══════════════════════════════════════════════════════════════════
print("\n😊 Sentimentos (digitar)...")
SENTIMENTOS = ['hungry', 'thirsty', 'excited', 'scared', 'happy', 'great', 'silly', 'tired']
sentimentos = [
    ('Tom eats cereal and milk because he is ______.', 'hungry'),
    ('Lily drinks orange juice because she is ______.', 'thirsty'),
    ('At the park, Tom and Lily are very ______!', 'excited'),
    ('Lily sees a big dog. She is ______.', 'scared'),
    ('Under the tree, eating sandwiches, they are ______.', 'happy'),
    ('"How are you, Ben?" — "I\'m ______, thanks!"', 'great'),
    ('Ben makes funny faces. He is ______!', 'silly'),
    ('At 5:00 p.m., Dad says the kids are ______.', 'tired'),
]
for enunciado, resposta in sentimentos:
    opcoes = [resposta] + [s for s in SENTIMENTOS if s != resposta][:3]
    criar_questao(ingles, 'Complete with a feeling:\n' + enunciado, resposta, opcoes,
                  modo='digitar', banco=SENTIMENTOS,
                  aceitas=[f"he is {resposta}", f"she is {resposta}", f"they are {resposta}",
                           f"very {resposta}", f"because he is {resposta}", f"because she is {resposta}"])

# Rostinho → quem da história se sente assim? (digitar o nome)
PERSONAGENS = ['Tom', 'Lily', 'Ben', 'Dad']
rosto_quem = [
    ('scared', 'Who feels like this when the big dog comes?\nType the name.', 'Lily'),
    ('silly', 'Who makes funny faces and looks like this?\nType the name.', 'Ben'),
    ('hungry', 'Who is hungry in the morning?\nType the name.', 'Tom'),
    ('thirsty', 'Who is thirsty in the morning?\nType the name.', 'Lily'),
]
for sentimento, enunciado, resposta in rosto_quem:
    criar_questao(ingles, enunciado, resposta, [resposta] + [p for p in PERSONAGENS if p != resposta][:2],
                  modo='digitar', banco=PERSONAGENS, svg='rosto:' + sentimento)


# ══════════════════════════════════════════════════════════════════
# 3) HE'S / SHE'S / THEY'RE / YOU'RE / I'M — digitar
# ══════════════════════════════════════════════════════════════════
print("\n🧩 He's / She's / They're / You're / I'm (digitar)...")
PRONOMES = ["He's", "She's", "They're", "You're", "I'm"]
pronomes = [
    ('Lily sees a big dog. ______ scared.', "She's", ["She is", "She's scared", "She is scared"]),
    ('Tom and Lily are at the park. ______ excited.', "They're", ["They are", "They're excited", "They are excited"]),
    ('Ben makes funny faces. ______ silly.', "He's", ["He is", "He's silly", "He is silly"]),
    ('Dad talks to the kids: "______ tired, kids."', "You're", ["You are", "You're tired", "You are tired"]),
    ('Ben answers: "______ great, thanks!"', "I'm", ["I am", "I'm great", "I am great"]),
    ('Dad talks about the dog: "Don\'t worry. ______ friendly!"', "He's", ["He is", "He's friendly", "He is friendly"]),
    ('Tom is eating cereal. ______ hungry.', "He's", ["He is", "He's hungry", "He is hungry"]),
    ('Tom and Lily eat sandwiches under a tree. ______ happy.', "They're", ["They are", "They're happy", "They are happy"]),
]
for enunciado, resposta, aceitas in pronomes:
    opcoes = [resposta] + [p for p in PRONOMES if p != resposta][:3]
    criar_questao(ingles, 'Complete with He\'s, She\'s, They\'re, You\'re or I\'m:\n' + enunciado,
                  resposta, opcoes, modo='digitar', banco=PRONOMES, aceitas=aceitas)


# ══════════════════════════════════════════════════════════════════
# 4) RESPOSTAS CURTAS — Yes, he is. / No, they aren't. (digitar)
# ══════════════════════════════════════════════════════════════════
print("\n✍️  Respostas curtas (digitar)...")
CURTAS = ["Yes, he is.", "No, he isn't.", "Yes, she is.", "No, she isn't.", "Yes, they are.", "No, they aren't."]
curtas = [
    ('Is Tom hungry in the morning?', "Yes, he is.", ["Yes he is", "Yes, he's hungry", "Yes, he is hungry"]),
    ('Is Lily happy when she sees the big dog?', "No, she isn't.", ["No she isn't", "No, she is not", "No, she's scared", "No, she is scared"]),
    ('Are Tom and Lily excited at the park?', "Yes, they are.", ["Yes they are", "Yes, they're excited", "Yes, they are excited"]),
    ('Are the kids bored under the tree?', "No, they aren't.", ["No they aren't", "No, they are not", "No, they're happy", "No, they are happy"]),
    ('Is Ben silly?', "Yes, he is.", ["Yes he is", "Yes, he's silly", "Yes, he is silly"]),
    ('Is Lily thirsty in the morning?', "Yes, she is.", ["Yes she is", "Yes, she's thirsty", "Yes, she is thirsty"]),
    ('Are Tom and Lily tired at 5:00 p.m.?', "Yes, they are.", ["Yes they are", "Yes, they're tired", "Yes, they are tired"]),
    ('Is Tom scared of the dog?', "No, he isn't.", ["No he isn't", "No, he is not"]),
]
for enunciado, resposta, aceitas in curtas:
    opcoes = [resposta] + [c for c in CURTAS if c != resposta][:3]
    criar_questao(ingles, 'Short answer:\n' + enunciado, resposta, opcoes, modo='digitar',
                  banco=CURTAS, aceitas=aceitas)

# How are you?
criar_questao(ingles, 'Tom asks: "How are you, Ben?"\nType Ben\'s answer (it\'s in the text!).', "I'm great, thanks!",
              ["I'm great, thanks!", "I'm tired, thanks!", "He's great, thanks!"], modo='digitar', banco=[],
              aceitas=["I'm great", "I am great", "I am great, thanks", "I'm great thanks"])


# ══════════════════════════════════════════════════════════════════
# 5) INTERPRETAÇÃO — múltipla escolha
# ══════════════════════════════════════════════════════════════════
print("\n🔘 Interpretação (múltipla escolha)...")
interpretacao = [
    ('What day is it in the story?', "Saturday", ["Saturday", "Monday", "Sunday", "Friday"]),
    ('Who is Lily?', "Tom's sister", ["Tom's sister", "Tom's mom", "Ben's sister", "Tom's teacher"]),
    ('Who goes to the park with Tom and Lily?', "Dad", ["Dad", "Mom", "Ben", "Grandma"]),
    ('What does Lily drink in the morning?', "Orange juice", ["Orange juice", "Milk", "Water", "Soda"]),
    ('Where do they eat sandwiches?', "Under a tree", ["Under a tree", "At school", "In the kitchen", "In the car"]),
    ('The big dog is...', "friendly", ["friendly", "angry", "hungry", "tired"]),
    ('Why does everybody laugh?', "Ben makes funny faces.", ["Ben makes funny faces.", "The dog is silly.", "Dad is tired.", "Lily is scared."]),
]
for enunciado, resposta, opcoes in interpretacao:
    criar_questao(ingles, enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=ingles, modulo=MODULO).count()
digitar = sum(1 for e in BancoQuestao.objects.filter(disciplina=ingles, modulo=MODULO).values_list('dados_extras', flat=True)
              if (e or {}).get('modo') == 'digitar')
print(f"\n🎉 Pronto! O card 'ING - Story: A Busy Saturday' tem {total} questões ({digitar} de digitar).")
