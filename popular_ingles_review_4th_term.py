"""
popular_ingles_review_4th_term.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ingles_review_4th_term.py

Popula o banco com o card de Inglês:
  - review_4th_term (ING - Review 4th Term)

Baseado na folha "Review for the test - 4th term" (30/09/2026) da
Profª Sônia Fonseca:
  1) Texto da família do Mike — WHO IS HAPPY? (quem é feliz quando...)
  2) How are you? — I'm OK / We're fine / I am great (rostinhos)
  3) Rostos → ANGRY, EXCITED, SCARED, SURPRISED, TIRED, WORRIED
  4) HOW DO THEY LOOK? → He looks / She looks / They look + sentimento
  5) Sentimento + ação: tired → yawning, happy → smiling,
     angry → frowning, having fun → laughing, sad → crying

O card abre com o texto (está no template ingles_quiz.html) e sorteia
12 questões por partida — pelo menos 9 de DIGITAR.

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'review_4th_term'


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


print("\n🇬🇧 Garantindo disciplina Inglês...")
ingles, _ = Disciplina.objects.get_or_create(nome='ingles', defaults={'nome_exibicao': 'Inglês'})
print("  ✅ Inglês pronto.")

TEXTO = '(Text: Mike\'s family)\n'

# ══════════════════════════════════════════════════════════════════
# 1) WHO IS HAPPY? — digitar o nome (word bank)
# ══════════════════════════════════════════════════════════════════
print("\n😊 Who is happy? (digitar)...")
QUEM = ['Mike', 'Dad', 'Mom', 'Sister', 'Scooby']
quem = [
    ('Who is happy when he is playing soccer with his friends?', 'Mike', ["Mike's", 'I am']),
    ('Who is happy when he is running in the garden?', 'Scooby', ['the dog', 'Scooby the dog']),
    ('Who is happy when he is surfing?', 'Dad', ["Mike's dad", 'My dad', 'the dad', 'father']),
    ('Who is happy when she is playing with her dolls?', 'Sister', ["Mike's sister", 'My sister', 'the sister']),
    ('Who is happy when she is riding her bike?', 'Mom', ["Mike's mom", 'My mom', 'the mom', 'mother']),
]
for pergunta, resposta, aceitas in quem:
    erradas = [q for q in QUEM if q != resposta][:3]
    criar_questao(ingles, TEXTO + pergunta + '\nType the answer.', resposta, [resposta] + erradas,
                  modo='digitar', banco=QUEM, aceitas=aceitas)

# Interpretação — múltipla escolha
print("\n🔘 Interpretação (múltipla escolha)...")
interpretacao = [
    ('How old is Mike?', 'He is 8 years old.', ['He is 9 years old.', 'He is 7 years old.', 'He is 10 years old.']),
    ('Who is Scooby?', 'The family dog', ["Mike's brother", "Mike's friend", 'The family cat']),
    ('When is the whole family very happy?', 'When they are together.',
     ['When they are at school.', 'When they are sleeping.', 'When it is raining.']),
    ('What is Dad doing when he is happy?', 'Surfing', ['Riding a bike', 'Playing soccer', 'Running in the garden']),
    ('What is Mike doing when he is happy?', 'Playing soccer with his friends',
     ['Surfing', 'Playing with dolls', 'Riding a bike']),
]
for pergunta, resposta, erradas in interpretacao:
    criar_questao(ingles, TEXTO + pergunta, resposta, [resposta] + erradas)

# ══════════════════════════════════════════════════════════════════
# 2) HOW ARE YOU? — OK / fine / great (rostinhos)
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  How are you? (digitar)...")
COMO = ['OK', 'fine', 'great']
como = [
    ('bored', '"How are you?" — "I\'m tired. I\'m ______."\nLook at the face and type the word.', 'OK', ['okay', "I'm OK"]),
    ('fine', '"How are you?" — "We\'re ______."\nLook at the face and type the word.', 'fine', ["We're fine"]),
    ('great', '"You look happy!" — "Yes, it\'s my birthday. I am ______."\nLook at the face and type the word.', 'great',
     ['I am great']),
]
for rosto, enunciado, resposta, aceitas in como:
    criar_questao(ingles, enunciado, resposta, COMO, modo='digitar', banco=COMO, aceitas=aceitas, svg='rosto:' + rosto)

# ══════════════════════════════════════════════════════════════════
# 3) LOOK AT THE FACES AND WRITE THE CORRECT WORD
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Faces → word (digitar)...")
PALAVRAS = ['angry', 'excited', 'scared', 'surprised', 'tired', 'worried']
faces = [
    ('A', 'tired'), ('B', 'scared'), ('C', 'angry'), ('D', 'surprised'), ('E', 'worried'), ('F', 'excited'),
]
for letra, resposta in faces:
    erradas = [p for p in PALAVRAS if p != resposta][:3]
    criar_questao(ingles, f'Face {letra}: Look at the face and write the correct word.', resposta,
                  [resposta] + erradas, modo='digitar', banco=PALAVRAS, svg='rosto:' + resposta)

# ══════════════════════════════════════════════════════════════════
# 4) HOW DO THEY LOOK? — frase completa (digitar)
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  How do they look? (digitar a frase)...")
BANCO_FRASE = ['He looks', 'She looks', 'They look', 'bored', 'happy', 'hungry', 'thirsty', 'sad', 'silly']
frases = [
    ('Two children are holding balloons and smiling.\nHow do THEY look? Write the sentence.', 'They look happy.', 'happy',
     ['They look sad.', 'They look bored.']),
    ('A girl is crying.\nHow does SHE look? Write the sentence.', 'She looks sad.', 'sad',
     ['She looks happy.', 'He looks sad.']),
    ('A boy is thinking about chicken, with a fork and a knife.\nHow does HE look? Write the sentence.', 'He looks hungry.', 'hungry',
     ['He looks thirsty.', 'She looks hungry.']),
    ('A boy is making a funny face with his tongue out.\nHow does HE look? Write the sentence.', 'He looks silly.', 'silly',
     ['He looks sad.', 'They look silly.']),
    ('Two children are drinking water.\nHow do THEY look? Write the sentence.', 'They look thirsty.', 'thirsty',
     ['They look hungry.', 'He looks thirsty.']),
    ('A woman has her face on her hand and nothing to do.\nHow does SHE look? Write the sentence.', 'She looks bored.', 'bored',
     ['She looks silly.', 'She looks happy.']),
]
for enunciado, resposta, sentimento, erradas in frases:
    criar_questao(ingles, enunciado, resposta, [resposta] + erradas, modo='digitar', banco=BANCO_FRASE,
                  svg='rosto:' + sentimento)

# He looks / She looks / They look — múltipla escolha
print("\n🔘 looks x look (múltipla escolha)...")
look = [
    ('Complete: "Tom and Ana ______ happy."', 'look', ['looks', 'looking', 'is look']),
    ('Complete: "My sister ______ bored."', 'looks', ['look', 'are look', 'looking']),
    ('Complete: "My dad ______ tired."', 'looks', ['look', 'are look', 'am look']),
]
for enunciado, resposta, erradas in look:
    criar_questao(ingles, enunciado, resposta, [resposta] + erradas)

# ══════════════════════════════════════════════════════════════════
# 5) SENTIMENTO + AÇÃO — yawning, smiling, frowning, laughing, crying
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Feeling + action (digitar)...")
ACOES = ['yawning', 'smiling', 'frowning', 'laughing', 'crying']
acoes = [
    ('My brother is tired. He is ______.', 'yawning', 'tired'),
    ('My teacher is happy. She is ______.', 'smiling', 'happy'),
    ('My dog is angry. He is ______.', 'frowning', 'angry'),
    ('My friends are having fun. They are ______.', 'laughing', 'great'),
    ('My mom is sad. She is ______.', 'crying', 'sad'),
]
for enunciado, resposta, rosto in acoes:
    erradas = [a for a in ACOES if a != resposta][:3]
    criar_questao(ingles, 'Complete the sentence:\n' + enunciado, resposta, [resposta] + erradas,
                  modo='digitar', banco=ACOES, svg='rosto:' + rosto)

SENT = ['tired', 'happy', 'angry', 'sad']
inverso = [
    ('My brother is yawning. He is ______.', 'tired'),
    ('My teacher is smiling. She is ______.', 'happy'),
    ('My dog is frowning. He is ______.', 'angry'),
    ('My mom is crying. She is ______.', 'sad'),
]
for enunciado, resposta in inverso:
    erradas = [s for s in SENT if s != resposta]
    criar_questao(ingles, 'Type the feeling:\n' + enunciado, resposta, [resposta] + erradas,
                  modo='digitar', banco=SENT)

total = BancoQuestao.objects.filter(disciplina=ingles, modulo=MODULO).count()
digitar = sum(1 for e in BancoQuestao.objects.filter(disciplina=ingles, modulo=MODULO).values_list('dados_extras', flat=True)
              if (e or {}).get('modo') == 'digitar')
print(f"\n🎉 Pronto! O card 'ING - Review 4th Term' tem {total} questões ({digitar} de digitar).")
