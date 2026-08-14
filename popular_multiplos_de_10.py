"""
popular_multiplos_de_10.py
----------------------------
Execute na raiz do projeto:
    python popular_multiplos_de_10.py

Popula o banco com questões de Matemática — "Multiplicação por
Dezenas, Centenas e Milhares" (multiplicar por 10, 100, 1.000 e o
truque de multiplicar por 20, 30 e 40), com base nos cadernos de
atividade (Multiplicação por 20,30,40 — Caderno 13; Multiplicação por
10,100 e 1000 — Caderno 11), Colégio Santo Agostinho, 3º ano.

Pode rodar de novo sem problema — não duplica questões existentes.
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


print("\n🧮 Criando disciplina Matemática (se ainda não existir)...")
matematica, _ = Disciplina.objects.get_or_create(
    nome='matematica', defaults={'nome_exibicao': 'Matemática'}
)
print("  ✅ Matemática pronta.")

print("\n🔟 Populando: Matemática › Multiplicação por Dezenas, Centenas e Milhares...")

questoes = [
    # Multiplicar por 10 (acrescentar 1 zero)
    ('7 × 10 = ?', '70', ['70', '7', '700', '80']),
    ('9 × 10 = ?', '90', ['90', '9', '900', '100']),
    ('23 × 10 = ?', '230', ['230', '23', '2.300', '240']),
    ('45 × 10 = ?', '450', ['450', '45', '4.500', '460']),
    ('68 × 10 = ?', '680', ['680', '68', '6.800', '690']),
    ('84 × 10 = ?', '840', ['840', '84', '8.400', '850']),
    ('99 × 10 = ?', '990', ['990', '99', '9.900', '1.000']),
    ('150 × 10 = ?', '1.500', ['1.500', '150', '15.000', '1.510']),
    ('238 × 10 = ?', '2.380', ['2.380', '238', '23.800', '2.390']),
    ('306 × 10 = ?', '3.060', ['3.060', '306', '30.600', '3.070']),

    # Multiplicar por 100 (acrescentar 2 zeros)
    ('3 × 100 = ?', '300', ['300', '30', '3.000', '400']),
    ('12 × 100 = ?', '1.200', ['1.200', '120', '12.000', '1.300']),
    ('54 × 100 = ?', '5.400', ['5.400', '540', '54.000', '5.500']),
    ('257 × 100 = ?', '25.700', ['25.700', '2.570', '257.000', '25.800']),
    ('6 × 100 = ?', '600', ['600', '60', '6.000', '700']),
    ('45 × 100 = ?', '4.500', ['4.500', '450', '45.000', '4.600']),
    ('78 × 100 = ?', '7.800', ['7.800', '780', '78.000', '7.900']),
    ('120 × 100 = ?', '12.000', ['12.000', '1.200', '120.000', '12.100']),

    # Multiplicar por 1.000 (acrescentar 3 zeros)
    ('5 × 1.000 = ?', '5.000', ['5.000', '500', '50.000', '6.000']),
    ('9 × 1.000 = ?', '9.000', ['9.000', '900', '90.000', '10.000']),
    ('4 × 1.000 = ?', '4.000', ['4.000', '400', '40.000', '5.000']),
    ('12 × 1.000 = ?', '12.000', ['12.000', '1.200', '120.000', '13.000']),
    ('45 × 1.000 = ?', '45.000', ['45.000', '4.500', '450.000', '46.000']),
    ('100 × 1.000 = ?', '100.000', ['100.000', '10.000', '1.000.000', '101.000']),

    # Multiplicar por 20, 30 e 40 (truque: multiplica o algarismo, depois por 10)
    ('2 × 20 = ?', '40', ['40', '4', '400', '60']),
    ('3 × 20 = ?', '60', ['60', '6', '600', '80']),
    ('4 × 20 = ?', '80', ['80', '8', '800', '100']),
    ('5 × 20 = ?', '100', ['100', '10', '1.000', '120']),
    ('6 × 20 = ?', '120', ['120', '12', '1.200', '140']),
    ('7 × 20 = ?', '140', ['140', '14', '1.400', '160']),
    ('8 × 20 = ?', '160', ['160', '16', '1.600', '180']),
    ('9 × 20 = ?', '180', ['180', '18', '1.800', '200']),
    ('2 × 30 = ?', '60', ['60', '6', '600', '90']),
    ('3 × 30 = ?', '90', ['90', '9', '900', '120']),
    ('4 × 30 = ?', '120', ['120', '12', '1.200', '150']),
    ('5 × 30 = ?', '150', ['150', '15', '1.500', '180']),
    ('6 × 30 = ?', '180', ['180', '18', '1.800', '210']),
    ('7 × 30 = ?', '210', ['210', '21', '2.100', '240']),
    ('8 × 30 = ?', '240', ['240', '24', '2.400', '270']),
    ('9 × 30 = ?', '270', ['270', '27', '2.700', '300']),
    ('2 × 40 = ?', '80', ['80', '8', '800', '120']),
    ('3 × 40 = ?', '120', ['120', '12', '1.200', '160']),
    ('4 × 40 = ?', '160', ['160', '16', '1.600', '200']),
    ('5 × 40 = ?', '200', ['200', '20', '2.000', '240']),
    ('6 × 40 = ?', '240', ['240', '24', '2.400', '280']),
    ('7 × 40 = ?', '280', ['280', '28', '2.800', '320']),
    ('8 × 40 = ?', '320', ['320', '32', '3.200', '360']),
    ('9 × 40 = ?', '360', ['360', '36', '3.600', '400']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'multiplos_de_10', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='multiplos_de_10').count()
print(f"\n✅ Concluído! Total de questões de Multiplicação por Dezenas, Centenas e Milhares: {total}")
