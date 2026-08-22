"""
popular_ingles_science.py
---------------------------
Execute na raiz do projeto:
    python popular_ingles_science.py

Popula o banco com questões do novo card "Science" dentro de Inglês,
em 4 módulos (todas as perguntas e respostas em inglês):
  - science_vertebrates_invertebrates
  - science_oviparous_viviparous
  - science_habitats
  - science_eating_habits

Baseado no material "Grouping Animals" (Ms. Dordron, Colégio Santo
Agostinho). Os 4 jogos de colmeia (Hive Games) NÃO usam este script —
os pares deles ficam direto no views.py (TEMAS_SCIENCE_HIVE), porque
não são perguntas de múltipla escolha.

Pode rodar de novo sem problema — usa update_or_create, então além de
nunca duplicar, também atualiza o conteúdo se este arquivo for editado.
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
    print(f"  {status}: {enunciado[:65]}")


print("\n🇬🇧 Criando disciplina Inglês (se ainda não existir)...")
ingles, _ = Disciplina.objects.get_or_create(
    nome='ingles', defaults={'nome_exibicao': 'Inglês'}
)
print("  ✅ Inglês pronto.")


# ══════════════════════════════════════════════════════════════════
# MÓDULO — VERTEBRATES X INVERTEBRATES
# ══════════════════════════════════════════════════════════════════
print("\n🦴 Populando: Inglês › Science › Vertebrates x Invertebrates...")

vertebrates_invertebrates = [
    ('Which animals have a backbone (spine) inside their body?', 'Vertebrates',
     ['Vertebrates', 'Invertebrates', 'Amphibians', 'Mammals']),
    ('Which animals do NOT have a vertebral column?', 'Invertebrates',
     ['Invertebrates', 'Vertebrates', 'Reptiles', 'Fish']),
    ('What covers the brain of a vertebrate?', 'The cranium (skull)',
     ['The cranium (skull)', 'An exoskeleton', 'A shell only', 'Nothing']),
    ('What are the 5 major groups of vertebrates?', 'Mammals, birds, fish, amphibians and reptiles',
     ['Mammals, birds, fish, amphibians and reptiles', 'Insects, spiders and worms',
      'Only mammals and birds', 'Fish and insects']),
    ('Some invertebrates have soft bodies. Which of these is an example?', 'Jellyfish',
     ['Jellyfish', 'Lion', 'Eagle', 'Turtle']),
    ('A hard outer casing that protects some invertebrates is called:', 'Exoskeleton',
     ['Exoskeleton', 'Backbone', 'Cranium', 'Fur']),
    ('Which of these animals is an insect with an exoskeleton?', 'Beetle',
     ['Beetle', 'Dog', 'Frog', 'Snake']),
    ('Is a spider a vertebrate or an invertebrate?', 'Invertebrate',
     ['Invertebrate', 'Vertebrate', 'Amphibian', 'Mammal']),
    ('Is an iguana a vertebrate or an invertebrate?', 'Vertebrate',
     ['Vertebrate', 'Invertebrate', 'Mollusc', 'Crustacean']),
    ('Which group do snails, shrimp and scallops belong to?', 'Invertebrates',
     ['Invertebrates', 'Vertebrates', 'Mammals', 'Reptiles']),
    ('Warm-blooded vertebrates include:', 'Mammals and birds',
     ['Mammals and birds', 'Fish and reptiles', 'Amphibians and fish', 'Only reptiles']),
    ('Cold-blooded vertebrates include:', 'Fish, reptiles and amphibians',
     ['Fish, reptiles and amphibians', 'Mammals and birds', 'Only mammals', 'Only birds']),
    ('There can be cartilage instead of bone in the backbone of some:', 'Vertebrates',
     ['Vertebrates', 'Invertebrates', 'Insects', 'Molluscs']),
    ('Which of these is a vertebrate?', 'Shark', ['Shark', 'Octopus', 'Starfish', 'Centipede']),
    ('Which of these is an invertebrate?', 'Starfish', ['Starfish', 'Dolphin', 'Owl', 'Crocodile']),
]
for enunciado, resposta, opcoes in vertebrates_invertebrates:
    criar_questao(ingles, 'science_vertebrates_invertebrates', enunciado, resposta, opcoes)

# ── Extra: Mammals and Birds (com base no material "Mammals and Birds",
#    Ms. Dordron) — aprofunda o mesmo tema de vertebrados, comparando
#    especificamente estes dois grupos.
mammals_and_birds = [
    ('What do mammals and birds have in common?', 'They are warm-blooded and have a backbone',
     ['They are warm-blooded and have a backbone', 'They both have feathers', 'They both lay eggs only',
      'They are both invertebrates']),
    ('What covers the body of a bird?', 'Feathers', ['Feathers', 'Fur', 'Scales', 'A shell']),
    ('Do mammals have feathers?', 'No, only birds have feathers',
     ['No, only birds have feathers', 'Yes, all mammals have feathers', 'Only baby mammals do', 'Yes, but only in winter']),
    ("A bird's feathers can have different:", 'Functions', ['Functions', 'Names only', 'Colors only', 'Sizes only']),
    ('How do birds reproduce?', 'They lay eggs',
     ['They lay eggs', 'They give birth to live babies', "They don't reproduce", 'They split in half']),
    ('Are birds warm-blooded or cold-blooded?', 'Warm-blooded', ['Warm-blooded', 'Cold-blooded', 'Neither', 'Both']),
    ('Are mammals warm-blooded or cold-blooded?', 'Warm-blooded', ['Warm-blooded', 'Cold-blooded', 'Neither', 'Both']),
    ('Do both mammals and birds have a backbone (spine)?', 'Yes, both have a backbone',
     ['Yes, both have a backbone', 'No, neither has one', 'Only mammals have one', 'Only birds have one']),
    ('Which of these is an example of a mammal?', 'Lion', ['Lion', 'Eagle', 'Ostrich', 'Penguin']),
    ('Which of these is an example of a bird?', 'Eagle', ['Eagle', 'Lion', 'Dog', 'Cat']),
    ('Which of these animals can fly, thanks to its feathers?', 'Eagle', ['Eagle', 'Lion', 'Elephant', 'Bear']),
]
for enunciado, resposta, opcoes in mammals_and_birds:
    criar_questao(ingles, 'science_vertebrates_invertebrates', enunciado, resposta, opcoes)

# ── Extra: Fish (com base no material "Fish", Ms. Dordron) — aprofunda
#    o tema de vertebrados, focando nas características dos peixes.
fish = [
    ('Fish are vertebrate animals, so they have a:', 'Backbone', ['Backbone', 'Exoskeleton', 'Shell', 'Cartilage only']),
    ('How do fish breathe?', 'Using their gills', ['Using their gills', 'Using lungs', 'Using their skin only', 'They do not breathe']),
    ('What are the bodies of fish covered with?', 'Scales', ['Scales', 'Feathers', 'Fur', 'Shells']),
    ('What do fish have to help them swim?', 'Fins', ['Fins', 'Wings', 'Legs', 'Paws']),
    ('Fish live in the water, so they are considered:', 'Aquatic animals', ['Aquatic animals', 'Terrestrial animals', 'Aerial animals', 'Arboreal animals']),
    ('Are fish oviparous or viviparous?', 'Oviparous', ['Oviparous', 'Viviparous', 'Neither', 'Both']),
    ('Are fish cold-blooded or warm-blooded?', 'Cold-blooded', ['Cold-blooded', 'Warm-blooded', 'Neither', 'Both']),
    ('How many habitats do fish usually have?', '1', ['1', '2', '3', '4']),
    ('Fish usually have jaws and:', 'Teeth', ['Teeth', 'Fur', 'Feathers', 'Wings']),
    ('Can many fish see colors?', 'Yes, many fish can see colors', ['Yes, many fish can see colors', 'No, fish are completely blind', 'Only at night', 'Only baby fish can']),
    ('Which of these is an example of a fish?', 'Shark', ['Shark', 'Frog', 'Turtle', 'Dolphin']),
]
for enunciado, resposta, opcoes in fish:
    criar_questao(ingles, 'science_vertebrates_invertebrates', enunciado, resposta, opcoes)

# ── Extra: Reptiles and Amphibians (com base no material "Reptiles and
#    Amphibians", Ms. Dordron) — compara estes dois grupos de vertebrados.
reptiles_amphibians = [
    ('Which of these animals are examples of reptiles?', 'Turtles, snakes, lizards and crocodiles',
     ['Turtles, snakes, lizards and crocodiles', 'Frogs and salamanders', 'Fish and birds', 'Only snakes']),
    ('Which of these animals are examples of amphibians?', 'Frogs and salamanders',
     ['Frogs and salamanders', 'Turtles and snakes', 'Lizards and crocodiles', 'Only frogs']),
    ('What kind of skin do amphibians have?', 'Moist skin', ['Moist skin', 'Dry skin', 'Skin covered in feathers', 'Skin covered in fur']),
    ('Are amphibians cold-blooded or warm-blooded?', 'Cold-blooded', ['Cold-blooded', 'Warm-blooded', 'Neither', 'Both']),
    ('How many habitats do amphibians usually have?', '2', ['2', '1', '3', '4']),
    ('Most adult amphibians are:', 'Carnivore animals', ['Carnivore animals', 'Herbivore animals', 'Omnivore animals', 'They do not eat']),
    ('How do amphibians reproduce?', 'They lay eggs', ['They lay eggs', 'They give birth to live babies', 'They do not reproduce', 'They split in half']),
    ('Are reptiles invertebrate or vertebrate animals?', 'Vertebrate', ['Vertebrate', 'Invertebrate', 'Neither', 'Both']),
    ('Are reptiles cold-blooded or warm-blooded?', 'Cold-blooded', ['Cold-blooded', 'Warm-blooded', 'Neither', 'Both']),
    ('What is the body of a reptile covered with?', 'Scales', ['Scales', 'Feathers', 'Fur', 'Moist skin']),
    ('Are most reptiles herbivores?', 'No, most reptiles are not herbivores', ['No, most reptiles are not herbivores', 'Yes, all reptiles are herbivores', 'Yes, but only baby reptiles', 'Reptiles do not eat']),
    ('Are all reptiles only terrestrial animals?', 'No, some reptiles also live in water', ['No, some reptiles also live in water', 'Yes, all reptiles only live on land', 'Yes, reptiles can only fly', 'Reptiles only live underground']),
    ('Which of these has moist skin and needs to live near water?', 'Frog', ['Frog', 'Turtle', 'Snake', 'Crocodile']),
    ('Which of these is covered in dry scales and lays eggs on land?', 'Lizard', ['Lizard', 'Frog', 'Salamander', 'Toad']),
]
for enunciado, resposta, opcoes in reptiles_amphibians:
    criar_questao(ingles, 'science_vertebrates_invertebrates', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO — OVIPAROUS X VIVIPAROUS
# ══════════════════════════════════════════════════════════════════
print("\n🥚 Populando: Inglês › Science › Oviparous x Viviparous...")

oviparous_viviparous = [
    ('Animals that lay eggs are called:', 'Oviparous', ['Oviparous', 'Viviparous', 'Herbivores', 'Carnivores']),
    ('Animals that give birth to live offspring are called:', 'Viviparous',
     ['Viviparous', 'Oviparous', 'Omnivores', 'Aquatic']),
    ('In oviparous animals, where does the embryo develop?', 'Externally, inside an egg',
     ['Externally, inside an egg', "Inside the mother's body", 'In the water only', 'In the soil']),
    ('In viviparous animals, where does the embryo develop?', "Internally, inside the mother's body",
     ["Internally, inside the mother's body", 'Externally, inside an egg', 'In a nest only', 'In the sea']),
    ("When does an oviparous animal's baby come out?", 'When the egg hatches',
     ['When the egg hatches', 'When the mother delivers it', 'After one year always', 'Never']),
    ('Which of these animals is oviparous?', 'Turtle', ['Turtle', 'Dog', 'Cow', 'Horse']),
    ('Which of these animals is viviparous?', 'Cat', ['Cat', 'Chicken', 'Frog', 'Salmon']),
    ('Is a penguin oviparous or viviparous?', 'Oviparous', ['Oviparous', 'Viviparous', 'Neither', 'Both']),
    ('Is a tiger oviparous or viviparous?', 'Viviparous', ['Viviparous', 'Oviparous', 'Neither', 'Both']),
    ('Which of these lays eggs?', 'Ostrich', ['Ostrich', 'Zebra', 'Pig', 'Rhino']),
    ('Which of these gives birth to live young?', 'Zebra', ['Zebra', 'Ostrich', 'Salmon', 'Parrot']),
    ('Fish and amphibians are usually:', 'Oviparous', ['Oviparous', 'Viviparous', 'Warm-blooded only', 'Invertebrates']),
    ('Most mammals are:', 'Viviparous', ['Viviparous', 'Oviparous', 'Cold-blooded', 'Aquatic only']),
    ('Which of these is oviparous?', 'Butterfly', ['Butterfly', 'Human', 'Elephant', 'Whale']),
    ('When the development of the fetus is complete in a viviparous animal, the mother:', 'Delivers the baby',
     ['Delivers the baby', 'Lays an egg', 'Builds a nest', 'Sheds its skin']),
]
for enunciado, resposta, opcoes in oviparous_viviparous:
    criar_questao(ingles, 'science_oviparous_viviparous', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO — ANIMAL HABITATS
# ══════════════════════════════════════════════════════════════════
print("\n🌍 Populando: Inglês › Science › Animal Habitats...")

habitats = [
    ('Animals that live in the water are called:', 'Aquatic', ['Aquatic', 'Terrestrial', 'Aerial', 'Arboreal']),
    ('Animals that live on the land are called:', 'Terrestrial', ['Terrestrial', 'Aquatic', 'Aerial', 'Arboreal']),
    ('Animals that live in the air are called:', 'Aerial', ['Aerial', 'Aquatic', 'Terrestrial', 'Arboreal']),
    ('Animals that live on trees are called:', 'Arboreal', ['Arboreal', 'Aquatic', 'Terrestrial', 'Aerial']),
    ('Which of these is an aquatic animal?', 'Dolphin', ['Dolphin', 'Lion', 'Eagle', 'Monkey']),
    ('Which of these is a terrestrial animal?', 'Elephant', ['Elephant', 'Shark', 'Owl', 'Koala']),
    ('Which of these is an aerial animal?', 'Bat', ['Bat', 'Whale', 'Zebra', 'Sloth']),
    ('Which of these is an arboreal animal?', 'Sloth', ['Sloth', 'Shark', 'Camel', 'Hippo']),
    ('Which animals live in both water AND on land?', 'Amphibians',
     ['Amphibians', 'Only fish', 'Only birds', 'Only insects']),
    ('A frog is an example of an animal that lives:', 'In water and on land',
     ['In water and on land', 'Only in the air', 'Only underground', 'Only on trees']),
    ('Which of these organs helps aquatic animals breathe underwater?', 'Gills',
     ['Gills', 'Lungs only', 'Wings', 'Fur']),
    ('Birds and flying insects are the most popular examples of:', 'Aerial animals',
     ['Aerial animals', 'Aquatic animals', 'Terrestrial animals', 'Arboreal animals']),
    ('Which of these lives on trees?', 'Orangutan', ['Orangutan', 'Hippopotamus', 'Crab', 'Salmon']),
    ('A hippo is an example of an animal that lives:', 'In water and on land',
     ['In water and on land', 'Only on trees', 'Only in the air', 'Only underground']),
    ('Which of these is a crustacean that can live in water and on land?', 'Crab',
     ['Crab', 'Eagle', 'Koala', 'Giraffe']),
]
for enunciado, resposta, opcoes in habitats:
    criar_questao(ingles, 'science_habitats', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO — EATING HABITS
# ══════════════════════════════════════════════════════════════════
print("\n🍽️  Populando: Inglês › Science › Eating Habits...")

eating_habits = [
    ('Animals that only eat meat are called:', 'Carnivores', ['Carnivores', 'Herbivores', 'Omnivores', 'Vegetarians']),
    ('Animals that only eat plants are called:', 'Herbivores', ['Herbivores', 'Carnivores', 'Omnivores', 'Predators']),
    ('Animals that eat both meat and plants are called:', 'Omnivores',
     ['Omnivores', 'Herbivores', 'Carnivores', 'Insectivores']),
    ('Which of these is a carnivore?', 'Lion', ['Lion', 'Cow', 'Rabbit', 'Deer']),
    ('Which of these is a herbivore?', 'Zebra', ['Zebra', 'Wolf', 'Shark', 'Leopard']),
    ('Which of these is an omnivore?', 'Bear', ['Bear', 'Antelope', 'Panda', 'Beaver']),
    ('Herbivores eat things like flowers, fruit, nuts, grass or:', 'Wood',
     ['Wood', 'Fish', 'Insects', 'Meat']),
    ('Carnivore animals primarily feed on:', 'Other animals',
     ['Other animals', 'Only plants', 'Only fruit', 'Only fish']),
    ('Which of these is a carnivore that lives in the ocean?', 'Shark',
     ['Shark', 'Panda', 'Koala', 'Elephant']),
    ('Which of these animals is an omnivore?', 'Pig', ['Pig', 'Tiger', 'Cow', 'Deer']),
    ('Which of these is a herbivore?', 'Panda', ['Panda', 'Wolf', 'Eagle', 'Crocodile']),
    ('Humans, in terms of eating habits, are usually classified as:', 'Omnivores',
     ['Omnivores', 'Herbivores only', 'Carnivores only', 'Insectivores']),
    ('Which of these is a carnivore?', 'Crocodile', ['Crocodile', 'Rabbit', 'Sheep', 'Koala']),
    ('A grasshopper mainly eats plants, so it is a:', 'Herbivore',
     ['Herbivore', 'Carnivore', 'Omnivore', 'Predator']),
    ('Which of these animals hunts other animals for food?', 'Wolf',
     ['Wolf', 'Rabbit', 'Cow', 'Sheep']),
]
for enunciado, resposta, opcoes in eating_habits:
    criar_questao(ingles, 'science_eating_habits', enunciado, resposta, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE INGLÊS › SCIENCE CONCLUÍDA!")
print("=" * 55)
for modulo, nome in [
    ('science_vertebrates_invertebrates', 'Vertebrates x Invertebrates'),
    ('science_oviparous_viviparous', 'Oviparous x Viviparous'),
    ('science_habitats', 'Animal Habitats'),
    ('science_eating_habits', 'Eating Habits'),
]:
    total = BancoQuestao.objects.filter(disciplina=ingles, modulo=modulo).count()
    print(f"   {nome:.<32} {total}")
