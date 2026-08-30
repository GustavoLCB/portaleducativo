"""
popular_expressoes_numericas.py
--------------------------------
Execute na raiz do projeto:
    python popular_expressoes_numericas.py

Popula o banco com questões do NOVO card de Matemática — "Expressões
Numéricas" (expressões com mais de uma operação e parênteses, fator ou
divisor desconhecido, e cálculo direto de multiplicação/divisão), com
base no arquivo MATEMÁTICA.docx (Colégio Santo Agostinho).

Pode rodar de novo sem problema — não duplica questões existentes
(usa update_or_create, então se você me mandar uma correção de texto
depois, é só rodar de novo).
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

print("\n🧩 Populando: Matemática › Expressões Numéricas...")

questoes = [
    # Expressão com parênteses e mais de uma operação
    ('658 + (1.400 - 759) - 246 = ?', '1.053', ['1.053', '1.043', '1.153', '953']),

    # Fator/divisor desconhecido
    ('___ x 6 = 48. Qual é o número que falta?', '8', ['8', '6', '7', '42']),
    ('___ x 8 = 72. Qual é o número que falta?', '9', ['9', '8', '7', '64']),
    ('___ ÷ 8 = 32. Qual é o número que falta?', '256', ['256', '4', '40', '224']),

    # Cálculo direto (multiplicação e divisão)
    ('82 ÷ 2 = ?', '41', ['41', '40', '42', '44']),
    ('96 ÷ 3 = ?', '32', ['32', '33', '31', '30']),
    ('55 ÷ 5 = ?', '11', ['11', '10', '12', '15']),
    ('30 x 10 = ?', '300', ['300', '30', '3.000', '310']),
    ('16 x 30 = ?', '480', ['480', '460', '490', '180']),
    ('70 ÷ 10 = ?', '7', ['7', '70', '17', '700']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'expressoes_numericas', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='expressoes_numericas').count()
print(f"\n✅ Concluído! Total de questões de Expressões Numéricas: {total}")
