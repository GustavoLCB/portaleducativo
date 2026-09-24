"""
popular_matematica_prova_3periodo.py
----------------------------------------
Execute na raiz do projeto:
    python popular_matematica_prova_3periodo.py

Popula o banco com o novo card de Matemática:
  - prova_3periodo (MAT - Prova 3º Período)

Baseado na Prova de Matemática do 3º Período (17/09/2026) — tema
"A fauna da Mata Atlântica" — Colégio Santo Agostinho:
  - Número 38.624: ordens, trocar algarismos, produto, soma dos
    valores absolutos, número romano
  - Frações de grupos (pintar 1/3 e 2/4)
  - Tabela de animais registrados: total e diferença
  - Frações de quantidades (terça parte, metade, quinta parte)
  - Arme e efetue (multiplicação e divisão)
  - Situação-problema dos micos (4 porções por dia)
  - Hexágono (lados e vértices) e figuras que não são triângulos
    nem quadriláteros (folha de 23/09)
  - Expressões numéricas

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


print("\n🧮 Garantindo disciplina Matemática...")
matematica, _ = Disciplina.objects.get_or_create(nome='matematica', defaults={'nome_exibicao': 'Matemática'})
print("  ✅ Matemática pronta.")

print("\n🏆 Populando: Matemática › MAT - Prova 3º Período...")
N = 'Em uma área protegida da Mata Atlântica foram registrados 38.624 animais.\n'
questoes = [
    # ── 1) O número 38.624 ──
    (N + 'Trocando o algarismo da 4ª ordem com o da 2ª ordem, que número obtemos?', '32.684',
     ['38.264', '32.648', '36.824']),
    (N + 'Qual é o PRODUTO entre o algarismo da 5ª ordem e o algarismo das centenas?', '18',
     ['9', '24', '11']),
    (N + 'Qual é a SOMA dos valores absolutos dos algarismos desse número?', '23',
     ['29', '20', '24']),
    (N + 'Quantas ordens tem o número 38.624?', '5', ['4', '6', '2']),
    (N + 'Como se escreve o algarismo da 1ª ordem em número romano?', 'IV', ['VI', 'II', 'IIII']),
    (N + 'Qual é o valor posicional do algarismo 8 nesse número?', '8.000', ['800', '80', '80.000']),
    (N + 'Qual é o valor posicional do algarismo 6 nesse número?', '600', ['60', '6.000', '6']),
    (N + 'Qual é o antecessor de 38.624?', '38.623', ['38.625', '38.614', '37.624']),
    (N + 'Qual é o sucessor de 38.624?', '38.625', ['38.623', '38.634', '39.624']),
    (N + 'Como se lê o número 38.624?', 'Trinta e oito mil, seiscentos e vinte e quatro',
     ['Trezentos e oitenta e seis mil, duzentos e quatro', 'Trinta e oito mil, sessenta e vinte e quatro',
      'Três mil, oitocentos e sessenta e dois']),

    # ── 2) Frações de grupos ──
    ('Em um grupo de 3 micos, devemos pintar 1/3 deles. Quantos micos vamos pintar?', '1', ['3', '2', '0']),
    ('Em um grupo de 4 papagaios, devemos pintar 2/4 deles. Quantos papagaios vamos pintar?', '2', ['4', '1', '3']),
    ('Pintar 2/4 de um grupo é o mesmo que pintar...', 'a metade do grupo',
     ['a terça parte do grupo', 'o grupo inteiro', 'a quarta parte do grupo']),
    ('Em um grupo de 6 tucanos, 1/3 voou. Quantos tucanos voaram?', '2', ['3', '1', '6']),

    # ── 3) Tabela: Mico-leão-dourado 1.426 · Jaguatirica 1.318 · Preguiça 1.507 · Tucano 1.694 ──
    ('Tabela: Mico-leão-dourado 1.426 · Jaguatirica 1.318 · Preguiça 1.507 · Tucano 1.694.\n'
     'Qual é a quantidade TOTAL de animais registrados nos quatro grupos?', '5.945', ['5.845', '4.438', '6.045']),
    ('Tabela: Mico-leão-dourado 1.426 · Jaguatirica 1.318 · Preguiça 1.507 · Tucano 1.694.\n'
     'Qual é a DIFERENÇA entre a quantidade de tucanos e a de jaguatiricas?', '376', ['386', '276', '3.012']),
    ('Tabela: Mico-leão-dourado 1.426 · Jaguatirica 1.318 · Preguiça 1.507 · Tucano 1.694.\n'
     'Qual animal teve MAIS registros?', 'Tucano', ['Preguiça', 'Mico-leão-dourado', 'Jaguatirica']),
    ('Tabela: Mico-leão-dourado 1.426 · Jaguatirica 1.318 · Preguiça 1.507 · Tucano 1.694.\n'
     'Quanto é 1.426 + 1.318 (micos + jaguatiricas)?', '2.744', ['2.734', '2.644', '2.844']),
    ('Tabela: Mico-leão-dourado 1.426 · Jaguatirica 1.318 · Preguiça 1.507 · Tucano 1.694.\n'
     'Quantas preguiças foram registradas a MAIS que micos-leões-dourados?', '81', ['91', '181', '71']),

    # ── 4) Frações de quantidades ──
    ('A TERÇA PARTE de 369 árvores é:', '123', ['133', '113', '246']),
    ('A METADE de 48 espécies é:', '24', ['12', '26', '96']),
    ('A QUINTA PARTE de 85 animais é:', '17', ['15', '19', '425']),
    ('A QUARTA PARTE de 180 porções de frutas é:', '45', ['40', '60', '90']),

    # ── 5) Arme e efetue ──
    ('Arme e efetue: 7 × 1.305 =', '9.135', ['9.035', '7.135', '9.235']),
    ('Arme e efetue: 8 × 2.456 =', '19.648', ['19.548', '16.648', '18.648']),
    ('Arme e efetue: 9 × 976 =', '8.784', ['8.684', '8.794', '9.784']),
    ('Arme e efetue: 128 ÷ 2 =', '64', ['62', '46', '74']),
    ('Arme e efetue: 729 ÷ 3 =', '243', ['233', '342', '253']),
    ('Arme e efetue: 964 ÷ 4 =', '241', ['231', '214', '251']),

    # ── 6) Situação-problema dos micos ──
    ('Em um centro de conservação, cada mico recebe 4 porções de frutas por dia. '
     'Quantas porções um mico receberá durante 15 dias?', '60', ['45', '19', '64']),
    ('Para alimentar 3 micos durante 15 dias são necessárias 180 porções de frutas. '
     'Qual é a QUARTA PARTE de 180?', '45', ['60', '40', '90']),

    # ── 7) Geometria ──
    ('Quantos LADOS tem um hexágono?', '6', ['5', '8', '4']),
    ('Quantos VÉRTICES tem um hexágono?', '6', ['5', '12', '3']),
    ('Qual afirmativa sobre o hexágono é FALSA?', 'Um hexágono possui 5 lados.',
     ['Um hexágono possui 6 lados.', 'Um hexágono possui 6 vértices.', 'O hexágono é um polígono.']),
    ('Qual destas figuras NÃO é um triângulo nem um quadrilátero?', 'Pentágono',
     ['Quadrado', 'Retângulo', 'Losango']),
    ('Qual figura NÃO tem lados retos (não é polígono)?', 'Círculo', ['Hexágono', 'Pentágono', 'Quadrado']),
    ('Quantos lados tem um pentágono?', '5', ['6', '4', '8']),

    # ── 8) Expressões numéricas ──
    ('Resolva: 2.516 − 4 × 125 + 36 ÷ 6 + 1.308 =', '3.330', ['2.022', '3.320', '5.330']),
    ('Na expressão 2.516 − 4 × 125 + 36 ÷ 6 + 1.308, qual conta fazemos PRIMEIRO?',
     '4 × 125 e 36 ÷ 6 (multiplicação e divisão)', ['2.516 − 4', '6 + 1.308', '125 + 36']),
    ('Resolva: 4.100 + 96 ÷ 3 − 1.425 + 7 × 68 =', '3.183', ['2.707', '3.273', '2.297']),
    ('Na expressão 4.100 + 96 ÷ 3 − 1.425 + 7 × 68, quanto é 7 × 68?', '476', ['466', '486', '416']),
    ('Na expressão 4.100 + 96 ÷ 3 − 1.425 + 7 × 68, quanto é 96 ÷ 3?', '32', ['23', '33', '30']),
]
for enunciado, resposta, erradas in questoes:
    criar_questao(matematica, enunciado, resposta, erradas)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo=MODULO).count()
print(f"\n🎉 Pronto! O card 'MAT - Prova 3º Período' tem {total} questões.")
