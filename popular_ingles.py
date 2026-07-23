"""
popular_ingles.py
----------------------
Execute na raiz do projeto:
    python popular_ingles.py

Popula o banco com questões de Inglês em 4 módulos:
  - weather_clothes (tempo e roupas)
  - atividades_like (like to + infinitivo, do/does)
  - vocabulario_geral (objetos, animais, natureza)
  - esportes_convites (ações esportivas e convites)

Baseado no material real de Inglês do 3º ano (Colégio Santo Agostinho).
Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_questao(disciplina, modulo, enunciado, resposta, opcoes):
    obj, criado = BancoQuestao.objects.get_or_create(
        disciplina=disciplina, modulo=modulo, enunciado=enunciado,
        defaults={
            'tipo': 'multipla_escolha',
            'resposta_correta': resposta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅" if criado else "⏭️ "
    print(f"  {status} {enunciado[:65]}")


print("\n🇬🇧 Criando disciplina Inglês...")
ingles, _ = Disciplina.objects.get_or_create(
    nome='ingles', defaults={'nome_exibicao': 'Inglês'}
)
print("  ✅ Inglês pronto.")


# ══════════════════════════════════════════════════════════════════
# MÓDULO 1 — WEATHER & CLOTHES (tempo e roupas)
# ══════════════════════════════════════════════════════════════════
print("\n☀️  Populando: Inglês › Weather & Clothes...")

weather_clothes = [
    ('Qual é a palavra em inglês para "chuvoso"?', 'Rainy', ['Rainy', 'Sunny', 'Snowy', 'Windy']),
    ('Qual é a palavra em inglês para "ensolarado"?', 'Sunny', ['Sunny', 'Rainy', 'Snowy', 'Cloudy']),
    ('Qual é a palavra em inglês para "nevando"?', 'Snowy', ['Snowy', 'Sunny', 'Rainy', 'Windy']),
    ('Qual é a palavra em inglês para "com vento"?', 'Windy', ['Windy', 'Rainy', 'Sunny', 'Snowy']),
    ('Quando está "snowy" (nevando), você deve vestir:', 'A coat', ['A coat', 'A bathing suit', 'Shorts', 'Sandals']),
    ('Quando está "rainy" (chuvoso), você deve levar:', 'An umbrella', ['An umbrella', 'Sunglasses', 'A kite', 'A ball']),
    ('Qual peça de roupa cobre as mãos?', 'Gloves', ['Gloves', 'Sneakers', 'Scarf', 'Hat']),
    ('Qual é a palavra em inglês para "tênis"?', 'Sneakers', ['Sneakers', 'Sandals', 'Gloves', 'Coat']),
    ('Qual é a palavra em inglês para "casaco"?', 'Coat', ['Coat', 'Pants', 'Sweater', 'Scarf']),
    ('Qual é a palavra em inglês para "calça"?', 'Pants', ['Pants', 'Coat', 'Gloves', 'Sandals']),
    ('Qual é a palavra em inglês para "suéter"?', 'Sweater', ['Sweater', 'Umbrella', 'Sandals', 'Cap']),
    ('Qual é a palavra em inglês para "sandálias"?', 'Sandals', ['Sandals', 'Sneakers', 'Gloves', 'Coat']),
    ('"What day is today?" pergunta sobre:', 'O dia da semana', ['O dia da semana', 'O tempo/clima', 'A roupa', 'A cor']),
    ('"What\'s the weather like?" pergunta sobre:', 'O tempo/clima', ['O tempo/clima', 'O dia da semana', 'A roupa', 'A hora']),
    ('Qual é a palavra em inglês para "capa de chuva"?', 'Raincoat', ['Raincoat', 'Sweater', 'Scarf', 'Gloves']),
]
for enunciado, resposta, opcoes in weather_clothes:
    criar_questao(ingles, 'weather_clothes', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 2 — ATIVIDADES (like to + infinitivo, do/does)
# ══════════════════════════════════════════════════════════════════
print("\n🏃 Populando: Inglês › Atividades (like to)...")

atividades_like = [
    ('Complete: "I ___ to play soccer."', 'like', ['like', 'likes', 'liked', 'liking']),
    ('Complete: "She ___ to play soccer."', 'likes', ['likes', 'like', 'liked', 'liking']),
    ('"Do you like to swim?" — resposta afirmativa correta:', 'Yes, I do', ['Yes, I do', 'Yes, I like', 'Yes, I am', 'Yes, I can']),
    ('"Do you like to swim?" — resposta negativa correta:', "No, I don't", ["No, I don't", 'No, I not', 'No, I isn\'t', 'No, I doesn\'t']),
    ('"Does she like to dance?" — resposta afirmativa correta:', 'Yes, she does', ['Yes, she does', 'Yes, she do', 'Yes, she is', 'Yes, she like']),
    ('Qual é o verbo em inglês para "andar de bicicleta"?', 'Ride a bike', ['Ride a bike', 'Fly a kite', 'Jump rope', 'Skateboard']),
    ('Qual é o verbo em inglês para "andar de skate"?', 'Skateboard', ['Skateboard', 'Rollerblade', 'Ride a bike', 'Jump rope']),
    ('Qual é o verbo em inglês para "empinar pipa"?', 'Fly a kite', ['Fly a kite', 'Jump rope', 'Ride a bike', 'Play tag']),
    ('Qual é o verbo em inglês para "pular corda"?', 'Jump rope', ['Jump rope', 'Fly a kite', 'Skateboard', 'Rollerblade']),
    ('Qual é o verbo em inglês para "brincar de esconde-esconde"?', 'Play hide and seek', ['Play hide and seek', 'Play tag', 'Play a game', 'Play soccer']),
    ('Qual é o verbo em inglês para "andar de patins"?', 'Rollerblade', ['Rollerblade', 'Skateboard', 'Ride a bike', 'Jump rope']),
    ('"I like to swim. It\'s ___." (algo que você gosta)', 'fun', ['fun', 'boring', 'sad', 'difficult']),
    ('"I don\'t like to study. It\'s ___." (algo que você não gosta)', 'boring', ['boring', 'fun', 'happy', 'easy']),
    ('Complete: "___ you like to play a game?"', 'Do', ['Do', 'Does', 'Is', 'Are']),
    ('Complete: "___ he like to play baseball?"', 'Does', ['Does', 'Do', 'Is', 'Are']),
]
for enunciado, resposta, opcoes in atividades_like:
    criar_questao(ingles, 'atividades_like', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 3 — VOCABULÁRIO GERAL
# ══════════════════════════════════════════════════════════════════
print("\n📖 Populando: Inglês › Vocabulário Geral...")

vocabulario_geral = [
    ('Qual é a palavra em inglês para "escola"?', 'School', ['School', 'House', 'Classroom', 'Table']),
    ('Qual é a palavra em inglês para "gato"?', 'Cat', ['Cat', 'Dog', 'Mouse', 'Bird']),
    ('Qual é a palavra em inglês para "cachorro"?', 'Dog', ['Dog', 'Cat', 'Mouse', 'Spider']),
    ('Qual é a palavra em inglês para "lápis"?', 'Pencil', ['Pencil', 'Pen', 'Book', 'Board']),
    ('Qual é a palavra em inglês para "computador"?', 'Computer', ['Computer', 'Telephone', 'Table', 'Box']),
    ('Qual é a palavra em inglês para "aranha"?', 'Spider', ['Spider', 'Mouse', 'Bird', 'Cat']),
    ('Qual é a palavra em inglês para "lua"?', 'Moon', ['Moon', 'Sun', 'Sky', 'Earth']),
    ('Qual é a palavra em inglês para "rio"?', 'River', ['River', 'Sky', 'Moon', 'House']),
    ('Qual é a palavra em inglês para "rato/camundongo"?', 'Mouse', ['Mouse', 'Cat', 'Dog', 'Spider']),
    ('Qual é a palavra em inglês para "pássaro"?', 'Bird', ['Bird', 'Mouse', 'Spider', 'Cat']),
    ('Qual é a palavra em inglês para "sol"?', 'Sun', ['Sun', 'Moon', 'Sky', 'Earth']),
    ('Qual é a palavra em inglês para "céu"?', 'Sky', ['Sky', 'Sun', 'Moon', 'Earth']),
    ('Qual é a palavra em inglês para "casa"?', 'House', ['House', 'School', 'Classroom', 'Box']),
    ('Qual é a palavra em inglês para "avião"?', 'Airplane', ['Airplane', 'Telephone', 'Computer', 'Box']),
    ('Qual é a palavra em inglês para "telefone"?', 'Telephone', ['Telephone', 'Computer', 'Airplane', 'Board']),

    # Novas — móveis e objetos de casa
    ('Qual é a palavra em inglês para "sofá"?', 'Sofa', ['Sofa', 'Armchair', 'Chair', 'Bed']),
    ('Qual é a palavra em inglês para "poltrona"?', 'Armchair', ['Armchair', 'Sofa', 'Chair', 'Desk']),
    ('Qual é a palavra em inglês para "cadeira"?', 'Chair', ['Chair', 'Sofa', 'Armchair', 'Bed']),
    ('Qual é a palavra em inglês para "caixa de som"?', 'Speakers', ['Speakers', 'Remote control', 'Lamp', 'Fan']),
    ('Qual é a palavra em inglês para "tapete"?', 'Carpet', ['Carpet', 'Cushion', 'Mirror', 'Pillow']),
    ('Qual é a palavra em inglês para "almofada"?', 'Cushion', ['Cushion', 'Carpet', 'Pillow', 'Mirror']),
    ('Qual é a palavra em inglês para "controle remoto"?', 'Remote control', ['Remote control', 'Speakers', 'Alarm clock', 'Fan']),
    ('Qual é a palavra em inglês para "guarda-roupa"?', 'Closet', ['Closet', 'Desk', 'Bed', 'Chair']),
    ('Qual é a palavra em inglês para "escrivaninha"?', 'Desk', ['Desk', 'Closet', 'Bed', 'Chair']),
    ('Qual é a palavra em inglês para "cama"?', 'Bed', ['Bed', 'Closet', 'Desk', 'Sofa']),
    ('Qual é a palavra em inglês para "travesseiro"?', 'Pillow', ['Pillow', 'Cushion', 'Carpet', 'Mirror']),
    ('Qual é a palavra em inglês para "abajur"?', 'Lamp', ['Lamp', 'Fan', 'Speakers', 'Alarm clock']),
    ('Qual é a palavra em inglês para "espelho"?', 'Mirror', ['Mirror', 'Carpet', 'Pillow', 'Cushion']),
    ('Qual é a palavra em inglês para "ventilador"?', 'Fan', ['Fan', 'Lamp', 'Alarm clock', 'Speakers']),
    ('Qual é a palavra em inglês para "despertador"?', 'Alarm clock', ['Alarm clock', 'Fan', 'Lamp', 'Remote control']),
    ('Qual é a palavra em inglês para "lixeira"?', 'Trash', ['Trash', 'Folder', 'Backpack', 'Ruler']),

    # Novas — material escolar
    ('Qual é a palavra em inglês para "apagador/borracha"?', 'Eraser', ['Eraser', 'Ruler', 'Glue', 'Scissors']),
    ('Qual é a palavra em inglês para "régua"?', 'Ruler', ['Ruler', 'Eraser', 'Glue', 'Scissors']),
    ('Qual é a palavra em inglês para "cola"?', 'Glue', ['Glue', 'Ruler', 'Eraser', 'Folder']),
    ('Qual é a palavra em inglês para "tesoura"?', 'Scissors', ['Scissors', 'Glue', 'Ruler', 'Eraser']),
    ('Qual é a palavra em inglês para "mochila"?', 'Backpack', ['Backpack', 'Folder', 'Trash', 'Desk']),
    ('Qual é a palavra em inglês para "pasta"?', 'Folder', ['Folder', 'Backpack', 'Trash', 'Ruler']),
]
for enunciado, resposta, opcoes in vocabulario_geral:
    criar_questao(ingles, 'vocabulario_geral', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 4 — ESPORTES E CONVITES
# ══════════════════════════════════════════════════════════════════
print("\n⚽ Populando: Inglês › Esportes e Convites...")

esportes_convites = [
    ('Qual é o verbo em inglês para "jogar pega-pega"?', 'Play tag', ['Play tag', 'Catch a ball', 'Bounce a ball', 'Throw a ball']),
    ('Qual é o verbo em inglês para "pegar a bola"?', 'Catch a ball', ['Catch a ball', 'Throw a ball', 'Bounce a ball', 'Play tag']),
    ('Qual é o verbo em inglês para "quicar a bola"?', 'Bounce a ball', ['Bounce a ball', 'Catch a ball', 'Throw a ball', 'Play tag']),
    ('Qual é o verbo em inglês para "arremessar a bola"?', 'Throw a ball', ['Throw a ball', 'Catch a ball', 'Bounce a ball', 'Watch a game']),
    ('Qual é o verbo em inglês para "assistir a um jogo"?', 'Watch a game', ['Watch a game', 'Play a game', 'Throw a ball', 'Catch a ball']),
    ('"Let\'s play soccer!" — resposta de quem aceita o convite:', 'Sure. That sounds fun!', ['Sure. That sounds fun!', "No, thanks. It's boring.", 'Maybe tomorrow.', "I don't know."]),
    ('"Let\'s play soccer!" — resposta de quem recusa o convite:', "No, thanks. It's boring.", ['No, thanks. It\'s boring.', 'Sure. That sounds fun!', 'Yes, let\'s go!', 'Great idea!']),
    ('Coloque em ordem: "SOCCER — LET\'S — PLAY"', "Let's play soccer", ["Let's play soccer", 'Soccer play let\'s', 'Play let\'s soccer', 'Let\'s soccer play']),
    ('Qual esporte usa uma cesta (aro) para fazer pontos?', 'Basketball', ['Basketball', 'Baseball', 'Soccer', 'Tag']),
    ('Qual esporte usa um taco e uma luva?', 'Baseball', ['Baseball', 'Basketball', 'Soccer', 'Tag']),
    ('Qual esporte usa um gol para fazer pontos?', 'Soccer', ['Soccer', 'Basketball', 'Baseball', 'Tag']),
    ('"They are flying kites" significa:', 'Eles estão empinando pipa', ['Eles estão empinando pipa', 'Eles estão pulando corda', 'Eles estão andando de bicicleta', 'Eles estão nadando']),
    ('"They are jumping ropes" significa:', 'Eles estão pulando corda', ['Eles estão pulando corda', 'Eles estão empinando pipa', 'Eles estão andando de skate', 'Eles estão correndo']),
    ('"They are riding bikes" significa:', 'Eles estão andando de bicicleta', ['Eles estão andando de bicicleta', 'Eles estão andando de patins', 'Eles estão pulando corda', 'Eles estão nadando']),
    ('Qual é a palavra em inglês para "boné"?', 'Cap', ['Cap', 'Hat', 'Scarf', 'Gloves']),
]
for enunciado, resposta, opcoes in esportes_convites:
    criar_questao(ingles, 'esportes_convites', enunciado, resposta, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE INGLÊS CONCLUÍDA!")
print("=" * 55)
for modulo, nome in [
    ('weather_clothes', 'Weather & Clothes'),
    ('atividades_like', 'Atividades (like to)'),
    ('vocabulario_geral', 'Vocabulário Geral'),
    ('esportes_convites', 'Esportes e Convites'),
]:
    total = BancoQuestao.objects.filter(disciplina=ingles, modulo=modulo).count()
    print(f"   {nome:.<32} {total}")
