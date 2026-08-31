"""
popular_2ano_figuras_geometricas.py
--------------------------------------
Execute na raiz do projeto:
    python popular_2ano_figuras_geometricas.py

Popula o banco com questões do NOVO card de Matemática do 2º ANO —
"Figuras Geométricas" (vértices, faces e arestas de cubo, pirâmide,
cone, cilindro e esfera, e associação com objetos do dia a dia), com
base no material "Unidade 4 — Figuras geométricas" do 2º ano (Colégio
Santo Agostinho).

Observação: os exercícios de contar cubinhos em blocos e o labirinto
da malha quadriculada não entraram aqui porque dependem de enxergar a
imagem — não dá pra transformar em pergunta de texto com segurança.
Fiquei só com o que é 100% verificável em texto (propriedades das
figuras geométricas).

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

print("\n🔺 Populando: Matemática (2º ano) › Figuras Geométricas...")

questoes = [
    # Cubo
    ('Quantos vértices tem um cubo?', '8', ['8', '6', '12', '4']),
    ('Quantas faces tem um cubo?', '6', ['6', '8', '4', '12']),
    ('Quantas arestas tem um cubo?', '12', ['12', '8', '6', '10']),
    ('Qual figura geométrica tem seis faces e oito vértices?', 'Cubo', ['Cubo', 'Pirâmide', 'Cone', 'Cilindro']),

    # Cilindro
    ('Quantos vértices tem um cilindro?', '0', ['0', '2', '1', '4']),
    ('Qual figura geométrica tem duas bases circulares?', 'Cilindro', ['Cilindro', 'Cone', 'Esfera', 'Cubo']),
    ('Uma lata de refrigerante se parece com qual figura geométrica?', 'Cilindro', ['Cilindro', 'Cone', 'Esfera', 'Cubo']),

    # Cone
    ('Qual figura tem uma base circular e termina em um único vértice no topo?', 'Cone', ['Cone', 'Cilindro', 'Esfera', 'Cubo']),
    ('Um cone de trânsito se parece com qual figura geométrica?', 'Cone', ['Cone', 'Cilindro', 'Esfera', 'Pirâmide']),

    # Esfera
    ('Qual figura geométrica não tem vértices e pode rolar com facilidade para qualquer lado?', 'Esfera', ['Esfera', 'Cubo', 'Cone', 'Pirâmide']),
    ('Um globo terrestre se parece com qual figura geométrica?', 'Esfera', ['Esfera', 'Cilindro', 'Cone', 'Cubo']),

    # Pirâmide de base quadrada
    ('Quantos vértices tem uma pirâmide de base quadrada?', '5', ['5', '4', '6', '8']),
    ('Quantas faces tem uma pirâmide de base quadrada?', '5', ['5', '4', '6', '8']),
    ('Quantas arestas tem uma pirâmide de base quadrada?', '8', ['8', '4', '5', '12']),
    ('Quantas arestas tem a base de uma pirâmide de base quadrada?', '4', ['4', '3', '5', '8']),
    ('Qual figura geométrica tem uma base quadrada e cinco vértices?', 'Pirâmide', ['Pirâmide', 'Cubo', 'Cone', 'Cilindro']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'figuras_geometricas', '2', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='figuras_geometricas', ano='2').count()
print(f"\n✅ Concluído! Total de questões de Figuras Geométricas (2º ano): {total}")
