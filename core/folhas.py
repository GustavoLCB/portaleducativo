"""Catálogo das FOLHAS de trabalho (PDF) de cada matéria.

Para incluir uma folha nova:
  1. copie o PDF para  core/folhas_pdf/<materia>/  ;
  2. acrescente um dicionário na lista da matéria abaixo.
O 'numero' é o número de ordem que aparece no canto superior direito da folha
(as folhas são mostradas em ordem crescente desse número).
"""

MATERIAS_FOLHAS = {
    'matematica': {'nome': 'Matemática', 'icone': '🧮', 'menu': 'menu_matematica',
                   'cor': '#026873', 'caixa': 'rgba(1, 45, 50, 0.6)', 'texto': '#1c2b22',
                   'imagem': 'img/imagemfundo1.png'},
    'portugues':  {'nome': 'Português', 'icone': '📚', 'menu': 'menu_portugues',
                   'cor': '#4a1942', 'caixa': 'rgba(40, 14, 36, 0.6)', 'texto': '#2c1e28',
                   'imagem': 'img/fundoport.png'},
    'ingles':     {'nome': 'Inglês', 'icone': '🇺🇸', 'menu': 'menu_ingles',
                   'cor': '#0d3b66', 'caixa': 'rgba(6, 30, 54, 0.6)', 'texto': '#0d2035',
                   'imagem': 'img/fundoing.png'},
    'ciencias':   {'nome': 'Ciências', 'icone': '🔬', 'menu': 'menu_ciencias',
                   'cor': '#1b4d3e', 'caixa': 'rgba(10, 40, 32, 0.6)', 'texto': '#1c2b24',
                   'imagem': 'img/fundocien.png'},
    'geografia':  {'nome': 'Geografia', 'icone': '🌎', 'menu': 'menu_geografia',
                   'cor': '#1b5e20', 'caixa': 'rgba(10, 50, 15, 0.6)', 'texto': '#1c2b1c',
                   'imagem': 'img/fundogeo.png'},
    'historia':   {'nome': 'História', 'icone': '🏛️', 'menu': 'menu_historia',
                   'cor': '#5c3a21', 'caixa': 'rgba(40, 25, 14, 0.6)', 'texto': '#2b1c10',
                   'imagem': 'img/fundohist.png'},
}

FOLHAS = {
    'matematica': [
        {'numero': 73, 'titulo': 'Problemas e figuras geométricas', 'data': '23/09/2026',
         'paginas': 3, 'arquivo': 'matematica-folha-73-problemas-divisao-subtracao.pdf'},
        {'numero': 76, 'titulo': 'Vamos treinar a tabuada (trilha)', 'data': '29/09/2026',
         'paginas': 1, 'arquivo': 'matematica-folha-76-trilha-da-tabuada.pdf'},
    ],
    'portugues': [],
    'ingles': [
        {'numero': 33, 'titulo': 'Unit 6 – Feelings (páginas 96 e 97)', 'data': '21/09/2026',
         'paginas': 2, 'arquivo': 'ingles-folha-33-unit6-feelings.pdf'},
        {'numero': 34, 'titulo': 'Unit 6 – Grammar 1', 'data': '23/09/2026',
         'paginas': 2, 'arquivo': 'ingles-folha-34-unit6-grammar1.pdf'},
        {'numero': 36, 'titulo': 'Review for the test – 4th term', 'data': '30/09/2026',
         'paginas': 4, 'arquivo': 'ingles-folha-36-review-4th-term.pdf'},
    ],
    'ciencias': [],
    'geografia': [],
    'historia': [],
}
