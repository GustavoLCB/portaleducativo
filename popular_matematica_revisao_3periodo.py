"""
popular_matematica_revisao_3periodo.py
------------------------------------------
Execute na raiz do projeto:
    python popular_matematica_revisao_3periodo.py

Popula o banco com o novo card de Matemática — "MAT - Revisão 3º
Período" (módulo revisao_3periodo): frações de um número (terça e
quarta parte), subtração e divisão com prova real, dezenas e números
romanos (conversão, antecessor e sucessor).

Baseado no arquivo "Matematica PROVA REVISAO 15-09-2026.docx"
(Colégio Santo Agostinho).

Mesmo padrão dos outros populate scripts — pode rodar de novo sem
problema, não duplica questões existentes (usa update_or_create).
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


print("\n🧮 Garantindo disciplina Matemática...")
matematica, _ = Disciplina.objects.get_or_create(
    nome='matematica', defaults={'nome_exibicao': 'Matemática'}
)
print("  ✅ Matemática pronta.")

print("\n📝 Populando: Matemática › MAT - Revisão 3º Período...")

revisao_3periodo = [
    # ── Frações de um número (situações-problema) ──
    ('João tinha 24 figurinhas e decidiu dar a quarta parte delas para seu irmão. Quantas figurinhas ele deu?', '6',
     ['6', '8', '4', '12']),
    ('Davi tem 93 brinquedos e quer separar a terça parte deles para dar ao Caio. Quantos brinquedos Davi dará ao Caio?', '31',
     ['31', '30', '33', '93']),
    ('A terça parte dos 957 alunos de uma escola faltou no dia da Festa das Missões. Quantos alunos faltaram?', '319',
     ['319', '320', '318', '638']),
    ('Nessa mesma escola de 957 alunos, se a terça parte faltou na Festa das Missões, quantos alunos participaram da festa?', '638',
     ['638', '319', '957', '320']),

    # ── Subtração com prova real ──
    ('Qual é o resultado de 5.274 − 1.859?', '3.415',
     ['3.415', '3.425', '3.315', '3.515']),
    ('Para conferir se 5.274 − 1.859 = 3.415 está certo, qual é a prova real (conta de conferência) dessa subtração?', '3.415 + 1.859 = 5.274',
     ['3.415 + 1.859 = 5.274', '5.274 + 1.859 = 7.133', '3.415 − 1.859 = 1.556', '1.859 − 3.415 = 1.556']),

    # ── Divisão com prova real ──
    ('Quanto é 72 ÷ 8?', '9',
     ['9', '8', '7', '6']),
    ('Para conferir se 72 ÷ 8 = 9 está certo, qual é a prova real (conta de conferência) dessa divisão?', '9 × 8 = 72',
     ['9 × 8 = 72', '9 + 8 = 17', '72 × 8 = 576', '9 ÷ 8 = 72']),

    # ── Dezenas ──
    ('Para o lançamento de um carrinho, uma vendedora encomendou 100 dezenas de miniaturas. Quantas miniaturas foram encomendadas ao todo?', '1.000',
     ['1.000', '100', '10.000', '900']),

    # ── Situação-problema: divisão com resto ──
    ('Luís recebeu 500 figurinhas para distribuir entre 26 crianças e deu 9 figurinhas a cada uma. Quantas figurinhas sobraram?', '266',
     ['266', '234', '256', '274']),

    # ── Números romanos: conversão ──
    ('Como se escreve o número 10 em algarismos romanos?', 'X', ['X', 'IX', 'XI', 'V']),
    ('Como se escreve o número 15 em algarismos romanos?', 'XV', ['XV', 'VX', 'XIV', 'XVI']),
    ('Como se escreve o número 20 em algarismos romanos?', 'XX', ['XX', 'XIX', 'XXI', 'IX']),
    ('Como se escreve o número 2 em algarismos romanos?', 'II', ['II', 'I', 'III', 'IV']),
    ('Como se escreve o número 14 em algarismos romanos?', 'XIV', ['XIV', 'XVI', 'XIIII', 'IXV']),
    ('Como se escreve o número 4 em algarismos romanos?', 'IV', ['IV', 'VI', 'IIII', 'V']),
    ('Como se escreve o número 19 em algarismos romanos?', 'XIX', ['XIX', 'XVIIII', 'XXI', 'IXX']),
    ('Como se escreve o número 5 em algarismos romanos?', 'V', ['V', 'IV', 'VI', 'X']),
    ('Como se escreve o número 18 em algarismos romanos?', 'XVIII', ['XVIII', 'XIIX', 'XIX', 'XVII']),

    # ── Números romanos: antecessor e sucessor ──
    ('Qual número romano vem imediatamente antes de XI (11)?', 'X', ['X', 'IX', 'XII', 'VIII']),
    ('Qual número romano vem imediatamente depois de XI (11)?', 'XII', ['XII', 'X', 'XIII', 'IX']),
    ('Qual número romano vem imediatamente antes de VII (7)?', 'VI', ['VI', 'V', 'VIII', 'IV']),
    ('Qual número romano vem imediatamente depois de VII (7)?', 'VIII', ['VIII', 'IX', 'VI', 'VII']),
    ('Qual número romano vem imediatamente antes de XIX (19)?', 'XVIII', ['XVIII', 'XVII', 'XX', 'XVI']),
    ('Qual número romano vem imediatamente depois de XIX (19)?', 'XX', ['XX', 'XXI', 'XVIII', 'XVII']),
    ('Qual número romano vem imediatamente antes de IV (4)?', 'III', ['III', 'II', 'V', 'I']),
    ('Qual número romano vem imediatamente depois de IV (4)?', 'V', ['V', 'VI', 'III', 'IV']),
    ('Qual número romano vem imediatamente antes de XVII (17)?', 'XVI', ['XVI', 'XV', 'XVIII', 'XIV']),
    ('Qual número romano vem imediatamente depois de XVII (17)?', 'XVIII', ['XVIII', 'XIX', 'XVI', 'XX']),
    ('Qual número romano vem imediatamente antes de XX (20)?', 'XIX', ['XIX', 'XVIII', 'XXI', 'XVII']),
    ('Qual número romano vem imediatamente depois de XX (20)?', 'XXI', ['XXI', 'XIX', 'XXII', 'XVIII']),
]
for enunciado, resposta, opcoes in revisao_3periodo:
    criar_questao(matematica, 'revisao_3periodo', enunciado, resposta, opcoes)


print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE MATEMÁTICA › MAT - REVISÃO 3º PERÍODO CONCLUÍDA!")
print("=" * 55)
total = BancoQuestao.objects.filter(disciplina=matematica, modulo='revisao_3periodo').count()
print(f"   {{'MAT - Revisão 3º Período':.<32}} {{total}}")
