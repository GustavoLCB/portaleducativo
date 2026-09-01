"""
Popula o banco de questões do módulo 'Prepositions of Place' (Inglês).

Conteúdo baseado no material da Unit 4 do livro didático (Language
Activity Book / Student Book) usado em sala: preposições de lugar
(above, behind, between, in front of, next to, under) e vocabulário de
cômodos/móveis da casa que aparece nas mesmas atividades (fireplace,
bookcase, shower, tub, armchair, stairs, refrigerator, microwave,
stove, sofa, rug, shelves).

Como rodar (dentro do ambiente virtual, na pasta do projeto):
    python manage.py shell < popular_ingles_prepositions_of_place.py

Usa update_or_create (e não get_or_create) de propósito: se este
script for executado de novo depois de uma correção de texto em
'enunciado', ele ATUALIZA o registro existente em vez de silenciosamente
ignorá-lo. A chave de identidade de cada questão é
(disciplina, modulo, enunciado) — se um dia o texto do enunciado for
alterado, o registro antigo vira um "registro fantasma" e precisa ser
limpo com um script de limpeza (padrão EXECUTAR_DELETE), como já
fizemos em outros módulos.
"""

from core.models import Disciplina, BancoQuestao

DISCIPLINA_NOME = 'ingles'
MODULO = 'prepositions_of_place'

disciplina, _ = Disciplina.objects.get_or_create(nome=DISCIPLINA_NOME)

# Cada item: (enunciado, resposta_correta, [demais opções erradas])
QUESTOES = [
    # ── Bloco 1: preposições de lugar ────────────────────────────────
    ("The lamp is _____ the two armchairs.", "between",
     ["behind", "under", "above"]),
    ("The bookcase is _____ the armchair — you can't see it.", "behind",
     ["in front of", "between", "under"]),
    ("The picture is _____ the fireplace, on the wall.", "above",
     ["under", "next to", "between"]),
    ("The table is _____ the sofa, facing it.", "in front of",
     ["behind", "above", "next to"]),
    ("The rug is _____ the coffee table.", "under",
     ["above", "behind", "next to"]),
    ("The vase is _____ the bookcase, right beside it.", "next to",
     ["under", "between", "in front of"]),
    ("The microwave is _____ the stove and the fridge.", "between",
     ["above", "behind", "under"]),
    ("The cat is _____ the table, hiding from view.", "behind",
     ["in front of", "next to", "above"]),
    ("The shelves are _____ the tub, on the wall beside it.", "next to",
     ["under", "behind", "between"]),
    ("The clock is _____ the door, high on the wall.", "above",
     ["under", "in front of", "next to"]),
    ("The dog is sleeping _____ the bed.", "under",
     ["above", "behind", "next to"]),
    ("The chair is _____ the desk, so you can sit and study.", "in front of",
     ["behind", "above", "between"]),

    # ── Bloco 2: vocabulário da casa (Unit 4) ────────────────────────
    ("What do we call the place in the living room where you light a fire?",
     "fireplace", ["stove", "shower", "microwave"]),
    ("What furniture do we use to store books?",
     "bookcase", ["shelves", "stairs", "sofa"]),
    ("Where do you stand to take a shower?",
     "shower", ["tub", "sink", "stove"]),
    ("What do we call a comfortable chair for one person?",
     "armchair", ["sofa", "bookcase", "stairs"]),
    ("What connects the ground floor to the upper floor of a house?",
     "stairs", ["shelves", "rug", "fireplace"]),
    ("What appliance do we use to keep food cold?",
     "refrigerator", ["microwave", "stove", "tub"]),
    ("What kitchen appliance do we use to heat food quickly?",
     "microwave", ["stove", "refrigerator", "shower"]),
    ("What do we call the soft carpet piece on the floor?",
     "rug", ["shelves", "tub", "armchair"]),
]

criadas = 0
atualizadas = 0

for enunciado, resposta_correta, opcoes_erradas in QUESTOES:
    opcoes = opcoes_erradas + [resposta_correta]
    _, criado = BancoQuestao.objects.update_or_create(
        disciplina=disciplina,
        modulo=MODULO,
        enunciado=enunciado,
        defaults={
            'resposta_correta': resposta_correta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        },
    )
    if criado:
        criadas += 1
    else:
        atualizadas += 1

print(f"Módulo '{MODULO}' ({DISCIPLINA_NOME}): "
      f"{criadas} questão(ões) criada(s), {atualizadas} atualizada(s). "
      f"Total no módulo: {BancoQuestao.objects.filter(disciplina=disciplina, modulo=MODULO).count()}.")
