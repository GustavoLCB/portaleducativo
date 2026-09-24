"""
popular_ingles_feelings_grammar.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ingles_feelings_grammar.py

Popula o banco com o novo card de Inglês:
  - feelings_grammar (ING - Feelings (Grammar))

Baseado nas folhas da Profª Sônia Fonseca:
  - "Unit 6 - Grammar 1" (23/09/2026): How are you? → I'm / We're +
    adjective; He/She looks...
  - "Unit 6 - Feelings - pages 96 & 97" (21/09/2026): Is he/she...?
    No. He's/She's...

O card abre com um QUADRO EXPLICATIVO (está no template
ingles_quiz.html) e depois sorteia 12 questões misturando:
  - múltipla escolha
  - questões de DIGITAR (com "word bank" mostrando as opções)
  - rostinhos em SVG mostrando cada sentimento

Pode rodar de novo sem problema — não duplica questões existentes
(usa update_or_create com a chave disciplina + modulo + enunciado).
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'feelings_grammar'


def criar_questao(disciplina, enunciado, resposta, opcoes, modo='multipla_escolha', aceitas=None, svg=''):
    extras = {'opcoes': opcoes}
    if modo == 'digitar':
        extras['modo'] = 'digitar'
        extras['banco'] = list(opcoes)
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
    print(f"  {status} {marca} {enunciado[:60]}")


print("\n🇬🇧 Garantindo disciplina Inglês...")
ingles, _ = Disciplina.objects.get_or_create(nome='ingles', defaults={'nome_exibicao': 'Inglês'})
print("  ✅ Inglês pronto.")


# ══════════════════════════════════════════════════════════════════
# 1) MÚLTIPLA ESCOLHA — How are you? / I'm / We're / looks
# ══════════════════════════════════════════════════════════════════
print("\n🔘 Múltipla escolha...")
multipla = [
    ('"How are you?" — Which answer is correct?', "I'm fine.",
     ["I'm fine.", "I fine.", "I is fine.", "Me fine."]),
    ('"I\'m" is the short form of...', "I am",
     ["I am", "I is", "I are", "It am"]),
    ('"We\'re" is the short form of...', "We are",
     ["We are", "We is", "We am", "Were"]),
    ('Complete: "How ___ you?"', "are",
     ["are", "is", "am", "be"]),
    ('Complete: "We ___ great!"', "are",
     ["are", "is", "am", "be"]),
    ('Complete: "I ___ OK."', "am",
     ["am", "is", "are", "be"]),
    ('Put in order: you? / How / are', "How are you?",
     ["How are you?", "Are how you?", "You how are?", "How you are?"]),
    ('Put in order: great! / I\'m', "I'm great!",
     ["I'm great!", "Great I'm!", "I great'm!", "I'm is great!"]),
    ('Complete: "He ___ tired."', "looks",
     ["looks", "look", "looking", "are look"]),
    ('Complete: "You ___ angry."', "look",
     ["look", "looks", "is look", "are looks"]),
    ('Complete: "She ___ happy. She\'s always smiling."', "looks",
     ["looks", "look", "are look", "am look"]),
    ('"You look angry." — "No. I\'m ___." (Eu estou entediado.)', "bored",
     ["bored", "angry", "hungry", "great"]),
    ('"He looks tired." — "Yes. He\'s ___." (Ele está ocupado.)', "busy",
     ["busy", "happy", "silly", "thirsty"]),
    ('"He looks happy." — "Yes. He\'s always ___."', "smiling",
     ["smiling", "crying", "sleeping", "eating"]),
    ('Tom is eating a big sandwich. Why?', "He's hungry.",
     ["He's hungry.", "He's thirsty.", "He's scared.", "He's bored."]),
    ('Ana wants a glass of water. How does she feel?', "She's thirsty.",
     ["She's thirsty.", "She's hungry.", "She's silly.", "She's angry."]),
    ('Leo is yawning (bocejando). How does he look?', "He looks tired.",
     ["He looks tired.", "He looks excited.", "He looks angry.", "He looks surprised."]),
    ('Mia sees a big spider! How does she feel?', "She's scared.",
     ["She's scared.", "She's hungry.", "She's bored.", "She's fine."]),
    ('Tomorrow is Ben\'s birthday party! How does he feel?', "He's excited.",
     ["He's excited.", "He's bored.", "He's tired.", "He's worried."]),
    ('"Is he silly?" — Short answer (resposta curta) for YES:', "Yes, he is.",
     ["Yes, he is.", "Yes, he are.", "Yes, is he.", "Yes, he am."]),
    ('"Are they tired?" — Short answer for NO:', "No, they aren't.",
     ["No, they aren't.", "No, they isn't.", "No, they am not.", "No, are they."]),
    ('"worried" means...', "preocupado",
     ["preocupado", "com fome", "animado", "bobo"]),
    ('"silly" means...', "bobo / brincalhão",
     ["bobo / brincalhão", "com medo", "cansado", "com sede"]),
]
for enunciado, resposta, opcoes in multipla:
    criar_questao(ingles, enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# 2) ROSTINHOS EM SVG — múltipla escolha
#    (cada pergunta usa um NOME diferente → enunciado único no banco)
# ══════════════════════════════════════════════════════════════════
print("\n😊 Rostinhos (múltipla escolha)...")
rostos_mc = [
    ('Look at Kate. How does she look?', "She looks angry.", 'angry',
     ["She looks angry.", "She looks happy.", "She looks tired.", "She looks thirsty."]),
    ('Look at Paul. How does he look?', "He looks surprised.", 'surprised',
     ["He looks surprised.", "He looks bored.", "He looks hungry.", "He looks angry."]),
    ('Look at Lily. How does she look?', "She looks tired.", 'tired',
     ["She looks tired.", "She looks excited.", "She looks silly.", "She looks scared."]),
    ('Look at Max. How does he look?', "He looks excited.", 'excited',
     ["He looks excited.", "He looks worried.", "He looks bored.", "He looks tired."]),
    ('Look at Emma. How does she look?', "She looks worried.", 'worried',
     ["She looks worried.", "She looks happy.", "She looks hungry.", "She looks excited."]),
    ('Look at Sam. How does he look?', "He looks silly.", 'silly',
     ["He looks silly.", "He looks angry.", "He looks scared.", "He looks tired."]),
    ('Look at Nina. Is she happy?', "No. She's scared.", 'scared',
     ["No. She's scared.", "Yes, she is.", "No. She's hungry.", "No. She's great."]),
    ('Look at Jack. Is he angry?', "No. He's bored.", 'bored',
     ["No. He's bored.", "Yes, he is.", "No. He's excited.", "No. He's thirsty."]),
]
for enunciado, resposta, sentimento, opcoes in rostos_mc:
    criar_questao(ingles, enunciado, resposta, opcoes, svg='rosto:' + sentimento)


# ══════════════════════════════════════════════════════════════════
# 3) DIGITAR — com rostinhos (modelo da folha "Feelings":
#    "Is he hungry? No. He's thirsty.")
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Digitar (rostinhos)...")
rostos_digitar = [
    ('Is he hungry? No. He\'s ______.\n(Look at Tim and type the feeling.)', "thirsty", 'thirsty',
     ["thirsty", "hungry", "bored", "silly"]),
    ('Is she scared? No. She\'s ______.\n(Look at Sara and type the feeling.)', "angry", 'angry',
     ["angry", "scared", "tired", "fine"]),
    ('Is she angry? No. She\'s ______.\n(Look at Julia and type the feeling.)', "scared", 'scared',
     ["scared", "angry", "hungry", "happy"]),
    ('Is he silly? No. He\'s ______.\n(Look at Tony and type the feeling.)', "surprised", 'surprised',
     ["surprised", "silly", "thirsty", "bored"]),
    ('Is he surprised? No. He\'s ______.\n(Look at Dan and type the feeling.)', "bored", 'bored',
     ["bored", "surprised", "excited", "hungry"]),
    ('Is he bored? No. He\'s ______.\n(Look at Gabe and type the feeling.)', "hungry", 'hungry',
     ["hungry", "bored", "worried", "scared"]),
    ('Is she excited? No. She\'s ______.\n(Look at Bia and type the feeling.)', "worried", 'worried',
     ["worried", "excited", "silly", "thirsty"]),
    ('Is she worried? No. She\'s ______.\n(Look at Clara and type the feeling.)', "tired", 'tired',
     ["tired", "worried", "angry", "happy"]),
    ('Is he tired? No. He\'s ______.\n(Look at Nick and type the feeling.)', "excited", 'excited',
     ["excited", "tired", "scared", "bored"]),
    ('Is she sad? No. She\'s ______.\n(Look at Amy and type the feeling.)', "happy", 'happy',
     ["happy", "sad", "worried", "hungry"]),
    ('Is he scared? No. He\'s ______.\n(Look at Ryan and type the feeling.)', "silly", 'silly',
     ["silly", "scared", "angry", "tired"]),
]
for enunciado, resposta, sentimento, opcoes in rostos_digitar:
    criar_questao(ingles, enunciado, resposta, opcoes, modo='digitar', svg='rosto:' + sentimento)


# ══════════════════════════════════════════════════════════════════
# 4) DIGITAR — frases (ordenar palavras / completar)
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Digitar (frases)...")
frases_digitar = [
    # Ordenar palavras (folha Grammar 1, exercício 2) — o "banco" mostra as palavras soltas
    ('Write the words in the correct order:\nyou?  /  How  /  are', "How are you?",
     ["you?", "How", "are"], []),
    ('Write the words in the correct order:\ngreat!  /  I\'m', "I'm great!",
     ["great!", "I'm"], ["I am great"]),
    ('Write the words in the correct order:\nOK.  /  We\'re', "We're OK.",
     ["OK.", "We're"], ["We are OK", "We're okay", "We are okay"]),
    ('Write the words in the correct order:\nam  /  I  /  fine.', "I am fine.",
     ["am", "I", "fine."], []),
    ('Write the words in the correct order:\nlooks  /  She  /  happy.', "She looks happy.",
     ["looks", "She", "happy."], []),
    ('Write the words in the correct order:\nhe  /  Is  /  hungry?', "Is he hungry?",
     ["he", "Is", "hungry?"], []),
    # Completar com look / looks
    ('Complete with LOOK or LOOKS:\nHe ______ tired.', "looks",
     ["look", "looks"], ["he looks tired"]),
    ('Complete with LOOK or LOOKS:\nThey ______ happy.', "look",
     ["look", "looks"], ["they look happy"]),
    ('Complete with I\'M or WE\'RE:\nMy friends and I are at the park. ______ great!', "We're",
     ["I'm", "We're"], ["We are", "We're great", "We are great"]),
]
for enunciado, resposta, banco, aceitas in frases_digitar:
    BancoQuestao.objects.update_or_create(
        disciplina=ingles, modulo=MODULO, enunciado=enunciado,
        defaults={
            'tipo': 'completar_frase',
            'resposta_correta': resposta,
            'dados_extras': {
                'modo': 'digitar', 'banco': banco, 'aceitas': aceitas,
                # opções da Prova Multidisciplinar: a certa + erradas parecidas
                'opcoes': [resposta] + {
                    "How are you?": ["Are how you?", "You how are?"],
                    "I'm great!": ["Great I'm!", "I great'm!"],
                    "We're OK.": ["OK we're.", "We OK're."],
                    "I am fine.": ["Am I fine.", "I fine am."],
                    "She looks happy.": ["She happy looks.", "Looks she happy."],
                    "Is he hungry?": ["He is hungry?", "Hungry is he?"],
                    "looks": ["look", "looking"],
                    "look": ["looks", "looking"],
                    "We're": ["I'm", "He's"],
                }[resposta],
            },
            'ativo': True,
        }
    )
    print(f"  ✅ ⌨️  {enunciado.splitlines()[-1][:60]}")


# ══════════════════════════════════════════════════════════════════
# 5) DIGITAR — traduzir o sentimento (português → inglês)
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Digitar (traduzir sentimentos)...")
traduzir = [
    ('com fome', 'hungry', ['hungry', 'thirsty', 'happy', 'tired']),
    ('com sede', 'thirsty', ['thirsty', 'hungry', 'silly', 'scared']),
    ('cansado', 'tired', ['tired', 'bored', 'angry', 'excited']),
    ('entediado', 'bored', ['bored', 'tired', 'worried', 'happy']),
    ('bravo / zangado', 'angry', ['angry', 'scared', 'hungry', 'silly']),
    ('com medo', 'scared', ['scared', 'surprised', 'angry', 'fine']),
    ('surpreso', 'surprised', ['surprised', 'scared', 'excited', 'bored']),
    ('animado / empolgado', 'excited', ['excited', 'happy', 'worried', 'tired']),
    ('preocupado', 'worried', ['worried', 'angry', 'thirsty', 'silly']),
    ('bobo / brincalhão', 'silly', ['silly', 'scared', 'bored', 'hungry']),
    ('feliz', 'happy', ['happy', 'hungry', 'tired', 'angry']),
    ('bem', 'fine', ['fine', 'tired', 'scared', 'thirsty']),
]
for portugues, resposta, opcoes in traduzir:
    criar_questao(ingles, f'Type the feeling in English:\n"{portugues}"', resposta, opcoes, modo='digitar')

# DIGITAR — responder "How are you?" com uma frase completa
print("\n⌨️  Digitar (How are you?)...")
como_voce_esta = [
    ('Anna is very well today.\n"How are you, Anna?" — Type her answer (use I\'m + great).', "I'm great.",
     ["I'm great.", "I'm tired.", "I'm hungry."], ["I am great", "I'm great!"]),
    ('Pedro wants to sleep.\n"How are you, Pedro?" — Type his answer (use I\'m).', "I'm tired.",
     ["I'm tired.", "I'm great.", "I'm hungry."], ["I am tired"]),
    ('Tom and Sue want to eat pizza.\n"How are you?" — Type their answer (use We\'re).', "We're hungry.",
     ["We're hungry.", "We're thirsty.", "We're tired."], ["We are hungry"]),
    ('Carla is OK.\n"How are you, Carla?" — Type her answer (use I\'m + fine).', "I'm fine.",
     ["I'm fine.", "I'm scared.", "I'm bored."], ["I am fine", "I'm fine, thanks", "I'm fine, thank you"]),
]
for enunciado, resposta, opcoes, aceitas in como_voce_esta:
    criar_questao(ingles, enunciado, resposta, opcoes, modo='digitar', aceitas=aceitas)

total = BancoQuestao.objects.filter(disciplina=ingles, modulo=MODULO).count()
print(f"\n🎉 Pronto! O card 'ING - Feelings (Grammar)' tem {total} questões.")
