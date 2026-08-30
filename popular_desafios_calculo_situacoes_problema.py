"""
popular_desafios_calculo_situacoes_problema.py
---------------------------------------------
Execute na raiz do projeto:
    python popular_desafios_calculo_situacoes_problema.py

Acrescenta ao card JÁ EXISTENTE "Desafios de Cálculo" as situações-
problema (multiplicação, divisão, triplo, fração de uma quantidade)
extraídas do arquivo MATEMÁTICA.docx. Não mexe nas questões que já
estavam lá (popular_desafios_calculo.py) — só soma novas linhas.

Pode rodar de novo sem problema — não duplica questões existentes
(usa update_or_create, mesmo padrão dos outros scripts).
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

print("\n🧠 Acrescentando a Desafios de Cálculo (situações-problema do MATEMÁTICA.docx)...")

questoes = [
    ('O pai de Mário comprou uma bicicleta em 8 parcelas iguais de R$ 65,00. Quanto ele pagou pela bicicleta?',
     'R$ 520,00', ['R$ 520,00', 'R$ 510,00', 'R$ 530,00', 'R$ 480,00']),

    ('Um relojoeiro conserta 8 relógios em 1 dia. Quantos relógios ele conserta em 15 dias?',
     '120', ['120', '110', '130', '150']),

    ('Em uma excursão da escola foram utilizados 6 ônibus, cada um transportando 45 alunos. Quantos alunos participaram da excursão?',
     '270', ['270', '260', '280', '315']),

    ('Em uma partida de basquete, o time A marcou 52 pontos, e o time B marcou o triplo de pontos. Quantos pontos marcou o time B?',
     '156', ['156', '104', '150', '166']),

    ('Em uma gincana participaram 32 crianças, divididas em grupos com 1/8 do total em cada grupo. Quantas crianças ficaram em cada grupo?',
     '4', ['4', '8', '6', '2']),

    ('Nessa mesma gincana de 32 crianças, com 4 crianças em cada grupo (1/8 do total), quantos grupos foram formados ao todo?',
     '8', ['8', '4', '6', '16']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'desafios_calculo', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='desafios_calculo').count()
print(f"\n✅ Concluído! Total de questões de Desafios de Cálculo agora: {total}")
