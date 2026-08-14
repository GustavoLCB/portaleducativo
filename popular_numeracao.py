"""
popular_numeracao.py
----------------------
Execute na raiz do projeto:
    python popular_numeracao.py

Popula o banco com questões de Matemática — Sistema de Numeração
(valor posicional/absoluto, ordens e classes, sucessor/antecessor,
decomposição, comparação de números, dobro/triplo/quíntuplo e escrita
por extenso), com base nos temas cobrados na Avaliação de Matemática
do 2º Período (Colégio Santo Agostinho, 3º ano).

Pode rodar de novo sem problema — não duplica questões já existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_questao(disciplina, modulo, enunciado, resposta, opcoes):
    obj, criado = BancoQuestao.objects.update_or_create(
        disciplina=disciplina,
        modulo=modulo,
        enunciado=enunciado,
        defaults={
            'tipo': 'multipla_escolha',
            'resposta_correta': resposta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "🔄 Atualizado"
    print(f"  {status}: {enunciado[:65]}")


print("\n🧮 Criando disciplina Matemática...")
matematica, _ = Disciplina.objects.get_or_create(
    nome='matematica', defaults={'nome_exibicao': 'Matemática'}
)
print("  ✅ Matemática pronta.")

print("\n🔢 Populando: Matemática › Sistema de Numeração...")

questoes = [
    # Valor posicional e valor absoluto
    ('No número 2.164, qual é o valor posicional do algarismo 6?', '60',
     ['6', '60', '600', '6.000']),
    ('No número 3.482, qual é o valor absoluto do algarismo 8?', '8',
     ['8', '80', '800', '8.000']),
    ('No número 1.958, qual é o valor posicional do algarismo 9?', '900',
     ['9', '90', '900', '9.000']),
    ('No número 5.647, qual é o valor absoluto do algarismo que ocupa a ordem das unidades de milhar?', '5',
     ['5', '5.000', '500', '50']),

    # Sucessor e antecessor
    ('Qual é o sucessor do número 2.164?', '2.165',
     ['2.163', '2.165', '2.174', '2.166']),
    ('Qual é o antecessor do número 3.482?', '3.481',
     ['3.483', '3.480', '3.481', '3.472']),
    ('Qual é o sucessor do número 999?', '1.000',
     ['1.000', '998', '9.999', '900']),

    # Decomposição
    ('O número 2.164 pode ser decomposto corretamente em:', '2.000 + 100 + 60 + 4',
     ['2.000 + 100 + 60 + 4', '2.000 + 10 + 6 + 4', '200 + 100 + 60 + 4', '2.000 + 160 + 40']),
    ('O número 3.482 pode ser decomposto corretamente em:', '3.000 + 400 + 80 + 2',
     ['3.000 + 400 + 80 + 2', '3.000 + 40 + 8 + 2', '300 + 400 + 80 + 2', '3.000 + 480 + 2']),
    ('Qual número corresponde à decomposição 5.000 + 600 + 40 + 7?', '5.647',
     ['5.647', '5.476', '5.746', '5.674']),

    # Ordens e classes
    ('O número 2.164 possui:', '2 classes e 4 ordens',
     ['2 classes e 4 ordens', '4 classes e 2 ordens', '4 classes e 4 ordens', '1 classe e 4 ordens']),
    ('Quantas dezenas há no número 1.958?', '195',
     ['195', '19', '1.958', '958']),
    ('Quantas centenas há no número 3.482?', '34',
     ['34', '348', '3', '482']),

    # Comparação e ordenação
    ('Qual é o maior número: 2.164 ou 2.146?', '2.164',
     ['2.164', '2.146', 'São iguais', 'Não é possível saber']),
    ('Com os algarismos 9, 8, 5 e 1, qual é o maior número que podemos formar?', '9.851',
     ['9.851', '1.589', '8.951', '5.981']),
    ('Com os algarismos 3, 7 e 2, qual é o menor número que podemos formar?', '237',
     ['237', '732', '273', '723']),

    # Dobro, triplo e quíntuplo
    ('Qual é o dobro de 40?', '80',
     ['80', '20', '120', '400']),
    ('Qual é o quíntuplo do algarismo 8 (unidade do número 1.958)?', '40',
     ['40', '16', '24', '80']),
    ('Qual é o triplo de 12?', '36',
     ['36', '24', '15', '48']),

    # Escrita por extenso
    ('João terminou uma corrida na 38ª posição. Como se escreve essa posição por extenso?', 'Trigésimo oitavo',
     ['Trigésimo oitavo', 'Trinta e oitavo', 'Terceiro oitavo', 'Octogésimo terceiro']),
    ('Como se escreve o número 21 por extenso?', 'Vinte e um',
     ['Vinte e um', 'Vinte e dois', 'Doze', 'Trinta e um']),
    ('Como se escreve por extenso a posição de quem chegou em 5º lugar?', 'Quinto',
     ['Quinto', 'Quatro', 'Cinquenta', 'Quinze']),

    # Situações-problema (baseadas no contexto da prova - festa junina)
    ('Em uma festa junina, 50 crianças participaram de uma corrida do saco. João chegou na 38ª posição. Quantas crianças terminaram depois dele?', '12',
     ['12', '11', '38', '13']),

    # Números maiores: dezenas de milhar (5 algarismos)
    ('No número 34.582, qual é o valor posicional do algarismo 3?', '30.000',
     ['30.000', '3.000', '300', '3']),
    ('No número 34.582, quantas dezenas de milhar ele possui?', '3',
     ['3', '4', '34', '30']),
    ('Qual é o sucessor do número 9.999?', '10.000',
     ['10.000', '9.998', '10.001', '9.000']),
    ('Qual é o antecessor do número 10.000?', '9.999',
     ['9.999', '10.001', '9.000', '9.998']),
    ('O número 5.246 pode ser decomposto corretamente em:', '5.000 + 200 + 40 + 6',
     ['5.000 + 200 + 40 + 6', '5.000 + 20 + 4 + 6', '500 + 200 + 40 + 6', '5.000 + 240 + 6']),
    ('Quantas ordens tem o número 45.678?', '5',
     ['5', '4', '6', '45']),
    ('Quantas classes tem o número 45.678?', '2',
     ['2', '5', '1', '3']),
    ('No número 78.912, qual é o valor absoluto do algarismo 7?', '7',
     ['7', '70.000', '7.000', '700']),
    ('No número 78.912, qual é o valor posicional do algarismo 7?', '70.000',
     ['70.000', '7.000', '700', '7']),
    ('Como se lê o número 25.000?', 'Vinte e cinco mil',
     ['Vinte e cinco mil', 'Duzentos e cinco mil', 'Vinte e cinco centenas', 'Duas mil e quinhentos']),
    ('Qual número corresponde à decomposição 40.000 + 3.000 + 200 + 10 + 5?', '43.215',
     ['43.215', '4.325', '43.125', '40.325']),
    ('Qual é o antecessor do número 6.031?', '6.030',
     ['6.030', '6.032', '6.029', '6.130']),
    ('O número que vem logo depois de 19.999 é:', '20.000',
     ['20.000', '19.998', '20.001', '18.999']),
    ('Quantas unidades de milhar há no número 27.450?', '7',
     ['7', '2', '27', '70']),
    ('No número 27.450, qual algarismo ocupa a ordem das dezenas de milhar?', '2',
     ['2', '7', '4', '5']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'sistema_numeracao', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='sistema_numeracao').count()
print(f"\n✅ Concluído! Total de questões de Sistema de Numeração: {total}")


# ══════════════════════════════════════════════════════════════════
# MÓDULO NOVO — TABUADA DO 6 AO 9
# ══════════════════════════════════════════════════════════════════
# Diferente da tabuada de "Operações Matemáticas" (sorteada em
# JavaScript, nunca salva no banco), estas questões ficam gravadas de
# verdade — o que permite elas entrarem na Prova Multidisciplinar.
print("\n✖️  Populando: Matemática › Tabuada do 6 ao 9...")

tabuada_6_a_9 = [
    ('6 × 2 = ?', '12', ['12', '6', '18', '24']),
    ('6 × 3 = ?', '18', ['18', '12', '24', '30']),
    ('6 × 4 = ?', '24', ['24', '18', '30', '36']),
    ('6 × 5 = ?', '30', ['30', '24', '36', '42']),
    ('6 × 6 = ?', '36', ['36', '30', '42', '48']),
    ('6 × 7 = ?', '42', ['42', '36', '48', '54']),
    ('6 × 8 = ?', '48', ['48', '42', '54', '60']),
    ('6 × 9 = ?', '54', ['54', '48', '60', '45']),

    ('7 × 2 = ?', '14', ['14', '7', '21', '28']),
    ('7 × 3 = ?', '21', ['21', '14', '28', '35']),
    ('7 × 4 = ?', '28', ['28', '21', '35', '42']),
    ('7 × 5 = ?', '35', ['35', '28', '42', '49']),
    ('7 × 6 = ?', '42', ['42', '35', '49', '56']),
    ('7 × 7 = ?', '49', ['49', '42', '56', '63']),
    ('7 × 8 = ?', '56', ['56', '49', '63', '70']),
    ('7 × 9 = ?', '63', ['63', '56', '70', '49']),

    ('8 × 2 = ?', '16', ['16', '8', '24', '32']),
    ('8 × 3 = ?', '24', ['24', '16', '32', '40']),
    ('8 × 4 = ?', '32', ['32', '24', '40', '48']),
    ('8 × 5 = ?', '40', ['40', '32', '48', '56']),
    ('8 × 6 = ?', '48', ['48', '40', '56', '64']),
    ('8 × 7 = ?', '56', ['56', '48', '64', '72']),
    ('8 × 8 = ?', '64', ['64', '56', '72', '80']),
    ('8 × 9 = ?', '72', ['72', '64', '80', '56']),

    ('9 × 2 = ?', '18', ['18', '9', '27', '36']),
    ('9 × 3 = ?', '27', ['27', '18', '36', '45']),
    ('9 × 4 = ?', '36', ['36', '27', '45', '54']),
    ('9 × 5 = ?', '45', ['45', '36', '54', '63']),
    ('9 × 6 = ?', '54', ['54', '45', '63', '72']),
    ('9 × 7 = ?', '63', ['63', '54', '72', '81']),
    ('9 × 8 = ?', '72', ['72', '63', '81', '90']),
    ('9 × 9 = ?', '81', ['81', '72', '90', '63']),
]

for enunciado, resposta, opcoes in tabuada_6_a_9:
    criar_questao(matematica, 'tabuada_6_a_9', enunciado, resposta, opcoes)

total_tabuada = BancoQuestao.objects.filter(disciplina=matematica, modulo='tabuada_6_a_9').count()
print(f"\n✅ Concluído! Total de questões de Tabuada do 6 ao 9: {total_tabuada}")


# ══════════════════════════════════════════════════════════════════
# MÓDULO NOVO — TABUADA DO 2 AO 5
# ══════════════════════════════════════════════════════════════════
# Mesmo padrão da Tabuada do 6 ao 9, cobrindo agora as tabuadas do 2,
# 3, 4 e 5 — completa o conjunto de tabuadas guardadas de verdade no
# banco (de 2 a 9), permitindo entrarem na Prova Multidisciplinar.
print("\n✖️  Populando: Matemática › Tabuada do 2 ao 5...")

tabuada_2_a_5 = [
    ('2 × 2 = ?', '4', ['4', '2', '6', '8']),
    ('2 × 3 = ?', '6', ['6', '4', '8', '10']),
    ('2 × 4 = ?', '8', ['8', '6', '10', '12']),
    ('2 × 5 = ?', '10', ['10', '8', '12', '14']),
    ('2 × 6 = ?', '12', ['12', '10', '14', '16']),
    ('2 × 7 = ?', '14', ['14', '12', '16', '18']),
    ('2 × 8 = ?', '16', ['16', '14', '18', '20']),
    ('2 × 9 = ?', '18', ['18', '16', '20', '10']),

    ('3 × 2 = ?', '6', ['6', '3', '9', '12']),
    ('3 × 3 = ?', '9', ['9', '6', '12', '15']),
    ('3 × 4 = ?', '12', ['12', '9', '15', '18']),
    ('3 × 5 = ?', '15', ['15', '12', '18', '21']),
    ('3 × 6 = ?', '18', ['18', '15', '21', '24']),
    ('3 × 7 = ?', '21', ['21', '18', '24', '27']),
    ('3 × 8 = ?', '24', ['24', '21', '27', '30']),
    ('3 × 9 = ?', '27', ['27', '24', '30', '15']),

    ('4 × 2 = ?', '8', ['8', '4', '12', '16']),
    ('4 × 3 = ?', '12', ['12', '8', '16', '20']),
    ('4 × 4 = ?', '16', ['16', '12', '20', '24']),
    ('4 × 5 = ?', '20', ['20', '16', '24', '28']),
    ('4 × 6 = ?', '24', ['24', '20', '28', '32']),
    ('4 × 7 = ?', '28', ['28', '24', '32', '36']),
    ('4 × 8 = ?', '32', ['32', '28', '36', '40']),
    ('4 × 9 = ?', '36', ['36', '32', '40', '20']),

    ('5 × 2 = ?', '10', ['10', '5', '15', '20']),
    ('5 × 3 = ?', '15', ['15', '10', '20', '25']),
    ('5 × 4 = ?', '20', ['20', '15', '25', '30']),
    ('5 × 5 = ?', '25', ['25', '20', '30', '35']),
    ('5 × 6 = ?', '30', ['30', '25', '35', '40']),
    ('5 × 7 = ?', '35', ['35', '30', '40', '45']),
    ('5 × 8 = ?', '40', ['40', '35', '45', '50']),
    ('5 × 9 = ?', '45', ['45', '40', '50', '43']),
]

for enunciado, resposta, opcoes in tabuada_2_a_5:
    criar_questao(matematica, 'tabuada_2_a_5', enunciado, resposta, opcoes)

total_tabuada_2_a_5 = BancoQuestao.objects.filter(disciplina=matematica, modulo='tabuada_2_a_5').count()
print(f"\n✅ Concluído! Total de questões de Tabuada do 2 ao 5: {total_tabuada_2_a_5}")
