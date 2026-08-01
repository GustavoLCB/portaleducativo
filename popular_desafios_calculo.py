"""
popular_desafios_calculo.py
----------------------------
Execute na raiz do projeto:
    python popular_desafios_calculo.py

Popula o banco com questões de Matemática — "Desafios de Cálculo"
(expressões numéricas, cálculo mental com múltiplos de 10/100/1.000,
multiplicação e divisão armadas, situações-problema, leitura de
gráficos e termos da multiplicação), com base nas folhas de
28, 29 e 30/07/2026 (Colégio Santo Agostinho, 3º ano).

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_questao(disciplina, modulo, enunciado, resposta, opcoes):
    obj, criado = BancoQuestao.objects.get_or_create(
        disciplina=disciplina, modulo=modulo, enunciado=enunciado,
        defaults={
            'tipo': 'multipla_escolha',
            'resposta_correta': resposta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "⏭️  Já existe"
    print(f"  {status}: {enunciado[:65]}")


print("\n🧮 Criando disciplina Matemática (se ainda não existir)...")
matematica, _ = Disciplina.objects.get_or_create(
    nome='matematica', defaults={'nome_exibicao': 'Matemática'}
)
print("  ✅ Matemática pronta.")

print("\n🧠 Populando: Matemática › Desafios de Cálculo...")

questoes = [
    # Expressões numéricas
    ('380 - 36 ÷ 6 + 82 = ?', '456', ['456', '446', '374', '462']),
    ('6 × 5 + 840 - 216 = ?', '654', ['654', '630', '846', '624']),
    ('1.567 + 64 - 45 × 10 = ?', '1.181', ['1.181', '1.171', '1.281', '1.081']),
    ('467 - 36 ÷ 9 + 2.310 = ?', '2.773', ['2.773', '2.763', '2.673', '2.873']),

    # Multiplicação por 10, 100 e 1.000 (cálculo mental)
    ('15 × 100 = ?', '1.500', ['1.500', '150', '15.000', '1.050']),
    ('4 × 1.000 = ?', '4.000', ['4.000', '400', '40.000', '4.400']),
    ('30 × 100 = ?', '3.000', ['3.000', '300', '30.000', '3.300']),
    ('3.600 × 10 = ?', '36.000', ['36.000', '3.600', '360.000', '3.060']),
    ('8 × 1.000 = ?', '8.000', ['8.000', '800', '80.000', '8.800']),

    # Cálculo mental com sinais = e ≠
    ('Complete com o sinal correto: 6 × 60 ___ 360', '=', ['=', '≠', '>', '<']),
    ('Complete com o sinal correto: 4 × 20 ___ 120', '≠', ['≠', '=', '>', '<']),
    ('Complete com o sinal correto: 7 × 50 ___ 450', '≠', ['≠', '=', '>', '<']),
    ('Complete com o sinal correto: 24 × 100 ___ 2.040', '≠', ['≠', '=', '>', '<']),

    # Multiplicação e divisão armadas
    ('470 × 6 = ?', '2.820', ['2.820', '2.814', '2.720', '2.920']),
    ('342 × 7 = ?', '2.394', ['2.394', '2.384', '2.304', '2.494']),
    ('238 × 8 = ?', '1.904', ['1.904', '1.884', '1.814', '1.994']),
    ('637 × 2 = ?', '1.274', ['1.274', '1.264', '1.174', '1.374']),
    ('526 × 5 = ?', '2.630', ['2.630', '2.620', '2.530', '2.730']),
    ('387 × 9 = ?', '3.483', ['3.483', '3.473', '3.383', '3.583']),
    ('35 ÷ 7 = ?', '5', ['5', '6', '7', '4']),
    ('64 ÷ 8 = ?', '8', ['8', '7', '9', '6']),
    ('54 ÷ 9 = ?', '6', ['6', '5', '7', '9']),

    # Termos da multiplicação
    ('Qual termo indica quantas vezes a quantidade será repetida?', 'Multiplicando',
     ['Multiplicando', 'Multiplicador', 'Produto', 'Quociente']),
    ('Qual termo representa o resultado da multiplicação?', 'Produto',
     ['Produto', 'Multiplicando', 'Multiplicador', 'Fator']),

    # Situações-problema
    ('Paula tem 74 carrinhos. Carlos tem o triplo dos carrinhos de Paula. Quantos carrinhos Carlos tem?', '222',
     ['222', '148', '176', '296']),
    ('Uma doceira fez 456 brigadeiros pretos, 300 cajuzinhos, 1.042 doces de coco e 585 brigadeiros brancos. Quantos doces ela fez ao todo?', '2.383',
     ['2.383', '2.373', '2.483', '2.283']),
    ('A doceira fez 585 brigadeiros brancos e 456 pretos. Quantos brigadeiros brancos a mais que pretos ela fez?', '129',
     ['129', '139', '119', '121']),
    ('Uma encomenda custou R$ 318,00 e foi paga com 4 notas de R$ 100,00. Qual é o troco?', 'R$ 82,00',
     ['R$ 82,00', 'R$ 92,00', 'R$ 72,00', 'R$ 118,00']),
    ('Numa pesquisa sobre brincadeiras preferidas, Pique-esconde recebeu 90 votos e Pique-pega recebeu 70. Quantos votos as duas brincadeiras mais votadas têm juntas?', '160',
     ['160', '150', '170', '140']),

    # Valor posicional
    ('No número 2.497, quantas ordens ele possui?', '4', ['4', '2', '7', '9']),
    ('No número 2.497, quantas centenas ele tem?', '24', ['24', '4', '9', '49']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'desafios_calculo', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='desafios_calculo').count()
print(f"\n✅ Concluído! Total de questões de Desafios de Cálculo: {total}")
