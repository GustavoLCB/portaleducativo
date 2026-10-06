"""
popular_tabuada_trilha.py
----------------------------------------
Execute na raiz do projeto:
    python popular_tabuada_trilha.py

Popula o banco com o card de Matemática:
  - tabuada_trilha (Trilha da Tabuada (0 a 9))

Baseado na folha "Vamos treinar a tabuada?" (29/09/2026): todas as
100 contas de 0 × 0 até 9 × 9. No card, o aluno DIGITA o resultado
(15 contas sorteadas por partida). As 'opcoes' (resposta + 3 números
próximos) servem para a Prova Multidisciplinar, onde vira múltipla
escolha.

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'tabuada_trilha'


def opcoes_para(a, b):
    """A resposta certa + 3 erradas parecidas (tabuada vizinha), sem repetir nem ficar negativo."""
    certo = a * b
    candidatos = [a * (b + 1), a * (b - 1), (a + 1) * b, (a - 1) * b, certo + 1, certo + 2, certo + 10, certo - 1]
    erradas = []
    for c in candidatos:
        if c >= 0 and c != certo and c not in erradas:
            erradas.append(c)
        if len(erradas) == 3:
            break
    return [str(certo)] + [str(e) for e in erradas]


print("\n🧮 Garantindo disciplina Matemática...")
matematica, _ = Disciplina.objects.get_or_create(nome='matematica', defaults={'nome_exibicao': 'Matemática'})
print("  ✅ Matemática pronta.")

print("\n🐸 Populando: Matemática › Trilha da Tabuada (0 a 9)...")
criadas = 0
for a in range(10):
    for b in range(10):
        enunciado = f'{a} × {b} = ?'
        obj, criado = BancoQuestao.objects.update_or_create(
            disciplina=matematica, modulo=MODULO, enunciado=enunciado,
            defaults={
                'ano': '3',
                'tipo': 'completar_frase',
                'resposta_correta': str(a * b),
                'dados_extras': {'opcoes': opcoes_para(a, b), 'modo': 'digitar'},
                'ativo': True,
            }
        )
        criadas += criado

total = BancoQuestao.objects.filter(disciplina=matematica, modulo=MODULO).count()
print(f"  ✅ {criadas} contas novas criadas.")
print(f"\n🎉 Pronto! O card 'Trilha da Tabuada (0 a 9)' tem {total} contas.")
