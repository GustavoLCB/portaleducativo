"""
popular_fracoes_numeros.py
---------------------------
Execute na raiz do projeto:
    python popular_fracoes_numeros.py

Popula o banco com questões do NOVO card de Matemática — "Frações de
um Número" (metade, terça parte, quarta parte, quinta parte e sexta
parte de uma quantidade, incluindo dúzia/dezena/centena, e o problema
inverso "um número cuja metade é 15, qual é esse número?"), com base
no arquivo MATEMÁTICA.docx (Colégio Santo Agostinho).

Pode rodar de novo sem problema — não duplica questões existentes
(usa update_or_create).
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

print("\n🍰 Populando: Matemática › Frações de um Número...")

questoes = [
    # Metade
    ('Qual é a metade de 96?', '48', ['48', '46', '50', '44']),
    ('Qual é a metade de 14?', '7', ['7', '6', '8', '9']),
    ('Qual é a metade de 10?', '5', ['5', '4', '6', '3']),
    ('Qual é a metade de 100?', '50', ['50', '40', '55', '60']),

    # Terça parte
    ('Qual é a terça parte de 9?', '3', ['3', '2', '4', '6']),
    ('Qual é a terça parte de 15?', '5', ['5', '3', '6', '4']),
    ('Qual é a terça parte de 21?', '7', ['7', '6', '8', '3']),
    ('Qual é a terça parte de 180?', '60', ['60', '90', '50', '40']),

    # Quarta, quinta e sexta parte (com dúzia/dezena/centena)
    ('Seis dezenas equivalem a 60. Qual é a quarta parte de 60?', '15', ['15', '12', '20', '10']),
    ('Cinco dúzias equivalem a 60. Qual é a sexta parte de 60?', '10', ['10', '12', '6', '5']),
    ('Uma centena equivale a 100. Qual é a quinta parte de 100?', '20', ['20', '10', '25', '50']),
    ('Três dúzias equivalem a 36. Qual é a metade de 36?', '18', ['18', '12', '24', '9']),
    ('Nove dezenas equivalem a 90. Qual é a terça parte de 90?', '30', ['30', '45', '20', '60']),

    # Problema inverso (descobrir o número a partir da fração)
    ('Um número tem metade igual a 15. Qual é esse número?', '30', ['30', '15', '45', '20']),
    ('Um número tem terça parte igual a 10. Qual é esse número?', '30', ['30', '13', '20', '40']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'fracoes_numeros', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='fracoes_numeros').count()
print(f"\n✅ Concluído! Total de questões de Frações de um Número: {total}")
