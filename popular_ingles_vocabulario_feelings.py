"""
popular_ingles_vocabulario_feelings.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ingles_vocabulario_feelings.py

Acrescenta o vocabulário de SENTIMENTOS (Unit 6 - Feelings) a dois
cards que já existem:

  - vocabulario_geral (Vocabulário Geral): 13 palavras nos dois
    sentidos (português → inglês e inglês → português) = 26 questões
    tired, bored, fine, great, happy, hungry, surprised, angry,
    excited, worried, thirsty, scared, silly

  - vocabulario_visual (Vocabulário Visual): 10 emojis → palavra.
    (fine, great e thirsty ficaram de fora do visual porque não há
    emoji que mostre isso sem confundir com "happy" — mas elas estão
    no Vocabulário Geral e no card Feelings (Grammar), com desenhos.)

Não mexe nas palavras que já existem. Pode rodar de novo sem problema.
"""

import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

print("\n🇬🇧 Garantindo disciplina Inglês...")
ingles, _ = Disciplina.objects.get_or_create(nome='ingles', defaults={'nome_exibicao': 'Inglês'})

# (inglês, português)
SENTIMENTOS = [
    ('Tired', 'cansado'), ('Bored', 'entediado'), ('Fine', 'bem'), ('Great', 'ótimo'),
    ('Happy', 'feliz'), ('Hungry', 'com fome'), ('Surprised', 'surpreso'), ('Angry', 'bravo / zangado'),
    ('Excited', 'animado / empolgado'), ('Worried', 'preocupado'), ('Thirsty', 'com sede'),
    ('Scared', 'com medo / assustado'), ('Silly', 'bobo / brincalhão'),
]


def salvar(modulo, enunciado, resposta, opcoes):
    obj, criado = BancoQuestao.objects.update_or_create(
        disciplina=ingles, modulo=modulo, enunciado=enunciado,
        defaults={
            'tipo': 'multipla_escolha',
            'resposta_correta': resposta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "🔄 Atualizado"
    print(f"  {status} [{modulo}] {enunciado[:55]}")


# Sorteio "fixo" (sempre as mesmas opções erradas a cada execução)
sorteio = random.Random(2026)

# ══════════════════════════════════════════════════════════════════
# Vocabulário Geral — português → inglês e inglês → português
# ══════════════════════════════════════════════════════════════════
print("\n📖 Vocabulário Geral › Feelings...")
for ingles_palavra, portugues in SENTIMENTOS:
    outros = [s for s in SENTIMENTOS if s[0] != ingles_palavra]
    # Evita alternativas que confundem: fine / great / happy nunca aparecem juntas
    parecidas = {'Fine', 'Great', 'Happy'}
    if ingles_palavra in parecidas:
        outros = [s for s in outros if s[0] not in parecidas]
    erradas = sorteio.sample(outros, 3)
    salvar('vocabulario_geral', f'Qual é a palavra em inglês para "{portugues}"? (sentimento)',
           ingles_palavra, [ingles_palavra] + [e[0] for e in erradas])
    erradas = sorteio.sample(outros, 3)
    salvar('vocabulario_geral', f'O que significa "{ingles_palavra.lower()}" em português?',
           portugues, [portugues] + [e[1] for e in erradas])

# ══════════════════════════════════════════════════════════════════
# Vocabulário Visual — emoji → palavra
# (emojis conferidos: nenhum deles já é usado no popular_vocabulario_visual.py)
# ══════════════════════════════════════════════════════════════════
print("\n🖼️  Vocabulário Visual › Feelings...")
VISUAL = [
    ('🥱', 'Tired'), ('😒', 'Bored'), ('😊', 'Happy'), ('🤤', 'Hungry'), ('😲', 'Surprised'),
    ('😠', 'Angry'), ('🤩', 'Excited'), ('😟', 'Worried'), ('😨', 'Scared'), ('🤪', 'Silly'),
]
ja_existentes = set(
    BancoQuestao.objects.filter(disciplina=ingles, modulo='vocabulario_visual')
    .exclude(enunciado__in=[e for e, _ in VISUAL]).values_list('enunciado', flat=True)
)
for emoji, palavra in VISUAL:
    if emoji in ja_existentes:
        print(f"  ⚠️  {emoji} já é usado por outra palavra — pulando.")
        continue
    outras = [p for _, p in VISUAL if p != palavra]
    salvar('vocabulario_visual', emoji, palavra, [palavra] + sorteio.sample(outras, 3))

print("\n🎉 Pronto! Sentimentos adicionados ao Vocabulário Geral e ao Vocabulário Visual.")
