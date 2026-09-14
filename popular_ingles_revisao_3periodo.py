"""
popular_ingles_revisao_3periodo.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ingles_revisao_3periodo.py

Popula o banco com o novo módulo de Inglês:
  - revisao_3periodo (ING - Revisão 3º Período)

Baseado no material de revisão de 09/09/2026 da Profª Sônia Fonseca
("A Different Pair of Eyes" — texto sobre a cachorra-guia Ginny e
Laura) e na ficha de prática extra do Lucas, cobrindo:
  - Reading comprehension (texto "A Different Pair of Eyes")
  - Perguntas com WHERE e respostas com IT'S / THEY'RE
  - Favorite room (there is / there are)
  - Rotina diária (daily routine activities)
  - Horas com o'clock (telling time)
  - Partes do dia (morning, afternoon, evening, night)

Mesmo padrão do popular_ciencias_revisao_3periodo.py — pode rodar de
novo sem problema, não duplica questões existentes (usa
update_or_create).
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_questao(disciplina, modulo, enunciado, resposta, opcoes):
    obj, criado = BancoQuestao.objects.update_or_create(
        disciplina=disciplina, modulo=modulo, enunciado=enunciado,
        defaults={
            'tipo': 'multipla_escolha',
            'resposta_correta': resposta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "🔄 Atualizado"
    print(f"  {status} {enunciado[:65]}")


print("\n🇬🇧 Garantindo disciplina Inglês...")
ingles, _ = Disciplina.objects.get_or_create(
    nome='ingles', defaults={'nome_exibicao': 'Inglês'}
)
print("  ✅ Inglês pronto.")


# ══════════════════════════════════════════════════════════════════
# MÓDULO NOVO — REVISÃO 3º PERÍODO
# ══════════════════════════════════════════════════════════════════
print("\n📝 Populando: Inglês › Revisão 3º Período...")

revisao_3periodo = [
    # ── Reading comprehension: "A Different Pair of Eyes" ──
    ('Read: "This is Ginny the Labrador. She is very smart and happy." What kind of dog is Ginny?', 'A Labrador',
     ['A Labrador', 'A Poodle', 'A Bulldog', 'A Pug']),
    ('Read: "Laura is blind and Ginny is her guide dog." What is Ginny\'s job?', "She is Laura's guide dog",
     ["She is Laura's guide dog", 'She is a police dog', 'She is a farm dog', 'She is a race dog']),
    ('Read: "Ginny lives with Laura in Liverpool." Where do Ginny and Laura live?', 'In Liverpool',
     ['In Liverpool', 'In London', 'In Manchester', 'In Leeds']),
    ('Read: "In the morning, Ginny gets up at 7 o\'clock and helps Laura get dressed." What time does Ginny get up?', "At 7 o'clock",
     ["At 7 o'clock", "At 8 o'clock", "At 6 o'clock", "At 10 o'clock"]),
    ('Read: "Then, they eat breakfast and walk to school together at 8 o\'clock." What do Laura and Ginny do at 8 o\'clock?', 'They walk to school',
     ['They walk to school', 'They eat dinner', 'They go to bed', 'They play tennis']),
    ('Read: "In the afternoon, Laura plays tennis at a tennis club for blind players." Where does Laura play tennis?', 'At a tennis club for blind players',
     ['At a tennis club for blind players', 'At school', 'At the park', 'At home']),
    ('Read: "After that, Laura runs in a park and Ginny runs with her." What do Laura and Ginny do after tennis?', 'They run in a park',
     ['They run in a park', 'They eat lunch', 'They watch TV', 'They go to school']),
    ('Read: "At 6 o\'clock, Laura and her family eat dinner, Ginny eats dog food and she loves it." What time does the family eat dinner?', "At 6 o'clock",
     ["At 6 o'clock", "At 7 o'clock", "At 8 o'clock", "At 10 o'clock"]),
    ('Read: "After dinner, Laura does homework and Ginny relaxes on the sofa." What does Ginny do while Laura does homework?', 'She relaxes on the sofa',
     ['She relaxes on the sofa', 'She goes to school', 'She plays tennis', 'She eats breakfast']),
    ('Read: "At 10 o\'clock at night, they go to bed." What time do Laura and Ginny go to bed?', "At 10 o'clock",
     ["At 10 o'clock", "At 6 o'clock", "At 8 o'clock", "At 7 o'clock"]),
    ('Read: "Laura has many friends but Ginny is the best." According to the text, who is Laura\'s best friend?', 'Ginny',
     ['Ginny', "Laura's teacher", 'Another dog', "Laura's neighbor"]),

    # ── WHERE questions + IT'S / THEY'RE ──
    ('Complete: "____ is the bed?" — "It\'s in the bedroom."', 'Where',
     ['Where', 'What', 'When', 'Who']),
    ('"Where is the stove?" — "____ in the kitchen."', "It's",
     ["It's", "They're", "He's", "We're"]),
    ('There is ONE refrigerator in the kitchen. Complete: "Where is the refrigerator?" — "____ in the kitchen."', "It's",
     ["It's", "They're", "I'm", "You're"]),
    ('There are TWO chairs next to the table. Complete: "Where are the chairs?" — "____ next to the table."', "They're",
     ["They're", "It's", "She's", "I'm"]),
    ('Complete: "Where ____ the books?" — "They\'re on the shelf."', 'are',
     ['are', 'is', 'do', 'does']),
    ('Complete: "Where ____ the lamp?" — "It\'s on the desk."', 'is',
     ['is', 'are', 'do', 'does']),
    ('Which question is correct?', 'Where is the sofa?',
     ['Where is the sofa?', 'Where the sofa is?', 'Sofa where is?', 'Is where the sofa?']),
    ('"Is there an armchair in the living room?" — "Yes, ____ is."', 'there',
     ['there', 'it', 'they', 'this']),

    # ── Favorite room ──
    ('Complete: "My favorite room is the ____ because I sleep there."', 'bedroom',
     ['bedroom', 'garage', 'garden', 'street']),
    ('Which sentence is correct for talking about ONE object in a room?', 'There is a bed in my room.',
     ['There is a bed in my room.', 'There are a bed in my room.', 'There a bed is in my room.', 'Is there a bed my room.']),
    ('Which sentence is correct for talking about MORE than one object in a room?', 'There are two windows in my room.',
     ['There are two windows in my room.', 'There is two windows in my room.', 'There windows are two in my room.', 'Two windows there are in my room.']),
    ('Complete: "I like to ____ books in my favorite room."', 'read',
     ['read', 'reads', 'reading', 'readed']),
    ('Complete: "There ____ a TV and a sofa in my living room."', 'is',
     ['is', 'are', 'am', 'be']),

    # ── Daily routine activities ──
    ('Which activity do we usually do first, right after waking up?', 'Get up',
     ['Get up', 'Go to bed', 'Eat dinner', 'Play video games']),
    ('Complete: "I ____ my teeth every morning."', 'brush',
     ['brush', 'wash', 'eat', 'play']),
    ('Complete: "I ____ my face before breakfast."', 'wash',
     ['wash', 'brush', 'eat', 'play']),
    ('Complete: "In the morning, I ____ breakfast."', 'eat',
     ['eat', 'sleep', 'play', 'wash']),
    ('Which activity is usually done in the evening, after school?', 'Play video games',
     ['Play video games', 'Get up', 'Go to school', 'Wash my face']),
    ('Complete: "I play ____ my friends after school."', 'with',
     ['with', 'at', 'in', 'for']),

    # ── Telling time (o'clock) ──
    ('Complete: "____ is it?" — "It\'s two o\'clock."', 'What time',
     ['What time', 'When', 'Where', 'Who']),
    ('Complete: "____ does he play soccer?" — "At four o\'clock on Friday."', 'When',
     ['When', 'What time', 'Where', 'Who']),
    ('Complete: "I get up ____ seven o\'clock."', 'at',
     ['at', "it's", 'in', 'on']),
    ('Complete: "____ twelve o\'clock. I\'m eating lunch."', "It's",
     ["It's", 'At', 'In', 'On']),
    ('How do we say 3:00 in English?', "Three o'clock",
     ["Three o'clock", 'Three hours', 'Three past', 'Three time']),

    # ── Parts of the day ──
    ('Which part of the day comes right after "morning"?', 'Afternoon',
     ['Afternoon', 'Evening', 'Night', 'Dawn']),
    ('Which part of the day do we usually go to bed?', 'Night',
     ['Night', 'Morning', 'Afternoon', 'Noon']),
    ('Complete: "We usually eat breakfast in the ____."', 'morning',
     ['morning', 'afternoon', 'evening', 'night']),
    ('Put in the correct order: morning → ____ → evening → night.', 'afternoon',
     ['afternoon', 'dawn', 'midnight', 'noon']),
]
for enunciado, resposta, opcoes in revisao_3periodo:
    criar_questao(ingles, 'revisao_3periodo', enunciado, resposta, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE INGLÊS › REVISÃO 3º PERÍODO CONCLUÍDA!")
print("=" * 55)
total = BancoQuestao.objects.filter(disciplina=ingles, modulo='revisao_3periodo').count()
print(f"   {'Revisão 3º Período':.<32} {total}")
