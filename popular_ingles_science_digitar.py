"""
popular_ingles_science_digitar.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ingles_science_digitar.py

Acrescenta questões de DIGITAR aos módulos de Science (em Inglês),
com base na Prova de Ciências do 3º período (questões 6 e 7, que são
em inglês):
  - science_eating_habits (Eating Habits): "Mark only the CARNIVORE
    animals" → agora o aluno DIGITA o nome do animal certo, entre os
    mostrados no word bank.
  - science_habitats (Animal Habitats): completar frases com
    AQUATIC / HABITATS / LAND (word bank).
  - science_eating_habits: completar com MEAT / OMNIVORE.

Não mexe nas questões que já existem nesses módulos — só acrescenta.
Pode rodar de novo sem problema — não duplica questões.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_digitar(disciplina, modulo, enunciado, resposta, opcoes, banco, aceitas=None):
    obj, criado = BancoQuestao.objects.update_or_create(
        disciplina=disciplina, modulo=modulo, enunciado=enunciado,
        defaults={
            'tipo': 'completar_frase',
            'resposta_correta': resposta,
            'dados_extras': {'modo': 'digitar', 'opcoes': opcoes, 'banco': banco, 'aceitas': aceitas or []},
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "🔄 Atualizado"
    print(f"  {status} ⌨️  [{modulo}] {enunciado.splitlines()[0][:55]}")


print("\n🇬🇧 Garantindo disciplina Inglês...")
ingles, _ = Disciplina.objects.get_or_create(nome='ingles', defaults={'nome_exibicao': 'Inglês'})

EMOJI = {
    'bunny': '🐰', 'tiger': '🐯', 'horse': '🐴', 'snake': '🐍', 'capybara': '🦫', 'lion': '🦁',
    'cow': '🐄', 'giraffe': '🦒', 'shark': '🦈', 'sheep': '🐑', 'wolf': '🐺', 'pig': '🐷',
    'bear': '🐻', 'rabbit': '🐇', 'eagle': '🦅', 'goat': '🐐',
}

# ══════════════════════════════════════════════════════════════════
# Eating Habits — qual animal é CARNIVORE / HERBIVORE / OMNIVORE? (digitar)
# ══════════════════════════════════════════════════════════════════
print("\n🍽️  Eating Habits (digitar o nome do animal)...")
animais = [
    ('CARNIVORE', 'A', 'tiger', ['bunny', 'horse', 'capybara']),
    ('CARNIVORE', 'B', 'snake', ['bunny', 'horse', 'capybara']),
    ('CARNIVORE', 'C', 'lion', ['cow', 'giraffe', 'sheep']),
    ('CARNIVORE', 'D', 'shark', ['sheep', 'rabbit', 'horse']),
    ('CARNIVORE', 'E', 'wolf', ['goat', 'capybara', 'cow']),
    ('CARNIVORE', 'F', 'eagle', ['bunny', 'giraffe', 'sheep']),
    ('HERBIVORE', 'A', 'capybara', ['tiger', 'shark', 'snake']),
    ('HERBIVORE', 'B', 'giraffe', ['lion', 'wolf', 'eagle']),
    ('OMNIVORE', 'A', 'pig', ['lion', 'cow', 'shark']),
    ('OMNIVORE', 'B', 'bear', ['tiger', 'horse', 'sheep']),
]
for tipo, letra, certo, errados in animais:
    enunciado = f'Group {letra}: Which animal is a {tipo}?\nType its name in English.'
    nomes = [certo] + errados
    banco = [f'{EMOJI[n]} {n}' for n in nomes]
    criar_digitar(ingles, 'science_eating_habits', enunciado, certo, nomes, banco,
                  aceitas=[f'the {certo}', f'a {certo}', f'{certo}s'])

# ══════════════════════════════════════════════════════════════════
# Completar frases da prova (questão 6 da Prova de Ciências)
# ══════════════════════════════════════════════════════════════════
print("\n⌨️  Completar frases (word bank da prova)...")
BANCO = ['habitats', 'omnivore', 'aquatic', 'land', 'meat']
frases = [
    ('science_habitats', 'Complete: ______ animals live most of their lives in the water.', 'aquatic'),
    ('science_habitats', 'Complete: Animals can have different ______, for example, aquatic, terrestrial and aerial.', 'habitats'),
    ('science_habitats', 'Complete: Terrestrial animals live most of their lives on ______.', 'land'),
    ('science_eating_habits', 'Complete: Carnivore animals eat mainly ______.', 'meat'),
    ('science_eating_habits', 'Complete: ______ animals eat meat and plants.', 'omnivore'),
]
for modulo, enunciado, resposta in frases:
    opcoes = [resposta] + [p for p in BANCO if p != resposta][:3]
    criar_digitar(ingles, modulo, enunciado, resposta, opcoes, BANCO)

print("\n🎉 Pronto! Questões de digitar adicionadas em Eating Habits e Animal Habitats.")
