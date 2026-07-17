"""
popular_vocabulario_visual.py
------------------------------
Execute na raiz do projeto:
    python popular_vocabulario_visual.py

Popula o banco com o jogo "Vocabulário Visual" de Inglês: aparece um
emoji (a "figura") e o aluno escolhe, entre 4 opções, a palavra certa
em inglês. Cerca de 300 palavras organizadas em várias categorias — os
3 "errados" de cada pergunta são sorteados da MESMA categoria, pra ser
um desafio de verdade.

COMO ADICIONAR MAIS PALAVRAS VOCÊ MESMO(A):
Basta abrir este arquivo, encontrar a categoria certa dentro do
dicionário CATEGORIAS logo abaixo, e acrescentar uma linha no formato:
    ('EMOJI', 'Palavra em inglês'),
Depois, salve e rode este script de novo — ele NÃO duplica o que já
existe, só adiciona o que for novo. Se preferir, também pode só me
mandar a lista de palavras novas que eu insiro pra você.

IMPORTANTE: cada emoji só pode ser usado UMA VEZ em todo o arquivo
(ele funciona como "identidade" da pergunta). Este script verifica
isso sozinho antes de gravar, e avisa se achar algum repetido.

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'vocabulario_visual'

# Cada categoria: lista de (emoji, palavra em inglês)
CATEGORIAS = {
    'animais': [
        ('🐶', 'Dog'), ('🐱', 'Cat'), ('🐦', 'Bird'), ('🐟', 'Fish'), ('🦁', 'Lion'),
        ('🐘', 'Elephant'), ('🐰', 'Rabbit'), ('🐭', 'Mouse'), ('🐴', 'Horse'), ('🐮', 'Cow'),
        ('🐷', 'Pig'), ('🐑', 'Sheep'), ('🐔', 'Chicken'), ('🦆', 'Duck'), ('🐸', 'Frog'),
        ('🐝', 'Bee'), ('🦋', 'Butterfly'), ('🐍', 'Snake'), ('🐵', 'Monkey'), ('🐻', 'Bear'),
        ('🐞', 'Ladybug'), ('🐜', 'Ant'), ('🦊', 'Fox'), ('🐺', 'Wolf'), ('🐼', 'Panda'),
        ('🐨', 'Koala'), ('🦓', 'Zebra'), ('🦒', 'Giraffe'), ('🦏', 'Rhinoceros'), ('🦛', 'Hippopotamus'),
        ('🐫', 'Camel'), ('🦘', 'Kangaroo'), ('🐢', 'Turtle'), ('🐧', 'Penguin'), ('🦉', 'Owl'),
        ('🦇', 'Bat'), ('🐿️', 'Squirrel'), ('🦚', 'Peacock'), ('🦜', 'Parrot'), ('🦈', 'Shark'),
        ('🐳', 'Whale'), ('🐬', 'Dolphin'), ('🐙', 'Octopus'), ('🦀', 'Crab'), ('🐌', 'Snail'),
    ],
    'comida': [
        ('🍎', 'Apple'), ('🍌', 'Banana'), ('🍊', 'Orange'), ('🍇', 'Grapes'), ('🍉', 'Watermelon'),
        ('🍓', 'Strawberry'), ('🍞', 'Bread'), ('🧀', 'Cheese'), ('🥚', 'Egg'), ('🥛', 'Milk'),
        ('🍕', 'Pizza'), ('🎂', 'Cake'), ('🍦', 'Ice Cream'), ('🍪', 'Cookie'), ('🥕', 'Carrot'),
        ('🍍', 'Pineapple'), ('🍑', 'Peach'), ('🍒', 'Cherry'), ('🍋', 'Lemon'), ('🥭', 'Mango'),
        ('🥥', 'Coconut'), ('🥝', 'Kiwi'), ('🥑', 'Avocado'), ('🥔', 'Potato'), ('🧅', 'Onion'),
        ('🧄', 'Garlic'), ('🥦', 'Broccoli'), ('🌽', 'Corn'), ('🥒', 'Cucumber'), ('🌶️', 'Pepper'),
        ('🍄', 'Mushroom'), ('🍚', 'Rice'), ('🍜', 'Noodles'), ('🍔', 'Hamburger'), ('🌭', 'Hot Dog'),
        ('🌮', 'Taco'), ('🍿', 'Popcorn'), ('🍩', 'Donut'), ('🍬', 'Candy'), ('🍫', 'Chocolate'),
        ('🍯', 'Honey'),
    ],
    'natureza': [
        ('☀️', 'Sun'), ('🌙', 'Moon'), ('⭐', 'Star'), ('🌳', 'Tree'), ('🌸', 'Flower'),
        ('⛰️', 'Mountain'), ('🌈', 'Rainbow'), ('☁️', 'Cloud'), ('🌧️', 'Rain'), ('❄️', 'Snow'),
        ('🔥', 'Fire'), ('🌊', 'Ocean'), ('🌋', 'Volcano'), ('🏜️', 'Desert'), ('🏝️', 'Island'),
        ('⚡', 'Lightning'), ('⛄', 'Snowman'), ('☄️', 'Comet'), ('🌍', 'Earth'), ('🍃', 'Leaf'),
        ('🌱', 'Seed'), ('🌵', 'Cactus'), ('🌷', 'Tulip'), ('🌻', 'Sunflower'), ('🌹', 'Rose'),
    ],
    'corpo': [
        ('👁️', 'Eye'), ('👂', 'Ear'), ('👃', 'Nose'), ('👄', 'Mouth'), ('✋', 'Hand'), ('🦶', 'Foot'),
        ('🦷', 'Tooth'), ('👅', 'Tongue'), ('🧠', 'Brain'), ('🦴', 'Bone'), ('💪', 'Arm'), ('🦵', 'Leg'),
    ],
    'transporte': [
        ('🚗', 'Car'), ('🚌', 'Bus'), ('🚂', 'Train'), ('✈️', 'Airplane'), ('⛵', 'Boat'),
        ('🚲', 'Bicycle'), ('🏍️', 'Motorcycle'), ('🚀', 'Rocket'), ('🚚', 'Truck'), ('🚁', 'Helicopter'),
        ('🚢', 'Ship'), ('🚕', 'Taxi'), ('🚑', 'Ambulance'), ('🚒', 'Fire Truck'), ('🚜', 'Tractor'),
        ('🛴', 'Scooter'),
    ],
    'objetos_escola': [
        ('📖', 'Book'), ('✏️', 'Pencil'), ('🎒', 'Backpack'), ('✂️', 'Scissors'), ('🕐', 'Clock'),
        ('🔑', 'Key'), ('☂️', 'Umbrella'), ('👓', 'Glasses'), ('📷', 'Camera'), ('🎁', 'Gift'),
        ('📏', 'Ruler'), ('📓', 'Notebook'), ('🖌️', 'Paintbrush'), ('🖍️', 'Crayon'),
    ],
    'cores': [
        ('🔴', 'Red'), ('🟠', 'Orange Color'), ('🟡', 'Yellow'), ('🟢', 'Green'), ('🔵', 'Blue'),
        ('🟣', 'Purple'), ('⚫', 'Black'), ('⚪', 'White'), ('🟤', 'Brown'), ('💗', 'Pink'),
    ],
    'familia': [
        ('👩', 'Mother'), ('👨', 'Father'), ('👶', 'Baby'), ('👦', 'Boy'), ('👧', 'Girl'),
        ('👵', 'Grandmother'), ('👴', 'Grandfather'), ('👪', 'Family'),
    ],
    'esportes': [
        ('🏀', 'Basketball'), ('🎾', 'Tennis'), ('⚾', 'Baseball'), ('🏊', 'Swimming'), ('🏃', 'Running'),
        ('⚽', 'Soccer'), ('🏐', 'Volleyball'), ('🏈', 'Football'), ('⛳', 'Golf'), ('🎳', 'Bowling'),
        ('⛷️', 'Skiing'), ('🏄', 'Surfing'), ('🥊', 'Boxing'), ('🏓', 'Ping Pong'), ('🛹', 'Skateboarding'),
        ('🚴', 'Cycling'), ('🤸', 'Gymnastics'), ('🧗', 'Climbing'),
    ],
    'casa_mobilia': [
        ('🛏️', 'Bed'), ('🛋️', 'Couch'), ('🛁', 'Bathtub'), ('🚿', 'Shower'), ('🚽', 'Toilet'),
        ('🚪', 'Door'), ('🪟', 'Window'), ('🪑', 'Chair'), ('🕯️', 'Candle'), ('💡', 'Light Bulb'),
        ('🪞', 'Mirror'), ('🧹', 'Broom'), ('🧼', 'Soap'), ('🪥', 'Toothbrush'), ('🚰', 'Sink'),
        ('🗑️', 'Trash Can'), ('🔔', 'Bell'), ('🪜', 'Ladder'), ('🧺', 'Basket'), ('🖼️', 'Picture Frame'),
    ],
    'eletrodomesticos': [
        ('📺', 'Television'), ('💻', 'Computer'), ('📱', 'Cell Phone'), ('☎️', 'Telephone'),
        ('📻', 'Radio'), ('🔋', 'Battery'), ('🔌', 'Plug'), ('⏰', 'Alarm Clock'),
    ],
    'roupas': [
        ('👕', 'Shirt'), ('👖', 'Pants'), ('👗', 'Dress'), ('🧦', 'Socks'), ('👞', 'Shoe'),
        ('👠', 'High Heel'), ('👢', 'Boot'), ('🎩', 'Hat'), ('🧢', 'Cap'), ('👔', 'Necktie'),
        ('🧣', 'Scarf'), ('🧤', 'Gloves'), ('🧥', 'Coat'),
    ],
    'instrumentos_musicais': [
        ('🎸', 'Guitar'), ('🎹', 'Piano'), ('🥁', 'Drum'), ('🎻', 'Violin'), ('🎺', 'Trumpet'),
        ('🎷', 'Saxophone'), ('🎤', 'Microphone'), ('🎵', 'Musical Note'),
    ],
    'numeros': [
        ('1️⃣', 'One'), ('2️⃣', 'Two'), ('3️⃣', 'Three'), ('4️⃣', 'Four'), ('5️⃣', 'Five'),
        ('6️⃣', 'Six'), ('7️⃣', 'Seven'), ('8️⃣', 'Eight'), ('9️⃣', 'Nine'), ('🔟', 'Ten'),
    ],
    'formas': [
        ('⭕', 'Circle'), ('⬛', 'Square'), ('🔺', 'Triangle'), ('💎', 'Diamond'), ('❤️', 'Heart'),
    ],
}


def criar_questao(disciplina, emoji, palavra_certa, opcoes):
    obj, criado = BancoQuestao.objects.get_or_create(
        disciplina=disciplina, modulo=MODULO, enunciado=emoji,
        defaults={
            'tipo': 'multipla_escolha',
            'resposta_correta': palavra_certa,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅" if criado else "⏭️ "
    print(f"  {status} {emoji}  {palavra_certa}")


print("\n🇬🇧 Criando disciplina Inglês (se ainda não existir)...")
ingles, _ = Disciplina.objects.get_or_create(
    nome='ingles', defaults={'nome_exibicao': 'Inglês'}
)
print("  ✅ Pronto.")

# ── Verificação de segurança: nenhum emoji pode se repetir entre categorias ──
print("\n🔍 Verificando se há emojis repetidos entre categorias...")
contagem_emoji = {}
for categoria, palavras in CATEGORIAS.items():
    for emoji, palavra in palavras:
        contagem_emoji.setdefault(emoji, []).append((categoria, palavra))

duplicados = {e: v for e, v in contagem_emoji.items() if len(v) > 1}
if duplicados:
    print("  ⚠️  ATENÇÃO: os emojis abaixo aparecem mais de uma vez e serão ignorados na 2ª+ ocorrência:")
    for emoji, ocorrencias in duplicados.items():
        print(f"     {emoji}: {ocorrencias}")
else:
    print("  ✅ Nenhum emoji repetido. Tudo certo!")

total_palavras = sum(len(v) for v in CATEGORIAS.values())
print(f"\n🖼️  Populando: Inglês › Vocabulário Visual ({total_palavras} palavras no total)...")

emojis_ja_usados = set()
total_criadas = 0
for categoria, palavras in CATEGORIAS.items():
    for emoji, palavra in palavras:
        if emoji in emojis_ja_usados:
            continue  # já foi usado em outra categoria, pula (evita sobrescrever)
        emojis_ja_usados.add(emoji)

        outras = [p for (e, p) in palavras if p != palavra]
        erradas = random.sample(outras, min(3, len(outras)))
        opcoes = erradas + [palavra]
        random.shuffle(opcoes)
        criar_questao(ingles, emoji, palavra, opcoes)
        total_criadas += 1

print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE VOCABULÁRIO VISUAL CONCLUÍDA!")
print("=" * 55)
total = BancoQuestao.objects.filter(disciplina=ingles, modulo=MODULO).count()
print(f"   Total de palavras no banco: {total}")
for categoria, palavras in CATEGORIAS.items():
    print(f"   {categoria:.<24} {len(palavras)} palavras")
