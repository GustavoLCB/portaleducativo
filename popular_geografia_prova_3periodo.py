"""
popular_geografia_prova_3periodo.py
----------------------------------------
Execute na raiz do projeto:
    python popular_geografia_prova_3periodo.py

Popula o banco com o novo card de Geografia:
  - prova_3periodo (GEO - Prova 3º Período)

Baseado na Prova de Geografia do 3º Período (09/09/2026) —
Colégio Santo Agostinho:
  - "As cidades estão crescendo" e o gráfico da população urbana e
    rural no Brasil (1950–2022)
  - Atividades econômicas da cidade (comércio, indústria, serviços)
  - Indústria e setores da economia
  - Comércio virtual
  - Os rios: utilidades da água e como evitar a poluição
  - Desmatamento, mata ciliar e assoreamento
  - Extrativismo sustentável x predatório
  - Extrativismo animal, vegetal e mineral

Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao

MODULO = 'prova_3periodo'


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


print("\n🌎 Garantindo disciplina Geografia...")
geografia, _ = Disciplina.objects.get_or_create(nome='geografia', defaults={'nome_exibicao': 'Geografia'})
print("  ✅ Geografia pronta.")

print("\n🏆 Populando: Geografia › GEO - Prova 3º Período...")
G = '(Gráfico: população urbana x rural no Brasil, de 1950 a 2022)\n'
questoes = [
    # ── Urbanização ──
    (G + 'Em quais anos a população do CAMPO foi maior que a população da CIDADE?', '1950 e 1960',
     ['2000 e 2010', '1980 e 1991', '2010 e 2022']),
    (G + 'A partir de que ano a população da CIDADE ficou maior que a do CAMPO?', '1970',
     ['1950', '2022', '1960']),
    (G + 'O que aconteceu com a população URBANA de 1950 a 2022?', 'Cresceu muito',
     ['Diminuiu muito', 'Ficou igual', 'Desapareceu']),
    (G + 'Hoje, a maior parte da população brasileira vive...', 'nas cidades', ['no campo', 'nas florestas', 'no mar']),
    ('Quando muitas pessoas saem do campo para morar na cidade, chamamos isso de...', 'êxodo rural',
     ['extrativismo', 'assoreamento', 'desmatamento']),
    ('O crescimento das cidades é chamado de...', 'urbanização', ['industrialização', 'extrativismo', 'pecuária']),

    # ── Atividades econômicas ──
    ('Quais são as principais atividades econômicas da CIDADE?', 'Comércio, indústria e serviços',
     ['Agricultura, pecuária e pesca', 'Apenas a pecuária', 'Apenas o extrativismo']),
    ('Verdadeiro ou falso: "A indústria necessita de matérias-primas vindas do campo."', 'Verdadeiro',
     ['Falso', 'Só no inverno', 'Só a indústria de brinquedos']),
    ('Verdadeiro ou falso: "A indústria pertence ao setor primário da economia."', 'Falso',
     ['Verdadeiro', 'Só no campo', 'Só nas grandes cidades']),
    ('Verdadeiro ou falso: "A indústria produz roupas e máquinas que abastecem o campo."', 'Verdadeiro',
     ['Falso', 'Só roupas', 'Só no exterior']),
    ('O que é o COMÉRCIO VIRTUAL?', 'Comprar e vender produtos utilizando a internet',
     ['Montar uma loja de brinquedos dentro do shopping', 'Fazer compras usando moedas e cédulas de papel',
      'Trocar brinquedos antigos na praça do bairro']),

    # ── Setores da economia ──
    ('A PECUÁRIA pertence a qual setor da economia?', 'Setor primário', ['Setor secundário', 'Setor terciário', 'Setor virtual']),
    ('O COMÉRCIO pertence a qual setor da economia?', 'Setor terciário', ['Setor primário', 'Setor secundário', 'Setor rural']),
    ('A INDÚSTRIA pertence a qual setor da economia?', 'Setor secundário', ['Setor primário', 'Setor terciário', 'Setor rural']),
    ('Qual atividade pertence ao setor TERCIÁRIO (comércio e serviços)?', 'Uma farmácia vendendo remédios',
     ['Uma fábrica de roupas', 'A criação de gado', 'A plantação de milho']),

    # ── Rios ──
    ('Os rios são como "as veias do nosso planeta" porque...', 'transportam a água e levam vida por onde passam',
     ['são feitos de sangue', 'ficam dentro das cidades', 'não têm importância']),
    ('Qual é uma utilidade da água?', 'Beber e tomar banho', ['Jogar lixo', 'Fazer fumaça', 'Construir prédios de areia']),
    ('Como podemos evitar a poluição dos rios?', 'Não jogando lixo nas margens e não poluindo as águas',
     ['Jogando lixo só à noite', 'Cortando as árvores das margens', 'Gastando bastante água']),

    # ── Desmatamento, mata ciliar e assoreamento ──
    ('Como se chama a retirada da vegetação de um local, que pode causar grande impacto ambiental?', 'Desmatamento',
     ['Mata ciliar', 'Assoreamento', 'Pecuária']),
    ('Como se chama a vegetação que fica às margens dos rios?', 'Mata ciliar',
     ['Desmatamento', 'Assoreamento', 'Pecuária']),
    ('Como se chama o acúmulo de terra, rochas e lixo que torna os rios mais rasos?', 'Assoreamento',
     ['Mata ciliar', 'Desmatamento', 'Extrativismo']),

    # ── Extrativismo ──
    ('Uma comunidade coleta castanhas que já caíram das árvores, deixando parte delas para os animais e para '
     'novas árvores nascerem. Esse extrativismo é...', 'sustentável', ['predatório', 'mineral', 'industrial']),
    ('Uma empresa derrubou centenas de árvores de uma só vez para vender a madeira, deixando o solo sem proteção '
     'e os animais sem abrigo. Esse extrativismo é...', 'predatório', ['sustentável', 'animal', 'terciário']),
    ('O que pode acontecer ao meio ambiente se praticarmos apenas o extrativismo PREDATÓRIO?',
     'Desmatamento, erosão do solo e animais sem abrigo', ['As florestas vão crescer mais', 'Os rios ficarão mais fundos',
                                                            'Nada vai mudar']),
    ('Coleta de látex de seringueiras para fabricar borracha natural é extrativismo...', 'vegetal',
     ['animal', 'mineral', 'industrial']),
    ('Pesca tradicional de camarão no litoral é extrativismo...', 'animal', ['vegetal', 'mineral', 'industrial']),
    ('Extração de minério de ferro em jazidas para a produção de aço é extrativismo...', 'mineral',
     ['vegetal', 'animal', 'industrial']),
    ('Apanhar frutos nativos diretamente da mata é extrativismo...', 'vegetal', ['animal', 'mineral', 'industrial']),
    ('Retirada de areia e pedras do leito dos rios para a construção civil é extrativismo...', 'mineral',
     ['animal', 'vegetal', 'industrial']),
]
for enunciado, resposta, erradas in questoes:
    criar_questao(geografia, enunciado, resposta, erradas)

total = BancoQuestao.objects.filter(disciplina=geografia, modulo=MODULO).count()
print(f"\n🎉 Pronto! O card 'GEO - Prova 3º Período' tem {total} questões.")
