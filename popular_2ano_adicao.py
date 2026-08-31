"""
popular_2ano_adicao.py
------------------------
Execute na raiz do projeto:
    python popular_2ano_adicao.py

Popula o banco com questões do NOVO card de Matemática do 2º ANO —
"Adição" (somas simples, parcela desconhecida, situações-problema),
com base no material "Unidade 2 — Adição" do 2º ano (Colégio Santo
Agostinho).

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

print("\n➕ Populando: Matemática (2º ano) › Adição...")

questoes = [
    # Somas simples
    ('4 + 5 = ?', '9', ['9', '8', '10', '7']),
    ('2 + 5 = ?', '7', ['7', '6', '8', '5']),
    ('2 + 2 = ?', '4', ['4', '3', '5', '6']),
    ('1 + 4 + 3 = ?', '8', ['8', '7', '9', '6']),
    ('3 + 4 + 2 = ?', '9', ['9', '8', '10', '7']),

    # Parcela desconhecida
    ('3 + ___ = 7. Qual é o número que falta?', '4', ['4', '3', '5', '6']),
    ('5 + ___ = 8. Qual é o número que falta?', '3', ['3', '2', '4', '5']),

    # Situação-problema
    ('Lucas desenhou 5 triângulos em seu caderno e acrescentou mais 3. Quantos triângulos há ao todo?',
     '8', ['8', '7', '9', '6']),
    ('Ricardo tem 5 carrinhos e 4 bolas. No total, quantos carrinhos e bolas ele tem?',
     '9', ['9', '8', '10', '7']),
    ('Ricardo tem 3 petecas e 2 aviõezinhos. No total, quantas petecas e aviõezinhos ele tem?',
     '5', ['5', '4', '6', '3']),
    ('A equipe Corre Muito venceu 5 corridas e a equipe Muito Veloz venceu 4. Quantas corridas as duas equipes ganharam juntas?',
     '9', ['9', '8', '10', '7']),
    ('Na turma de Maria, 2 alunos preferem Matemática e 3 preferem Geografia. Quantos alunos preferem essas duas disciplinas juntas?',
     '5', ['5', '4', '6', '3']),
    ('Na turma de Maria, 4 alunos preferem Português, 2 preferem Matemática e 3 preferem Geografia. Qual é o número total de alunos entrevistados?',
     '9', ['9', '8', '10', '7']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'adicao', '2', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='adicao', ano='2').count()
print(f"\n✅ Concluído! Total de questões de Adição (2º ano): {total}")
