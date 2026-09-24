"""
popular_ciencias_prova_3periodo.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ciencias_prova_3periodo.py

Popula o banco com o novo card de Ciências:
  - prova_3periodo (CIEN - Prova 3º Período)

Baseado na Avaliação de Ciências do 3º Período (11/09/2026) —
Colégio Santo Agostinho:
  - Texto "Tartarugas marinhas: entre a praia e o mar" (Projeto TAMAR)
  - Ovíparo, vivíparo e ovovivíparo
  - Herbívoro, carnívoro e onívoro
  - Vertebrados e invertebrados (V ou F)
  - Tirinha do golfinho: classes de vertebrados (mamíferos, aves...)
  - Fases da vida (infância, adolescência, fase adulta, velhice)

(As questões em inglês da prova — habitats e carnívoros — já estão
nos cards de Science do Inglês, com questões de digitar.)

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'prova_3periodo'


def criar_questao(disciplina, enunciado, resposta, erradas, modulo=MODULO):
    """Cria/atualiza uma questão de múltipla escolha (a certa + 3 erradas)."""
    opcoes = [resposta] + [e for e in erradas if e != resposta]
    assert len(opcoes) == len(set(opcoes)) == 4, f"Opções repetidas ou faltando: {enunciado}"
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


print("\n🔬 Garantindo disciplina Ciências...")
ciencias, _ = Disciplina.objects.get_or_create(nome='ciencias', defaults={'nome_exibicao': 'Ciências'})
print("  ✅ Ciências pronta.")

print("\n🏆 Populando: Ciências › CIEN - Prova 3º Período...")
T = '(Texto: "Tartarugas marinhas: entre a praia e o mar")\n'
questoes = [
    # ── Tartarugas marinhas ──
    (T + 'Qual é o assunto principal do texto?', 'Os ambientes utilizados pelas tartarugas marinhas ao longo da vida',
     ['A construção de ninhos de aves nas árvores', 'A alimentação de todos os animais terrestres',
      'Os peixes que vivem nos rios']),
    (T + 'Por que a praia é importante para a reprodução das tartarugas marinhas?',
     'Porque as fêmeas colocam seus ovos na areia, onde os ovos se desenvolvem',
     ['Porque as tartarugas se alimentam de areia', 'Porque os filhotes nascem dentro do mar',
      'Porque as tartarugas adultas dormem na praia']),
    (T + 'Depois de nascer, para onde vão as tartaruguinhas?', 'Para o mar',
     ['Para a floresta', 'Para os rios', 'Para dentro da areia']),
    (T + 'No Atlântico Norte, onde os filhotes encontram alimento e proteção?',
     'Em locais do oceano onde se acumulam algas', ['Na areia da praia', 'Em lagos de água doce', 'Em cima das árvores']),
    (T + 'Na época da reprodução, para onde as fêmeas retornam?',
     'Para a região das praias onde nasceram', ['Para qualquer rio', 'Para o fundo do oceano', 'Para as montanhas']),
    (T + 'As tartarugas marinhas levam quanto tempo para chegar à fase adulta?', 'Muitos anos',
     ['Poucos dias', 'Uma semana', 'Um mês']),
    (T + 'Quanto à reprodução, a tartaruga marinha é classificada como...',
     'Ovípara, pois coloca ovos na areia, onde os filhotes se desenvolvem',
     ['Vivípara, pois os filhotes se desenvolvem dentro do corpo da mãe',
      'Ovovivípara, pois os ovos ficam dentro do corpo da mãe', 'Mamífera, pois mama leite']),

    # ── Reprodução ──
    ('Animais VIVÍPAROS são aqueles cujos filhotes...', 'se desenvolvem dentro do corpo da mãe e nascem vivos',
     ['nascem de ovos colocados na areia', 'nascem de sementes', 'se desenvolvem dentro de ovos fora do corpo da mãe']),
    ('Animais OVOVIVÍPAROS são aqueles em que...', 'os ovos ficam dentro do corpo da mãe até o nascimento dos filhotes',
     ['os filhotes mamam leite', 'os ovos são chocados no ninho', 'não existem ovos']),
    ('Qual destes animais é OVÍPARO?', 'Galinha', ['Cachorro', 'Vaca', 'Golfinho']),
    ('Qual destes animais é VIVÍPARO?', 'Cachorro', ['Tartaruga', 'Galinha', 'Jacaré']),

    # ── Alimentação ──
    ('A capivara se alimenta de capim e de outras plantas. Ela é um animal...', 'herbívoro',
     ['carnívoro', 'onívoro', 'aquático']),
    ('A onça-pintada se alimenta de outros animais, como capivaras. Ela é um animal...', 'carnívoro',
     ['herbívoro', 'onívoro', 'invertebrado']),
    ('O porco pode se alimentar de frutos, raízes e pequenos animais. Ele é um animal...', 'onívoro',
     ['herbívoro', 'carnívoro', 'invertebrado']),
    ('Animais ONÍVOROS se alimentam de...', 'plantas e de outros animais',
     ['apenas plantas', 'apenas carne', 'apenas insetos']),
    ('Qual destes animais é CARNÍVORO?', 'Tigre', ['Cavalo', 'Coelho', 'Capivara']),

    # ── Verdadeiro ou falso ──
    ('Verdadeiro ou falso: "Todos os animais que vivem na água são peixes."', 'Falso',
     ['Verdadeiro', 'Só no mar', 'Só nos rios']),
    ('Verdadeiro ou falso: "Os animais invertebrados não possuem coluna vertebral."', 'Verdadeiro',
     ['Falso', 'Só os insetos', 'Só os peixes']),
    ('Verdadeiro ou falso: "Os animais carnívoros se alimentam apenas de plantas."', 'Falso',
     ['Verdadeiro', 'Só os filhotes', 'Só no inverno']),
    ('Verdadeiro ou falso: "A reprodução permite o nascimento de novos indivíduos."', 'Verdadeiro',
     ['Falso', 'Só nas plantas', 'Só nos peixes']),

    # ── Tirinha do golfinho ──
    ('Tirinha: o golfinho diz "Moro na água!" e depois "Minha mãe me alimentava com leite!".\n'
     'A qual classe de vertebrados o golfinho pertence?', 'Mamíferos', ['Peixes', 'Anfíbios', 'Aves']),
    ('Na tirinha, qual fala do golfinho mostra que ele é um MAMÍFERO?', '"Minha mãe me alimentava com leite!"',
     ['"Moro na água!"', '"Então você é um peixe?"', '"Eu sei nadar!"']),
    ('Na tirinha, o pássaro pertence à classe das AVES. Qual é uma característica das aves?',
     'Têm o corpo coberto de penas', ['Têm o corpo coberto de escamas', 'Mamam leite quando filhotes',
                                        'Respiram por brânquias']),

    # ── Fases da vida ──
    ('Qual é a fase da vida entre a INFÂNCIA e a FASE ADULTA, quando ocorrem muitas mudanças no corpo?',
     'Adolescência', ['Velhice', 'Infância', 'Fase adulta']),
    ('Em qual fase da vida geralmente surgem responsabilidades como trabalhar e administrar a própria casa?',
     'Fase adulta', ['Infância', 'Adolescência', 'Fase de bebê']),
    ('Qual é a ORDEM correta das fases da vida?', 'Infância → adolescência → fase adulta → velhice',
     ['Adolescência → infância → velhice → fase adulta', 'Velhice → fase adulta → infância → adolescência',
      'Infância → fase adulta → adolescência → velhice']),
    ('Por que brincar é importante na INFÂNCIA?', 'Porque ajuda a criança a aprender, se desenvolver e conviver com outras pessoas',
     ['Porque a criança não precisa aprender nada', 'Porque brincar serve só para cansar', 'Porque só os adultos aprendem']),
]
for enunciado, resposta, erradas in questoes:
    criar_questao(ciencias, enunciado, resposta, erradas)

total = BancoQuestao.objects.filter(disciplina=ciencias, modulo=MODULO).count()
print(f"\n🎉 Pronto! O card 'CIEN - Prova 3º Período' tem {total} questões.")
