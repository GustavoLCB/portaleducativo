"""
popular_ingles.py
----------------------
Execute na raiz do projeto:
    python popular_ingles.py

Popula o banco com questões de Inglês em módulos:
  - weather_clothes (tempo e roupas)
  - atividades_like (like to + infinitivo, do/does)
  - vocabulario_geral (objetos, animais, natureza, cores, números,
    corpo humano, família, alimentos, roupas, transporte)
  - esportes_convites (ações esportivas e convites)
  - casa_comodos (cômodos e móveis da casa — formato visual)

Baseado no material real de Inglês do 3º ano (Colégio Santo Agostinho).
Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import random
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
]
for enunciado, resposta, opcoes in vocabulario_geral:
    criar_questao(ingles, 'vocabulario_geral', enunciado, resposta, opcoes)


# ── Vocabulário Geral: ampliação (cores, números, corpo, família,
# alimentos, roupas, transporte, natureza, objetos do dia a dia e
# animais extras) — mesmo módulo 'vocabulario_geral', só mais palavras.
print("\n📖 Populando: Inglês › Vocabulário Geral (ampliação)...")

vocabulario_geral_cores = [
    ('Qual é a palavra em inglês para "vermelho"?', 'Red', ['Red', 'Blue', 'Green', 'Yellow']),
    ('Qual é a palavra em inglês para "azul"?', 'Blue', ['Blue', 'Red', 'Green', 'Yellow']),
    ('Qual é a palavra em inglês para "verde"?', 'Green', ['Green', 'Blue', 'Yellow', 'Red']),
    ('Qual é a palavra em inglês para "amarelo"?', 'Yellow', ['Yellow', 'Green', 'Blue', 'Orange']),
    ('Qual é a palavra em inglês para "preto"?', 'Black', ['Black', 'White', 'Brown', 'Gray']),
    ('Qual é a palavra em inglês para "branco"?', 'White', ['White', 'Black', 'Gray', 'Brown']),
    ('Qual é a palavra em inglês para "laranja" (cor)?', 'Orange', ['Orange', 'Yellow', 'Red', 'Brown']),
    ('Qual é a palavra em inglês para "roxo"?', 'Purple', ['Purple', 'Pink', 'Blue', 'Red']),
    ('Qual é a palavra em inglês para "rosa"?', 'Pink', ['Pink', 'Purple', 'Red', 'White']),
    ('Qual é a palavra em inglês para "marrom"?', 'Brown', ['Brown', 'Black', 'Orange', 'Gray']),
]

vocabulario_geral_numeros = [
    ('Qual é a palavra em inglês para o número "1" (um)?', 'One', ['One', 'Two', 'Three', 'Ten']),
    ('Qual é a palavra em inglês para o número "2" (dois)?', 'Two', ['Two', 'One', 'Three', 'Four']),
    ('Qual é a palavra em inglês para o número "3" (três)?', 'Three', ['Three', 'Two', 'Four', 'Five']),
    ('Qual é a palavra em inglês para o número "4" (quatro)?', 'Four', ['Four', 'Three', 'Five', 'Six']),
    ('Qual é a palavra em inglês para o número "5" (cinco)?', 'Five', ['Five', 'Four', 'Six', 'Seven']),
    ('Qual é a palavra em inglês para o número "6" (seis)?', 'Six', ['Six', 'Five', 'Seven', 'Eight']),
    ('Qual é a palavra em inglês para o número "7" (sete)?', 'Seven', ['Seven', 'Six', 'Eight', 'Nine']),
    ('Qual é a palavra em inglês para o número "8" (oito)?', 'Eight', ['Eight', 'Seven', 'Nine', 'Ten']),
    ('Qual é a palavra em inglês para o número "9" (nove)?', 'Nine', ['Nine', 'Eight', 'Ten', 'One']),
    ('Qual é a palavra em inglês para o número "10" (dez)?', 'Ten', ['Ten', 'Nine', 'Eight', 'One']),
]

vocabulario_geral_corpo = [
    ('Qual é a palavra em inglês para "cabeça"?', 'Head', ['Head', 'Hair', 'Face', 'Neck']),
    ('Qual é a palavra em inglês para "olho"?', 'Eye', ['Eye', 'Ear', 'Nose', 'Mouth']),
    ('Qual é a palavra em inglês para "orelha"?', 'Ear', ['Ear', 'Eye', 'Nose', 'Mouth']),
    ('Qual é a palavra em inglês para "nariz"?', 'Nose', ['Nose', 'Mouth', 'Eye', 'Ear']),
    ('Qual é a palavra em inglês para "boca"?', 'Mouth', ['Mouth', 'Nose', 'Eye', 'Ear']),
    ('Qual é a palavra em inglês para "mão"?', 'Hand', ['Hand', 'Foot', 'Arm', 'Leg']),
    ('Qual é a palavra em inglês para "pé"?', 'Foot', ['Foot', 'Hand', 'Leg', 'Arm']),
    ('Qual é a palavra em inglês para "braço"?', 'Arm', ['Arm', 'Leg', 'Hand', 'Foot']),
    ('Qual é a palavra em inglês para "perna"?', 'Leg', ['Leg', 'Arm', 'Foot', 'Hand']),
    ('Qual é a palavra em inglês para "cabelo"?', 'Hair', ['Hair', 'Head', 'Face', 'Ear']),
]

vocabulario_geral_familia = [
    ('Qual é a palavra em inglês para "mãe"?', 'Mother', ['Mother', 'Father', 'Sister', 'Grandmother']),
    ('Qual é a palavra em inglês para "pai"?', 'Father', ['Father', 'Mother', 'Brother', 'Grandfather']),
    ('Qual é a palavra em inglês para "irmão"?', 'Brother', ['Brother', 'Sister', 'Father', 'Mother']),
    ('Qual é a palavra em inglês para "irmã"?', 'Sister', ['Sister', 'Brother', 'Mother', 'Father']),
    ('Qual é a palavra em inglês para "avó"?', 'Grandmother', ['Grandmother', 'Grandfather', 'Mother', 'Aunt']),
    ('Qual é a palavra em inglês para "avô"?', 'Grandfather', ['Grandfather', 'Grandmother', 'Father', 'Uncle']),
    ('Qual é a palavra em inglês para "bebê"?', 'Baby', ['Baby', 'Child', 'Family', 'Brother']),
    ('Qual é a palavra em inglês para "família"?', 'Family', ['Family', 'Baby', 'Mother', 'Father']),
]

vocabulario_geral_alimentos = [
    ('Qual é a palavra em inglês para "maçã"?', 'Apple', ['Apple', 'Banana', 'Orange', 'Grape']),
    ('Qual é a palavra em inglês para "banana"?', 'Banana', ['Banana', 'Apple', 'Orange', 'Grape']),
    ('Qual é a palavra em inglês para "pão"?', 'Bread', ['Bread', 'Rice', 'Cheese', 'Egg']),
    ('Qual é a palavra em inglês para "leite"?', 'Milk', ['Milk', 'Water', 'Juice', 'Cheese']),
    ('Qual é a palavra em inglês para "água"?', 'Water', ['Water', 'Milk', 'Juice', 'Rice']),
    ('Qual é a palavra em inglês para "arroz"?', 'Rice', ['Rice', 'Bread', 'Egg', 'Cheese']),
    ('Qual é a palavra em inglês para "ovo"?', 'Egg', ['Egg', 'Bread', 'Rice', 'Cheese']),
    ('Qual é a palavra em inglês para "queijo"?', 'Cheese', ['Cheese', 'Bread', 'Egg', 'Milk']),
    ('Qual é a palavra em inglês para "suco"?', 'Juice', ['Juice', 'Water', 'Milk', 'Ice cream']),
    ('Qual é a palavra em inglês para "sorvete"?', 'Ice cream', ['Ice cream', 'Cake', 'Juice', 'Cheese']),
]

vocabulario_geral_roupas = [
    ('Qual é a palavra em inglês para "camisa"?', 'Shirt', ['Shirt', 'T-shirt', 'Dress', 'Skirt']),
    ('Qual é a palavra em inglês para "camiseta"?', 'T-shirt', ['T-shirt', 'Shirt', 'Dress', 'Socks']),
    ('Qual é a palavra em inglês para "vestido"?', 'Dress', ['Dress', 'Skirt', 'Shirt', 'T-shirt']),
    ('Qual é a palavra em inglês para "saia"?', 'Skirt', ['Skirt', 'Dress', 'Shirt', 'Socks']),
    ('Qual é a palavra em inglês para "sapatos"?', 'Shoes', ['Shoes', 'Socks', 'Sandals', 'Sneakers']),
    ('Qual é a palavra em inglês para "meias"?', 'Socks', ['Socks', 'Shoes', 'Gloves', 'Shirt']),
]

vocabulario_geral_transporte = [
    ('Qual é a palavra em inglês para "carro"?', 'Car', ['Car', 'Bus', 'Train', 'Bicycle']),
    ('Qual é a palavra em inglês para "ônibus"?', 'Bus', ['Bus', 'Car', 'Train', 'Boat']),
    ('Qual é a palavra em inglês para "trem"?', 'Train', ['Train', 'Bus', 'Car', 'Ship']),
    ('Qual é a palavra em inglês para "barco"?', 'Boat', ['Boat', 'Ship', 'Car', 'Bus']),
    ('Qual é a palavra em inglês para "navio"?', 'Ship', ['Ship', 'Boat', 'Train', 'Car']),
    ('Qual é a palavra em inglês para "bicicleta"?', 'Bicycle', ['Bicycle', 'Car', 'Bus', 'Motorcycle']),
]

vocabulario_geral_natureza = [
    ('Qual é a palavra em inglês para "árvore"?', 'Tree', ['Tree', 'Flower', 'Grass', 'Leaf']),
    ('Qual é a palavra em inglês para "flor"?', 'Flower', ['Flower', 'Tree', 'Grass', 'Leaf']),
    ('Qual é a palavra em inglês para "estrela"?', 'Star', ['Star', 'Moon', 'Sun', 'Cloud']),
    ('Qual é a palavra em inglês para "nuvem"?', 'Cloud', ['Cloud', 'Sky', 'Star', 'Rain']),
    ('Qual é a palavra em inglês para "montanha"?', 'Mountain', ['Mountain', 'Sea', 'River', 'Sky']),
    ('Qual é a palavra em inglês para "mar"?', 'Sea', ['Sea', 'River', 'Mountain', 'Lake']),
    ('Qual é a palavra em inglês para "fogo"?', 'Fire', ['Fire', 'Water', 'Wind', 'Rain']),
    ('Qual é a palavra em inglês para "arco-íris"?', 'Rainbow', ['Rainbow', 'Cloud', 'Star', 'Rain']),
]

vocabulario_geral_objetos = [
    ('Qual é a palavra em inglês para "mochila"?', 'Backpack', ['Backpack', 'Notebook', 'Pencil', 'Ruler']),
    ('Qual é a palavra em inglês para "régua"?', 'Ruler', ['Ruler', 'Eraser', 'Scissors', 'Pencil']),
    ('Qual é a palavra em inglês para "borracha"?', 'Eraser', ['Eraser', 'Ruler', 'Pencil', 'Scissors']),
    ('Qual é a palavra em inglês para "caderno"?', 'Notebook', ['Notebook', 'Book', 'Backpack', 'Board']),
    ('Qual é a palavra em inglês para "tesoura"?', 'Scissors', ['Scissors', 'Ruler', 'Eraser', 'Glue']),
    ('Qual é a palavra em inglês para "chave"?', 'Key', ['Key', 'Box', 'Door', 'Clock']),
    ('Qual é a palavra em inglês para "relógio"?', 'Clock', ['Clock', 'Watch', 'Key', 'Calendar']),
    ('Qual é a palavra em inglês para "bola"?', 'Ball', ['Ball', 'Kite', 'Rope', 'Bike']),
]

vocabulario_geral_animais = [
    ('Qual é a palavra em inglês para "elefante"?', 'Elephant', ['Elephant', 'Giraffe', 'Zebra', 'Lion']),
    ('Qual é a palavra em inglês para "leão"?', 'Lion', ['Lion', 'Tiger', 'Elephant', 'Monkey']),
    ('Qual é a palavra em inglês para "tigre"?', 'Tiger', ['Tiger', 'Lion', 'Zebra', 'Elephant']),
    ('Qual é a palavra em inglês para "macaco"?', 'Monkey', ['Monkey', 'Rabbit', 'Frog', 'Snake']),
    ('Qual é a palavra em inglês para "girafa"?', 'Giraffe', ['Giraffe', 'Elephant', 'Zebra', 'Lion']),
    ('Qual é a palavra em inglês para "zebra"?', 'Zebra', ['Zebra', 'Giraffe', 'Elephant', 'Tiger']),
    ('Qual é a palavra em inglês para "coelho"?', 'Rabbit', ['Rabbit', 'Frog', 'Monkey', 'Snake']),
    ('Qual é a palavra em inglês para "borboleta"?', 'Butterfly', ['Butterfly', 'Bird', 'Bee', 'Spider']),
    ('Qual é a palavra em inglês para "cobra"?', 'Snake', ['Snake', 'Frog', 'Rabbit', 'Monkey']),
    ('Qual é a palavra em inglês para "sapo"?', 'Frog', ['Frog', 'Snake', 'Rabbit', 'Monkey']),
]

for bloco in [
    vocabulario_geral_cores, vocabulario_geral_numeros, vocabulario_geral_corpo,
    vocabulario_geral_familia, vocabulario_geral_alimentos, vocabulario_geral_roupas,
    vocabulario_geral_transporte, vocabulario_geral_natureza, vocabulario_geral_objetos,
    vocabulario_geral_animais,
]:
    for enunciado, resposta, opcoes in bloco:
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


# ══════════════════════════════════════════════════════════════════
# MÓDULO — ROOMS IN THE HOUSE (formato visual: imagem + nome)
# ══════════════════════════════════════════════════════════════════
print("\n🏠 Populando: Inglês › Rooms in the House...")

# Esse módulo mudou de formato (antes era pergunta em texto, agora é
# "imagem" (emoji grande) + nome do cômodo/móvel, igual ao Vocabulário
# Visual). Por isso apagamos as perguntas antigas em texto antes de
# gravar as novas — senão as duas versões ficariam misturadas no banco.
apagadas, _ = BancoQuestao.objects.filter(disciplina=ingles, modulo='casa_comodos').delete()
if apagadas:
    print(f"  🗑️  Removidas {apagadas} perguntas antigas (formato texto) de Rooms in the House.")

casa_comodos_visual = [
    # Cômodos (rooms) — usam emoji (ficaram bons)
    ('🍲', 'Kitchen'),
    ('🛏️', 'Bedroom'),
    ('🛁', 'Bathroom'),
    ('🛋️', 'Living room'),
    ('🍽️', 'Dining room'),
    ('🌳', 'Garden'),
    ('🚗', 'Garage'),
    ('💻', 'Office'),
    # Móveis e objetos com bom emoji disponível
    ('📚', 'Bookcase'),
    ('🪑', 'Armchair'),
    ('🔥', 'Fireplace'),
    ('🪜', 'Stairs'),
    ('🛌', 'Pillow'),
    ('📺', 'TV'),
    ('🪞', 'Mirror'),
    ('💡', 'Lamp'),
    ('🪟', 'Window'),
    ('🚪', 'Door'),
    # Móveis e objetos SEM bom emoji — usam ícone desenhado em SVG
    # (a "chave" abaixo precisa bater com o dicionário iconesSVG do
    # ingles_quiz.html; se mudar um nome aqui, mude lá também)
    ('table', 'Table'),
    ('stove', 'Stove'),
    ('microwave', 'Microwave'),
    ('chair', 'Chair'),
    ('sofa', 'Sofa'),
    ('shelf', 'Shelf'),
    ('fridge', 'Refrigerator'),
    ('washing_machine', 'Washing machine'),
]

# Verificação de segurança: nenhum emoji pode se repetir (o emoji é a
# "identidade" da pergunta — se repetisse, uma palavra sobrescreveria a
# outra sem querer).
emojis_vistos = set()
duplicados = [emoji for emoji, _ in casa_comodos_visual if emoji in emojis_vistos or emojis_vistos.add(emoji)]
if duplicados:
    print(f"  ⚠️  ATENÇÃO: emojis repetidos em casa_comodos_visual: {duplicados}")

for emoji, palavra_certa in casa_comodos_visual:
    outras = [palavra for (_, palavra) in casa_comodos_visual if palavra != palavra_certa]
    erradas = random.sample(outras, min(3, len(outras)))
    opcoes = erradas + [palavra_certa]
    random.shuffle(opcoes)
    criar_questao(ingles, 'casa_comodos', emoji, palavra_certa, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE INGLÊS CONCLUÍDA!")
print("=" * 55)
for modulo, nome in [
    ('weather_clothes', 'Weather & Clothes'),
    ('atividades_like', 'Atividades (like to)'),
    ('vocabulario_geral', 'Vocabulário Geral'),
    ('esportes_convites', 'Esportes e Convites'),
    ('casa_comodos', 'Rooms in the House'),
]:
    total = BancoQuestao.objects.filter(disciplina=ingles, modulo=modulo).count()
    print(f"   {nome:.<32} {total}")
