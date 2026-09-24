"""
popular_desafios_calculo_problemas_divisao_troco.py
----------------------------------------
Execute na raiz do projeto:
    python popular_desafios_calculo_problemas_divisao_troco.py

Acrescenta ao card que JÁ EXISTE "Desafios de Cálculo" as
situações-problema da folha de Matemática de 23/09/2026 (divisão em
partes iguais, diferença, multiplicação, troco) e algumas variações.

Não apaga nem altera as questões que já estavam lá — só soma novas.
Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'desafios_calculo'


def criar_questao(disciplina, enunciado, resposta, erradas, modulo=MODULO):
    """Cria/atualiza uma questão de múltipla escolha (a certa + 3 erradas)."""
    opcoes = [resposta] + [e for e in erradas if e != resposta]
    assert len(opcoes) == len(set(opcoes)) == 4, f"Opções repetidas ou faltando: {enunciado}"
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
matematica, _ = Disciplina.objects.get_or_create(nome='matematica', defaults={'nome_exibicao': 'Matemática'})

print("\n🧠 Acrescentando a Desafios de Cálculo (folha de 23/09/2026)...")
questoes = [
    ('Para uma reunião com 6 pessoas, mamãe encomendou uma pizza dividida igualmente em 30 pedaços. '
     'Quantos pedaços cada pessoa poderá comer, no máximo?', '5', ['6', '4', '24']),
    ('Uma pizza de 30 pedaços foi dividida igualmente entre 6 pessoas, e cada uma comeu 5 pedaços. '
     'Quantos pedaços sobraram?', 'Nenhum (0)', ['1', '5', '6']),
    ('Mamãe usou uma corda de 18 centímetros e cortou-a, igualmente, em 3 pedaços. '
     'Com quantos centímetros ficou cada pedaço?', '6 cm', ['5 cm', '9 cm', '15 cm']),
    ('No condomínio de Marcos, a produção de lixo mensal é de 298 quilos. No condomínio de Tuco, é de 470 quilos. '
     'Qual é a diferença entre a produção de lixo dos dois condomínios?', '172 kg', ['182 kg', '768 kg', '272 kg']),
    ('João caminha 25 quilômetros por dia. Quantos quilômetros ele caminha, ao todo, em 6 dias?',
     '150 km', ['125 km', '31 km', '160 km']),
    ('Uma campanha arrecadou 1.500 brinquedos, que serão distribuídos igualmente entre 10 orfanatos. '
     'Quantos brinquedos cada orfanato receberá?', '150', ['15', '1.490', '105']),
    ('O ingresso de uma peça de teatro custa R$ 25,00. Lia, Ciça e Dani compraram um ingresso cada. '
     'Quanto custaram os ingressos no total?', 'R$ 75,00', ['R$ 50,00', 'R$ 28,00', 'R$ 70,00']),
    ('Lia, Ciça e Dani gastaram R$ 75,00 em ingressos e pagaram com uma nota de R$ 100,00. '
     'Quanto receberam de troco?', 'R$ 25,00', ['R$ 35,00', 'R$ 75,00', 'R$ 15,00']),
    # Variações
    ('Uma pizza com 24 pedaços foi dividida igualmente entre 4 amigos. Quantos pedaços cada um comeu?',
     '6', ['4', '8', '20']),
    ('Uma fita de 20 centímetros foi cortada em 4 pedaços iguais. Quantos centímetros tem cada pedaço?',
     '5 cm', ['4 cm', '6 cm', '16 cm']),
    ('Pedro comprou um livro de R$ 38,00 e pagou com uma nota de R$ 50,00. Quanto recebeu de troco?',
     'R$ 12,00', ['R$ 22,00', 'R$ 88,00', 'R$ 18,00']),
    ('Uma escola arrecadou 800 livros e vai dividir igualmente entre 4 bibliotecas. Quantos livros cada uma recebe?',
     '200', ['400', '204', '796']),
]
for enunciado, resposta, erradas in questoes:
    criar_questao(matematica, enunciado, resposta, erradas)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo=MODULO).count()
print(f"\n🎉 Pronto! O card 'Desafios de Cálculo' agora tem {total} questões.")
