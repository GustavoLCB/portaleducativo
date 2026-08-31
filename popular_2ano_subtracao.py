"""
popular_2ano_subtracao.py
----------------------------
Execute na raiz do projeto:
    python popular_2ano_subtracao.py

Popula o banco com questões do NOVO card de Matemática do 2º ANO —
"Subtração e Operações Inversas" (subtrações simples, minuendo ou
subtraendo desconhecido, sinal + ou −, situações-problema e
sequências), com base no material "Unidade 3 — Subtração e operações
inversas" do 2º ano (Colégio Santo Agostinho).

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

print("\n➖ Populando: Matemática (2º ano) › Subtração e Operações Inversas...")

questoes = [
    # Subtrações simples
    ('7 - 4 = ?', '3', ['3', '4', '2', '11']),
    ('8 - 5 = ?', '3', ['3', '2', '4', '13']),
    ('9 - 3 = ?', '6', ['6', '5', '7', '12']),
    ('4 - 1 = ?', '3', ['3', '2', '4', '5']),
    ('4 - 3 = ?', '1', ['1', '0', '2', '7']),
    ('5 - 3 = ?', '2', ['2', '1', '3', '8']),
    ('6 - 3 = ?', '3', ['3', '2', '4', '9']),

    # Sinal + ou -
    ('Complete com o sinal + ou −: 3 ___ 1 = 4', '+', ['+', '−']),
    ('Complete com o sinal + ou −: 7 ___ 2 = 5', '−', ['−', '+']),
    ('Complete com o sinal + ou −: 4 ___ 3 = 1', '−', ['−', '+']),
    ('Complete com o sinal + ou −: 2 ___ 4 = 6', '+', ['+', '−']),

    # Minuendo/subtraendo desconhecido
    ('4 - ___ = 2. Qual é o número que falta?', '2', ['2', '1', '3', '6']),
    ('8 - ___ = 5. Qual é o número que falta?', '3', ['3', '2', '4', '13']),
    ('___ - 5 = 0. Qual é o número que falta?', '5', ['5', '0', '10', '4']),
    ('___ - 1 = 4. Qual é o número que falta?', '5', ['5', '4', '6', '3']),
    ('___ - 3 = 1. Qual é o número que falta?', '4', ['4', '3', '5', '1']),
    ('3 - ___ = 1. Qual é o número que falta?', '2', ['2', '1', '3', '4']),

    # Situações-problema
    ('Mário tinha 9 bolas de tênis. Perdeu 3 delas. Com quantas bolas ele ficou?',
     '6', ['6', '5', '7', '3']),
    ('Isabela pegou 7 maçãs e Ana pegou 4 maçãs no pomar. Quantas maçãs a mais Isabela pegou em relação a Ana?',
     '3', ['3', '2', '4', '11']),
    ('O compartimento de latas da geladeira tem 4 espaços, e Mário já colocou 4 latinhas de suco. Quantos espaços ainda faltam para completar?',
     '0', ['0', '1', '2', '4']),
    ('Uma bandeja de ovos tem 6 espaços, e há apenas 1 ovo nela. Quantos ovos ainda faltam para completar a bandeja?',
     '5', ['5', '4', '6', '1']),
    ('Para fazer uma casinha, Bruno comprou 5 folhas de cartolina. Utilizou 3. Com quantas folhas de cartolina ele ficou?',
     '2', ['2', '3', '1', '8']),
    ('Em um jogo de basquete, Janete fez 9 cestas, e Alessandra, 7. Quantas cestas Janete fez a mais que Alessandra?',
     '2', ['2', '3', '1', '16']),
    ('Daniela tinha 7 lápis e perdeu 3. Com quantos lápis ela ficou?',
     '4', ['4', '3', '5', '10']),
    ('Iaci tinha 8 laranjas. Utilizou 3 delas para fazer um suco. Com quantas laranjas Iaci ficou?',
     '5', ['5', '4', '6', '11']),
    ('Um coqueiro tinha 7 cocos. Caíram 4. Quantos cocos ficaram no coqueiro?',
     '3', ['3', '4', '2', '11']),

    # Sequências
    ('Em uma sequência que aumenta de 3 em 3, começando no 2 (2, 5, 8, 11, ...), qual número vem depois do 11?',
     '14', ['14', '13', '15', '17']),
    ('Em uma sequência que diminui de 2 em 2, começando no 13 (13, 11, 9, 7, ...), qual número vem depois do 7?',
     '5', ['5', '6', '4', '3']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'subtracao', '2', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='subtracao', ano='2').count()
print(f"\n✅ Concluído! Total de questões de Subtração (2º ano): {total}")
