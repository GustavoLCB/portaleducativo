"""
popular_geografia.py
----------------------
Execute na raiz do projeto:
    python popular_geografia.py

Popula o banco com questões de Geografia em 5 módulos:
  - extrativismo (vegetal, mineral, animal)
  - regioes_brasil (as 5 regiões e os estados)
  - agricultura (familiar, comercial, monocultura)
  - pecuaria (extensiva, intensiva, tipos de rebanho)
  - paisagem (pontos de vista, planos, natural x humanizada)

Baseado no material real de Geografia do 3º ano (Colégio Santo Agostinho).
Pode rodar de novo sem problema — não duplica questões existentes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Disciplina, BancoQuestao


def criar_questao(disciplina, modulo, enunciado, resposta, opcoes):
    obj, criado = BancoQuestao.objects.get_or_create(
        disciplina=disciplina, modulo=modulo, enunciado=enunciado,
        defaults={
            'tipo': 'multipla_escolha',
            'resposta_correta': resposta,
            'dados_extras': {'opcoes': opcoes},
            'ativo': True,
        }
    )
    status = "✅" if criado else "⏭️ "
    print(f"  {status} {enunciado[:65]}")


print("\n🌎 Criando disciplina Geografia...")
geografia, _ = Disciplina.objects.get_or_create(
    nome='geografia', defaults={'nome_exibicao': 'Geografia'}
)
print("  ✅ Geografia pronta.")


# ══════════════════════════════════════════════════════════════════
# MÓDULO 1 — EXTRATIVISMO
# ══════════════════════════════════════════════════════════════════
print("\n🌳 Populando: Geografia › Extrativismo...")

extrativismo = [
    ('Extrativismo é a atividade de retirar recursos de onde?', 'Do meio ambiente',
     ['Do meio ambiente', 'Da fábrica', 'Do supermercado', 'Da cidade']),
    ('Qual foi a primeira atividade econômica realizada no Brasil?', 'Extrativismo do pau-brasil',
     ['Extrativismo do pau-brasil', 'Agricultura de café', 'Pecuária de gado', 'Mineração de ouro']),
    ('O pau-brasil era usado principalmente para:', 'Tingir tecidos',
     ['Tingir tecidos', 'Fazer papel', 'Construir casas', 'Fazer remédios']),
    ('O extrativismo vegetal consiste na retirada de recursos de origem:', 'Vegetal',
     ['Vegetal', 'Mineral', 'Animal', 'Industrial']),
    ('O látex, usado para fabricar borracha, é extraído de qual planta?', 'Seringueira',
     ['Seringueira', 'Pau-brasil', 'Castanheira', 'Açaizeiro']),
    ('O extrativismo mineral consiste na exploração de recursos:', 'Do subsolo',
     ['Do subsolo', 'Das águas do mar', 'Das plantações', 'Das florestas']),
    ('Qual das opções abaixo é um exemplo de extrativismo MINERAL?', 'Ouro',
     ['Ouro', 'Castanha', 'Açaí', 'Látex']),
    ('Qual das opções abaixo é um exemplo de extrativismo VEGETAL?', 'Açaí',
     ['Açaí', 'Ouro', 'Petróleo', 'Bauxita']),
    ('O extrativismo animal inclui atividades como:', 'Caça e pesca',
     ['Caça e pesca', 'Plantio e colheita', 'Mineração e perfuração', 'Criação de gado']),
    ('No Brasil, a caça de animais é:', 'Ilegal, exceto para comunidades indígenas',
     ['Ilegal, exceto para comunidades indígenas', 'Totalmente proibida sempre', 'Permitida para todos', 'Uma atividade comercial livre']),
    ('Em qual região do Brasil o extrativismo vegetal (madeira, açaí, látex) é mais comum?', 'Região Norte',
     ['Região Norte', 'Região Sul', 'Região Sudeste', 'Região Nordeste']),
    ('Um problema socioambiental que o extrativismo mal feito pode causar é:', 'Redução da biodiversidade',
     ['Redução da biodiversidade', 'Aumento de empregos', 'Mais chuva', 'Mais turismo']),
    ('Biodiversidade significa:', 'Conjunto de espécies e seres vivos de uma região',
     ['Conjunto de espécies e seres vivos de uma região', 'Tipo de solo fértil', 'Quantidade de água doce', 'Nome de uma planta']),
    ('O ferro e o petróleo são exemplos de extrativismo:', 'Mineral', ['Mineral', 'Vegetal', 'Animal', 'Industrial']),
    ('A castanha e o açaí são exemplos de extrativismo:', 'Vegetal', ['Vegetal', 'Mineral', 'Animal', 'Industrial']),
]
for enunciado, resposta, opcoes in extrativismo:
    criar_questao(geografia, 'extrativismo', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 2 — REGIÕES DO BRASIL
# ══════════════════════════════════════════════════════════════════
print("\n🗺️  Populando: Geografia › Regiões do Brasil...")

regioes_brasil = [
    ('Quantas regiões o Brasil possui?', '5', ['5', '4', '6', '3']),
    ('Quantos estados + Distrito Federal formam o Brasil (unidades federativas)?', '27', ['27', '26', '25', '28']),
    ('O Rio de Janeiro pertence a qual região?', 'Sudeste', ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste']),
    ('São Paulo pertence a qual região?', 'Sudeste', ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste']),
    ('A Bahia pertence a qual região?', 'Nordeste', ['Nordeste', 'Norte', 'Sudeste', 'Sul']),
    ('O Amazonas pertence a qual região?', 'Norte', ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste']),
    ('O Mato Grosso pertence a qual região?', 'Centro-Oeste', ['Centro-Oeste', 'Norte', 'Sudeste', 'Sul']),
    ('O Rio Grande do Sul pertence a qual região?', 'Sul', ['Sul', 'Sudeste', 'Nordeste', 'Norte']),
    ('Quais são as 5 regiões do Brasil?', 'Norte, Nordeste, Centro-Oeste, Sudeste e Sul',
     ['Norte, Nordeste, Centro-Oeste, Sudeste e Sul', 'Norte, Sul, Leste, Oeste e Centro',
      'Amazônia, Pantanal, Cerrado, Caatinga e Mata Atlântica', 'Norte, Nordeste, Sudeste, Sul e Litoral']),
    ('A capital do Brasil, Brasília, fica em qual região?', 'Centro-Oeste', ['Centro-Oeste', 'Sudeste', 'Norte', 'Nordeste']),
    ('Minas Gerais pertence a qual região?', 'Sudeste', ['Sudeste', 'Sul', 'Nordeste', 'Norte']),
    ('Pernambuco pertence a qual região?', 'Nordeste', ['Nordeste', 'Norte', 'Sudeste', 'Sul']),
    ('Goiás pertence a qual região?', 'Centro-Oeste', ['Centro-Oeste', 'Norte', 'Sul', 'Sudeste']),
    ('O Paraná pertence a qual região?', 'Sul', ['Sul', 'Sudeste', 'Nordeste', 'Norte']),
    ('O Pará pertence a qual região?', 'Norte', ['Norte', 'Nordeste', 'Centro-Oeste', 'Sul']),
]
for enunciado, resposta, opcoes in regioes_brasil:
    criar_questao(geografia, 'regioes_brasil', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 3 — AGRICULTURA (familiar, comercial, monocultura)
# ══════════════════════════════════════════════════════════════════
print("\n🌾 Populando: Geografia › Agricultura...")

agricultura = [
    ('A agricultura familiar é praticada em:', 'Pequenas propriedades rurais',
     ['Pequenas propriedades rurais', 'Grandes propriedades comerciais', 'Fábricas', 'Áreas urbanas']),
    ('Cerca de quantos % dos alimentos consumidos no Brasil vêm da agricultura familiar?', '70%',
     ['70%', '30%', '50%', '90%']),
    ('A agricultura familiar está presente em quase quantos % das propriedades rurais do Brasil?', '85%',
     ['85%', '50%', '30%', '60%']),
    ('Qual região concentra cerca de metade das propriedades de agricultura familiar do Brasil?', 'Nordeste',
     ['Nordeste', 'Sul', 'Sudeste', 'Norte']),
    ('A agricultura comercial é praticada em:', 'Grandes propriedades',
     ['Grandes propriedades', 'Pequenas propriedades', 'Quintais de casa', 'Hortas escolares']),
    ('A agricultura comercial é voltada principalmente para:', 'Exportação e mercado interno',
     ['Exportação e mercado interno', 'Consumo só da própria família', 'Doação para escolas', 'Consumo só de animais']),
    ('Qual das opções abaixo é um insumo agrícola?', 'Adubo', ['Adubo', 'Boi', 'Casa', 'Escola']),
    ('A soja é produzida principalmente em qual estado?', 'Mato Grosso', ['Mato Grosso', 'Rio de Janeiro', 'Bahia', 'Pará']),
    ('O café é produzido principalmente em qual estado?', 'Minas Gerais', ['Minas Gerais', 'Amazonas', 'Rio Grande do Sul', 'Ceará']),
    ('Monocultura é:', 'O cultivo de apenas um produto agrícola',
     ['O cultivo de apenas um produto agrícola', 'O cultivo de vários produtos ao mesmo tempo', 'A criação de animais', 'A pesca em rios']),
    ('A monocultura geralmente ocorre em:', 'Latifúndios (grandes propriedades)',
     ['Latifúndios (grandes propriedades)', 'Pequenos quintais', 'Hortas comunitárias', 'Jardins']),
    ('No período colonial, o Brasil dependeu muito da monocultura de:', 'Cana-de-açúcar',
     ['Cana-de-açúcar', 'Soja', 'Milho', 'Café']),
    ('Um risco de um país depender de monocultura é:', 'A economia ficar vulnerável a mudanças de preço',
     ['A economia ficar vulnerável a mudanças de preço', 'A produção nunca cair', 'O país nunca ter problemas', 'Os preços nunca mudarem']),
    ('A laranja é produzida principalmente em qual estado?', 'São Paulo', ['São Paulo', 'Amazonas', 'Bahia', 'Paraná']),
    ('O arroz é produzido principalmente em qual estado?', 'Rio Grande do Sul', ['Rio Grande do Sul', 'Minas Gerais', 'Ceará', 'Pará']),
]
for enunciado, resposta, opcoes in agricultura:
    criar_questao(geografia, 'agricultura', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 4 — PECUÁRIA
# ══════════════════════════════════════════════════════════════════
print("\n🐄 Populando: Geografia › Pecuária...")

pecuaria = [
    ('Pecuária é a atividade de:', 'Criação de animais', ['Criação de animais', 'Plantio de vegetais', 'Extração de minérios', 'Pesca no mar']),
    ('Bois e vacas fazem parte de qual tipo de rebanho?', 'Bovino', ['Bovino', 'Suíno', 'Ovino', 'Equino']),
    ('Porcos fazem parte de qual tipo de rebanho?', 'Suíno', ['Suíno', 'Bovino', 'Caprino', 'Bufalino']),
    ('Ovelhas e carneiros fazem parte de qual tipo de rebanho?', 'Ovino', ['Ovino', 'Caprino', 'Bovino', 'Equino']),
    ('Cabras e bodes fazem parte de qual tipo de rebanho?', 'Caprino', ['Caprino', 'Ovino', 'Suíno', 'Bufalino']),
    ('Cavalos fazem parte de qual tipo de rebanho?', 'Equino', ['Equino', 'Bovino', 'Ovino', 'Suíno']),
    ('Búfalos fazem parte de qual tipo de rebanho?', 'Bufalino', ['Bufalino', 'Bovino', 'Caprino', 'Equino']),
    ('Na pecuária EXTENSIVA, os animais:', 'Vivem soltos em grandes áreas de pasto natural',
     ['Vivem soltos em grandes áreas de pasto natural', 'Vivem confinados em pequenos espaços', 'Ficam em fábricas', 'Vivem em aquários']),
    ('Na pecuária INTENSIVA, os animais vivem:', 'Em espaços confinados, mais controlados',
     ['Em espaços confinados, mais controlados', 'Soltos em enormes fazendas', 'Nas ruas da cidade', 'Em florestas selvagens']),
    ('Na pecuária intensiva, os animais recebem:', 'Ração nutritiva e cuidados veterinários',
     ['Ração nutritiva e cuidados veterinários', 'Apenas água da chuva', 'Nenhum tipo de cuidado', 'Apenas capim natural']),
    ('Qual tipo de pecuária usa mais tecnologia?', 'Intensiva', ['Intensiva', 'Extensiva', 'As duas usam igual', 'Nenhuma usa tecnologia']),
    ('Qual tipo de pecuária tem ritmo mais lento de produção?', 'Extensiva', ['Extensiva', 'Intensiva', 'As duas são iguais', 'Nenhuma das duas']),
    ('O leite da pecuária é usado para fabricar, entre outras coisas:', 'Queijo e manteiga',
     ['Queijo e manteiga', 'Papel e vidro', 'Tecido e plástico', 'Tinta e cimento']),
    ('O couro da pecuária é usado para fabricar:', 'Sapatos e bolsas', ['Sapatos e bolsas', 'Queijo e iogurte', 'Papel e livros', 'Vidro e cerâmica']),
    ('A avicultura (criação de aves) fornece:', 'Carne, ovos e penas', ['Carne, ovos e penas', 'Leite e couro', 'Lã e mel', 'Madeira e látex']),
]
for enunciado, resposta, opcoes in pecuaria:
    criar_questao(geografia, 'pecuaria', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 5 — PAISAGEM (pontos de vista, planos, natural x humanizada)
# ══════════════════════════════════════════════════════════════════
print("\n🏞️  Populando: Geografia › Paisagem...")

paisagem = [
    ('Observar uma paisagem de cima, como se estivéssemos em um drone, é o ponto de vista:', 'Vertical',
     ['Vertical', 'Frontal', 'Oblíquo', 'Lateral']),
    ('Observar uma paisagem bem de frente é o ponto de vista:', 'Frontal', ['Frontal', 'Vertical', 'Oblíquo', 'Traseiro']),
    ('Observar uma paisagem de lado/diagonal é o ponto de vista:', 'Oblíquo', ['Oblíquo', 'Frontal', 'Vertical', 'Traseiro']),
    ('No PRIMEIRO plano de uma paisagem, os elementos estão:', 'Mais perto de quem observa',
     ['Mais perto de quem observa', 'Mais longe de quem observa', 'No céu', 'Debaixo da terra']),
    ('No TERCEIRO plano de uma paisagem, os elementos estão:', 'Mais longe de quem observa',
     ['Mais longe de quem observa', 'Mais perto de quem observa', 'Embaixo d\'água', 'Dentro de uma casa']),
    ('Uma paisagem sem nenhuma interferência humana é chamada de:', 'Paisagem natural',
     ['Paisagem natural', 'Paisagem humanizada', 'Paisagem urbana', 'Paisagem industrial']),
    ('Uma paisagem modificada pela ação do ser humano é chamada de:', 'Paisagem humanizada',
     ['Paisagem humanizada', 'Paisagem natural', 'Paisagem selvagem', 'Paisagem intocada']),
    ('O que pode modificar uma paisagem de forma NATURAL (sem ação humana)?', 'Vento, chuva e mar',
     ['Vento, chuva e mar', 'Construção de prédios', 'Construção de estradas', 'Plantação de lavouras']),
    ('A construção do calçadão de Copacabana transformou a paisagem por ação:', 'Das pessoas (ação humana)',
     ['Das pessoas (ação humana)', 'Da natureza', 'Do vento', 'Do mar']),
    ('Desmatar uma área sem plantar novas árvores é uma atitude:', 'Incorreta, prejudica o meio ambiente',
     ['Incorreta, prejudica o meio ambiente', 'Correta e recomendada', 'Sem nenhuma consequência', 'Obrigatória por lei']),
    ('Fechar a torneira enquanto escova os dentes ajuda a:', 'Economizar água', ['Economizar água', 'Gastar mais água', 'Sujar a pia', 'Esquentar a água']),
    ('A água que chega até as nossas casas deve ser:', 'Tratada', ['Tratada', 'Usada sem cuidado', 'Ignorada', 'Vendida sem controle']),
    ('Reflorestar significa:', 'Plantar novas árvores em um local', ['Plantar novas árvores em um local', 'Cortar todas as árvores', 'Construir uma fábrica', 'Fazer uma estrada']),
    ('Um recurso natural que "pode acabar" se usado sem cuidado é:', 'A madeira', ['A madeira', 'O ar', 'A luz do sol', 'O tempo']),
    ('O ciclo do dia e da noite é um exemplo de algo que:', 'Provoca mudanças na paisagem', ['Provoca mudanças na paisagem', 'Nunca muda nada', 'É feito pelo homem', 'Só acontece no inverno']),
]
for enunciado, resposta, opcoes in paisagem:
    criar_questao(geografia, 'paisagem', enunciado, resposta, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE GEOGRAFIA CONCLUÍDA!")
print("=" * 55)
for modulo, nome in [
    ('extrativismo', 'Extrativismo'),
    ('regioes_brasil', 'Regiões do Brasil'),
    ('agricultura', 'Agricultura'),
    ('pecuaria', 'Pecuária'),
    ('paisagem', 'Paisagem'),
]:
    total = BancoQuestao.objects.filter(disciplina=geografia, modulo=modulo).count()
    print(f"   {nome:.<32} {total}")
