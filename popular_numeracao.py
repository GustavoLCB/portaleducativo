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
    obj, criado = BancoQuestao.objects.get_or_create(
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
    status = "✅ Criado" if criado else "⏭️  Já existe"
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
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'sistema_numeracao', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='sistema_numeracao').count()
print(f"\n✅ Concluído! Total de questões de Sistema de Numeração: {total}")
