"""
popular_2ano_mais_numeros.py
-------------------------------
Execute na raiz do projeto:
    python popular_2ano_mais_numeros.py

Popula o banco com questões do NOVO card de Matemática do 2º ANO —
"Mais Números" (dezenas/unidades, somas com base 10, sequências
crescentes/decrescentes, pares e ímpares, forma ordinal e escrita por
extenso), com base no material "Unidade 5 — Mais números" do 2º ano
(Colégio Santo Agostinho).

Observação: as questões que dependiam de contar contas de colar ou de
ábaco na imagem não entraram — fiquei só com o que dá pra verificar
100% em texto.

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_questao(disciplina, modulo, ano, enunciado, resposta, opcoes):
    obj, criado = BancoQuestao.objects.update_or_create(
        disciplina=disciplina, modulo=modulo, ano=ano, enunciado=enunciado,
        defaults={
            'tipo': 'multipla_escolha',
            'resposta_correta': resposta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "🔄 Atualizado"
    print(f"  {status}: {enunciado[:65]}")


print("\n🧮 Criando disciplina Matemática (se ainda não existir)...")
matematica, _ = Disciplina.objects.get_or_create(
    nome='matematica', defaults={'nome_exibicao': 'Matemática'}
)
print("  ✅ Matemática pronta.")

print("\n🔟 Populando: Matemática (2º ano) › Mais Números...")

questoes = [
    # Dezenas e unidades
    ('O número 13 tem quantas dezenas e quantas unidades?', '1 dezena e 3 unidades',
     ['1 dezena e 3 unidades', '3 dezenas e 1 unidade', '1 dezena e 8 unidades', '0 dezenas e 13 unidades']),
    ('O número 15 tem quantas dezenas e quantas unidades?', '1 dezena e 5 unidades',
     ['1 dezena e 5 unidades', '5 dezenas e 1 unidade', '1 dezena e 3 unidades', '0 dezenas e 15 unidades']),
    ('O número 18 tem quantas dezenas e quantas unidades?', '1 dezena e 8 unidades',
     ['1 dezena e 8 unidades', '8 dezenas e 1 unidade', '1 dezena e 3 unidades', '0 dezenas e 18 unidades']),

    # Somas com base 10
    ('10 + 3 = ?', '13', ['13', '12', '14', '10']),
    ('10 + 4 = ?', '14', ['14', '13', '15', '10']),
    ('___ + 6 = 10. Qual é o número que falta?', '4', ['4', '3', '5', '6']),
    ('7 + ___ = 10. Qual é o número que falta?', '3', ['3', '2', '4', '7']),
    ('10 - ___ = 8. Qual é o número que falta?', '2', ['2', '1', '3', '8']),
    ('10 - ___ = 3. Qual é o número que falta?', '7', ['7', '6', '8', '3']),

    # Escrita por extenso
    ('Como se escreve por extenso o número 14?', 'Catorze', ['Catorze', 'Quinze', 'Dezoito', 'Onze']),
    ('Como se escreve por extenso o número 17?', 'Dezessete', ['Dezessete', 'Dezesseis', 'Dezoito', 'Setenta']),

    # Forma ordinal
    ('Qual é a forma ordinal (numeral) de "oitavo"?', '8º', ['8º', '18º', '80º', '6º']),
    ('Qual é a forma ordinal (numeral) de "décimo quarto"?', '14º', ['14º', '4º', '40º', '10º']),
    ('Qual é a forma ordinal (numeral) de "segundo"?', '2º', ['2º', '12º', '20º', '1º']),
    ('Qual é a forma ordinal (numeral) de "décimo nono"?', '19º', ['19º', '9º', '90º', '20º']),
    ('Qual é a forma ordinal (numeral) de "quinto"?', '5º', ['5º', '15º', '50º', '4º']),
    ('Qual é a forma ordinal (numeral) de "décimo sexto"?', '16º', ['16º', '6º', '60º', '15º']),

    # Pares e ímpares
    ('O número 18 é par ou ímpar?', 'Par', ['Par', 'Ímpar']),
    ('O número 13 é par ou ímpar?', 'Ímpar', ['Ímpar', 'Par']),
    ('O número 5 é par ou ímpar?', 'Ímpar', ['Ímpar', 'Par']),
    ('O número 10 é par ou ímpar?', 'Par', ['Par', 'Ímpar']),
    ('Qual é o quinto número par, contando a partir do 2 (2, 4, 6, 8, ...)?', '10', ['10', '8', '12', '9']),
    ('Qual é o quinto número ímpar, contando a partir do 1 (1, 3, 5, 7, ...)?', '9', ['9', '7', '11', '10']),

    # Sequências crescentes/decrescentes
    ('Em uma sequência crescente que vai do 8 ao 16 (8, 9, 10, ..., 16), qual número vem logo depois do 14?', '15', ['15', '16', '14', '13']),
    ('Em uma sequência decrescente que vai do 14 ao 6 (14, 13, 12, ..., 6), qual número vem logo depois do 10?', '9', ['9', '8', '11', '7']),
    ('Começando em 1 e somando 2 repetidamente (1, 3, 5, 7, 9, ...), qual é o próximo número depois do 9?', '11', ['11', '10', '12', '13']),
    ('Complete a sequência crescente: 7, 9, 11, ___ (aumentando de 2 em 2). Qual é o próximo número?', '13', ['13', '12', '14', '15']),
    ('Complete a sequência decrescente: 21, 19, 17, ___ (diminuindo de 2 em 2). Qual é o próximo número?', '15', ['15', '16', '14', '13']),

    # Situações com números ordinais
    ('Em uma fila de ônibus, há cinco pessoas na sua frente. Que lugar você ocupa na fila (contando você)?', '6º', ['6º', '5º', '7º', '10º']),
    ('Você é o 6º da fila e chegaram mais quatro pessoas atrás de você. Qual lugar a última pessoa vai ocupar?', '10º', ['10º', '9º', '11º', '6º']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'mais_numeros', '2', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='mais_numeros', ano='2').count()
print(f"\n✅ Concluído! Total de questões de Mais Números (2º ano): {total}")
