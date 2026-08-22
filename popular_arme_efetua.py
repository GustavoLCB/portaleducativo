"""
popular_arme_efetua.py
------------------------
Execute na raiz do projeto:
    python popular_arme_efetua.py

Popula o banco com questões do novo card de Matemática "Arme e
Efetue": em vez de escolher entre 4 alternativas prontas, o aluno
digita o resultado casa por casa (unidade, dezena, centena...), como
faria armando a conta no caderno. Cobre as 4 operações: adição e
subtração (com reagrupamento/"vai um"/"empresta um"), multiplicação
por 1 algarismo e divisão exata ou com resto por 1 algarismo.

Formato de 'dados_extras' (diferente dos outros populate scripts,
porque aqui NÃO existem alternativas de múltipla escolha):
  - Adição, subtração, multiplicação:
        {'operador': '+', 'num1': 273, 'num2': 158, 'resultado': '431'}
  - Divisão:
        {'operador': '÷', 'dividendo': 39, 'divisor': 6,
         'quociente': '6', 'resto': '3'}

O campo 'resposta_correta' guarda:
  - Para + / − / ×: o resultado, ex: '431'
  - Para ÷: 'quociente|resto', ex: '6|3'

Por causa desse formato diferente, o módulo 'arme_efetua' NÃO entra
no catálogo da Prova Multidisciplinar (que espera sempre 4
alternativas prontas em 'dados_extras.opcoes').

Pode rodar de novo sem problema — usa update_or_create, então nunca
duplica e sempre atualiza se este arquivo for editado.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_questao_arme_efetua(disciplina, enunciado, resposta_correta, dados_extras):
    obj, criado = BancoQuestao.objects.update_or_create(
        disciplina=disciplina, modulo='arme_efetua', enunciado=enunciado,
        defaults={
            'tipo': 'arme_efetua',
            'resposta_correta': resposta_correta,
            'dados_extras': dados_extras,
            'ativo': True,
        }
    )
    status = "✅ Criado" if criado else "🔄 Atualizado"
    print(f"  {status}: {enunciado}")


print("\n🧮 Criando disciplina Matemática (se ainda não existir)...")
matematica, _ = Disciplina.objects.get_or_create(
    nome='matematica', defaults={'nome_exibicao': 'Matemática'}
)
print("  ✅ Matemática pronta.")


# ══════════════════════════════════════════════════════════════════
# ADIÇÃO (com reagrupamento — "vai um")
# ══════════════════════════════════════════════════════════════════
print("\n➕ Populando: Matemática › Arme e Efetue › Adição...")

adicoes = [
    (273, 158), (456, 289), (367, 258), (184, 297), (529, 346),
    (638, 195), (274, 489), (356, 467), (495, 238), (167, 758),
]
for num1, num2 in adicoes:
    resultado = str(num1 + num2)
    enunciado = f'Arme e efetue: {num1} + {num2}'
    criar_questao_arme_efetua(
        matematica, enunciado, resultado,
        {'operador': '+', 'num1': num1, 'num2': num2, 'resultado': resultado}
    )


# ══════════════════════════════════════════════════════════════════
# SUBTRAÇÃO (com reagrupamento — "empresta um")
# ══════════════════════════════════════════════════════════════════
print("\n➖ Populando: Matemática › Arme e Efetue › Subtração...")

subtracoes = [
    (542, 267), (631, 456), (800, 347), (725, 368), (913, 458),
    (604, 278), (852, 379), (700, 235), (461, 286), (950, 573),
]
for num1, num2 in subtracoes:
    resultado = str(num1 - num2)
    enunciado = f'Arme e efetue: {num1} - {num2}'
    criar_questao_arme_efetua(
        matematica, enunciado, resultado,
        {'operador': '-', 'num1': num1, 'num2': num2, 'resultado': resultado}
    )


# ══════════════════════════════════════════════════════════════════
# MULTIPLICAÇÃO (3 dígitos x 1 dígito)
# ══════════════════════════════════════════════════════════════════
print("\n✖️  Populando: Matemática › Arme e Efetue › Multiplicação...")

multiplicacoes = [
    (213, 3), (142, 4), (321, 3), (234, 2), (156, 4),
    (273, 3), (182, 4), (315, 3), (246, 3), (129, 5),
]
for num1, num2 in multiplicacoes:
    resultado = str(num1 * num2)
    enunciado = f'Arme e efetue: {num1} × {num2}'
    criar_questao_arme_efetua(
        matematica, enunciado, resultado,
        {'operador': '×', 'num1': num1, 'num2': num2, 'resultado': resultado}
    )


# ══════════════════════════════════════════════════════════════════
# DIVISÃO (1 dígito, exata ou com resto)
# ══════════════════════════════════════════════════════════════════
print("\n➗ Populando: Matemática › Arme e Efetue › Divisão...")

divisoes = [
    (84, 7), (96, 8), (72, 6), (108, 9), (56, 4),
    (135, 5), (144, 6), (91, 7), (39, 6), (25, 3),
]
for dividendo, divisor in divisoes:
    quociente, resto = divmod(dividendo, divisor)
    resposta_correta = f'{quociente}|{resto}'
    enunciado = f'Arme e efetue: {dividendo} ÷ {divisor}'
    criar_questao_arme_efetua(
        matematica, enunciado, resposta_correta,
        {
            'operador': '÷', 'dividendo': dividendo, 'divisor': divisor,
            'quociente': str(quociente), 'resto': str(resto),
        }
    )


# ── RESUMO ──────────────────────────────────────────────────────────
total = BancoQuestao.objects.filter(disciplina=matematica, modulo='arme_efetua').count()
print("\n" + "=" * 55)
print(f"✅ POPULAÇÃO DE ARME E EFETUE CONCLUÍDA! Total: {total} contas")
print("=" * 55)
