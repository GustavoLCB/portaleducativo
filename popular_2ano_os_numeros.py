"""
popular_2ano_os_numeros.py
----------------------------
Execute na raiz do projeto:
    python popular_2ano_os_numeros.py

Popula o banco com questões do NOVO card de Matemática do 2º ANO —
"Os Números" (contagem, comparação, ordem crescente/decrescente,
dúzia, dobro/metade simples), com base no material "Unidade 1 — Os
números" do 2º ano (Colégio Santo Agostinho).

IMPORTANTE: este módulo é isolado por 'ano=2', então não interfere em
nada do que já existe para o 3º ano, mesmo que algum nome de módulo
seja parecido.

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

print("\n🔢 Populando: Matemática (2º ano) › Os Números...")

questoes = [
    # Comparação de quantidades
    ('No empilhamento, havia 6 cubos verdes, 4 laranja, 5 rosa e 3 azuis. Quantos cubos havia ao todo?',
     '18', ['18', '17', '19', '16']),
    ('Qual é o menor número entre 4, 8, 1, 3, 5, 9 e 2?', '1', ['1', '2', '3', '4']),
    ('Qual é o maior número entre 6, 8, 3, 1, 5, 7 e 9?', '9', ['9', '8', '7', '6']),

    # Comparação de idades (situação-problema)
    ('Raquel tem 8 anos, Renata tem 5 anos e Daniela tem 7 anos. Quem é a mais velha das três?',
     'Raquel', ['Raquel', 'Renata', 'Daniela', 'Nenhuma']),
    ('Raquel tem 8 anos, Renata tem 5 anos e Daniela tem 7 anos. Quem é a mais nova das três?',
     'Renata', ['Renata', 'Raquel', 'Daniela', 'Nenhuma']),

    # Convenções numéricas (semana, dúzia, dobro, metade)
    ('Uma semana tem quantos dias?', '7', ['7', '5', '6', '8']),
    ('Comprei meia dúzia de bananas. Quantas bananas eu comprei?', '6', ['6', '12', '3', '5']),
    ('Qual é a metade de 4?', '2', ['2', '4', '1', '3']),
    ('Qual é o dobro de 4?', '8', ['8', '4', '2', '16']),

    # Situação-problema (divisão em grupos)
    ('Fátima comprou 9 novelos de lã. Para fazer cada cachecol, ela usa 2 novelos. Quantos cachecóis ela consegue fazer com os 9 novelos?',
     '4', ['4', '3', '5', '9']),
    ('Fátima tinha 9 novelos de lã e usou 2 em cada cachecol, fazendo 4 cachecóis. Sobrou algum novelo? Quantos?',
     '1', ['1', '0', '2', '3']),

    # Contagem de moedas
    ('Havia 4 moedas de 1 real em um quadro. Foram desenhadas mais 2 moedas de 1 real. Quantos reais há agora no quadro?',
     '6', ['6', '5', '7', '4']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'os_numeros', '2', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='os_numeros', ano='2').count()
print(f"\n✅ Concluído! Total de questões de Os Números (2º ano): {total}")
