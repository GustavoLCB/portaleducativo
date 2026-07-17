"""
popular_historia.py
----------------------
Execute na raiz do projeto:
    python popular_historia.py

Popula o banco com questões de História em 5 módulos:
  - primeiras_vilas (São Vicente, São Paulo de Piratininga, Olinda)
  - ciclo_do_ouro (mineração, tropeiros, escravizados)
  - capitais_brasil (Salvador, Rio de Janeiro, Brasília)
  - crescimento_cidades (industrialização, cortiços, transportes)
  - cidadania (direitos, deveres, Constituição, município)

Baseado no material real de História do 3º ano (Colégio Santo Agostinho).
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


print("\n🏛️  Criando disciplina História...")
historia, _ = Disciplina.objects.get_or_create(
    nome='historia', defaults={'nome_exibicao': 'História'}
)
print("  ✅ História pronta.")


# ══════════════════════════════════════════════════════════════════
# MÓDULO 1 — PRIMEIRAS VILAS DO BRASIL
# ══════════════════════════════════════════════════════════════════
print("\n🏘️  Populando: História › Primeiras Vilas do Brasil...")

primeiras_vilas = [
    ('Qual foi a primeira vila fundada no Brasil?', 'São Vicente', ['São Vicente', 'Olinda', 'São Paulo de Piratininga', 'Salvador']),
    ('Em que ano foi fundada a Vila de São Vicente?', '1532', ['1532', '1535', '1554', '1549']),
    ('Quem fundou a Vila de São Vicente?', 'Martim Afonso de Sousa', ['Martim Afonso de Sousa', 'Tomé de Sousa', 'Padres jesuítas', 'Pedro Álvares Cabral']),
    ('A Vila de São Vicente ficava localizada em qual região?', 'Litoral de São Paulo', ['Litoral de São Paulo', 'Nordeste', 'Interior de Minas Gerais', 'Litoral da Bahia']),
    ('Qual era a principal atividade econômica de São Vicente?', 'Cultivo de cana-de-açúcar', ['Cultivo de cana-de-açúcar', 'Mineração de ouro', 'Extração de pau-brasil apenas', 'Pecuária']),
    ('Quem fundou a Vila de São Paulo de Piratininga?', 'Padres jesuítas', ['Padres jesuítas', 'Martim Afonso de Sousa', 'O governo português diretamente', 'Tropeiros']),
    ('Por que a Vila de São Paulo de Piratininga foi construída no alto de um morro?', 'Para facilitar a defesa', ['Para facilitar a defesa', 'Para ficar perto do mar', 'Por causa do clima frio', 'Para ficar perto das minas']),
    ('Em que ano foi fundada a Vila de Olinda?', '1535', ['1535', '1532', '1554', '1549']),
    ('Olinda fica em qual região do Brasil?', 'Nordeste', ['Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']),
    ('Qual era a principal atividade econômica de Olinda?', 'Cana-de-açúcar', ['Cana-de-açúcar', 'Mineração', 'Café', 'Pecuária']),
    ('Em que ano Olinda foi reconhecida como Patrimônio Cultural da Humanidade pela UNESCO?', '1982', ['1982', '1935', '1954', '2000']),
    ('Colocando em ordem de fundação, qual foi a SEGUNDA vila fundada no Brasil?', 'Olinda', ['Olinda', 'São Vicente', 'São Paulo de Piratininga', 'Salvador']),
    ('Antes da chegada dos portugueses, quem vivia no território que hoje é o Brasil?', 'Povos indígenas', ['Povos indígenas', 'Colonizadores espanhóis', 'Ninguém vivia aqui', 'Apenas comerciantes europeus']),
    ('Qual foi uma das primeiras riquezas exploradas pelos portugueses no Brasil?', 'Pau-brasil', ['Pau-brasil', 'Petróleo', 'Café', 'Ferro']),
    ('Qual país colonizou o Brasil?', 'Portugal', ['Portugal', 'Espanha', 'França', 'Holanda']),
]
for enunciado, resposta, opcoes in primeiras_vilas:
    criar_questao(historia, 'primeiras_vilas', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 2 — CICLO DO OURO
# ══════════════════════════════════════════════════════════════════
print("\n⛏️  Populando: História › Ciclo do Ouro...")

ciclo_do_ouro = [
    ('Por volta de que ano a região de Minas Gerais cresceu muito por causa do ouro?', '1700', ['1700', '1500', '1900', '1822']),
    ('Quem realizava, normalmente, o trabalho de extração do ouro nas minas?', 'Pessoas escravizadas', ['Pessoas escravizadas', 'Os tropeiros', 'Os proprietários das minas', 'Os bandeirantes']),
    ('Por que havia pouca produção de alimentos na região das minas?', 'Porque a mineração era mais lucrativa', ['Porque a mineração era mais lucrativa', 'Porque não havia terra fértil', 'Porque ninguém sabia plantar', 'Porque era proibido plantar']),
    ('Quem eram os responsáveis por levar alimentos e mercadorias até a região mineradora?', 'Os tropeiros', ['Os tropeiros', 'Os jesuítas', 'Os candangos', 'Os vereadores']),
    ('Como os tropeiros normalmente transportavam as mercadorias?', 'Em lombo de animais, como mulas e cavalos', ['Em lombo de animais, como mulas e cavalos', 'De trem', 'De navio', 'De caminhão']),
    ('Depois que o ouro se esgotou, o que essas cidades da região mineradora se tornaram?', 'Cidades históricas e turísticas', ['Cidades históricas e turísticas', 'Cidades abandonadas', 'Cidades industriais', 'Portos importantes']),
    ('Depois de descoberta, a mineração tornou-se:', 'A atividade econômica mais importante do Brasil na época', ['A atividade econômica mais importante do Brasil na época', 'Uma atividade proibida', 'Menos importante que a pecuária', 'Uma atividade só de lazer']),
    ('Antes da mineração, qual atividade já era importante no litoral do Brasil?', 'O cultivo de cana-de-açúcar', ['O cultivo de cana-de-açúcar', 'A extração de petróleo', 'A pecuária extensiva', 'O cultivo de café']),
    ('As estradas percorridas pelos tropeiros eram geralmente:', 'Difíceis e precárias', ['Difíceis e precárias', 'Pavimentadas e largas', 'Feitas de concreto', 'Iluminadas à noite']),
    ('O ouro encontrado em Minas Gerais atraiu:', 'Pessoas de diferentes lugares do Brasil e de Portugal', ['Pessoas de diferentes lugares do Brasil e de Portugal', 'Apenas pessoas da própria região', 'Apenas portugueses da nobreza', 'Ninguém, pois era um segredo']),
    ('A cana-de-açúcar foi a ÚNICA atividade responsável pela formação de vilas no Brasil?', 'Não, a mineração também formou vilas', ['Não, a mineração também formou vilas', 'Sim, só a cana-de-açúcar formou vilas', 'Não, só a pecuária formou vilas', 'Sim, junto com a pesca']),
    ('As cidades que enriqueceram com o ouro tinham construções como:', 'Casarões, igrejas e prédios públicos', ['Casarões, igrejas e prédios públicos', 'Apenas cabanas simples', 'Só estradas de terra', 'Apenas fábricas']),
    ('Os locais onde os tropeiros paravam para descansar durante as viagens, muitas vezes:', 'Deram origem a povoados e vilas', ['Deram origem a povoados e vilas', 'Foram destruídos depois', 'Viraram desertos', 'Nunca mais foram usados']),
    ('O que os tropeiros comercializavam principalmente?', 'Alimentos e outros produtos essenciais', ['Alimentos e outros produtos essenciais', 'Apenas joias', 'Apenas roupas de luxo', 'Apenas livros']),
    ('A principal atividade econômica na região das minas era:', 'A mineração', ['A mineração', 'A pecuária', 'A pesca', 'O turismo']),
]
for enunciado, resposta, opcoes in ciclo_do_ouro:
    criar_questao(historia, 'ciclo_do_ouro', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 3 — CAPITAIS DO BRASIL
# ══════════════════════════════════════════════════════════════════
print("\n🏙️  Populando: História › Capitais do Brasil...")

capitais_brasil = [
    ('Qual foi a primeira capital do Brasil?', 'Salvador', ['Salvador', 'Rio de Janeiro', 'Brasília', 'São Paulo']),
    ('Quem fundou Salvador como primeira capital do Brasil?', 'Tomé de Sousa', ['Tomé de Sousa', 'Martim Afonso de Sousa', 'Oscar Niemeyer', 'Dom Pedro I']),
    ('Por que Salvador foi escolhida como a primeira capital?', 'Por sua localização perto das plantações de cana-de-açúcar', ['Por sua localização perto das plantações de cana-de-açúcar', 'Por ser a maior cidade da época', 'Por ter ouro nas proximidades', 'Por ser no interior do país']),
    ('Qual foi a segunda capital do Brasil?', 'Rio de Janeiro', ['Rio de Janeiro', 'Salvador', 'Brasília', 'Recife']),
    ('Por que a capital foi transferida de Salvador para o Rio de Janeiro?', 'Por estar mais perto da região das minas de ouro', ['Por estar mais perto da região das minas de ouro', 'Por ter praias mais bonitas', 'Por ordem do rei da Espanha', 'Por ser mais fria']),
    ('Em 1808, quem chegou ao Rio de Janeiro, vindo de Portugal?', 'A família real portuguesa', ['A família real portuguesa', 'Os primeiros jesuítas', 'Os primeiros escravizados', 'Os primeiros tropeiros']),
    ('Qual é a capital atual do Brasil?', 'Brasília', ['Brasília', 'Rio de Janeiro', 'Salvador', 'São Paulo']),
    ('Quem planejou a cidade de Brasília?', 'Oscar Niemeyer e Lúcio Costa', ['Oscar Niemeyer e Lúcio Costa', 'Tomé de Sousa', 'Martim Afonso de Sousa', 'Dom João VI']),
    ('Por que Brasília foi construída no interior do país?', 'Para integrar melhor o território brasileiro', ['Para integrar melhor o território brasileiro', 'Porque não havia mais espaço no litoral', 'Por causa do clima', 'Para ficar perto do mar']),
    ('Como eram chamados os trabalhadores que construíram Brasília?', 'Candangos', ['Candangos', 'Tropeiros', 'Jesuítas', 'Bandeirantes']),
    ('As condições de trabalho dos candangos, que construíram Brasília, eram:', 'Inadequadas, com muitas horas de trabalho', ['Inadequadas, com muitas horas de trabalho', 'Muito confortáveis', 'Iguais às de hoje em dia', 'Sem nenhum risco']),
    ('O que é uma "cidade planejada"?', 'Uma cidade projetada e organizada antes de ser construída', ['Uma cidade projetada e organizada antes de ser construída', 'Uma cidade que cresceu sem nenhum planejamento', 'Uma cidade muito antiga', 'Uma cidade só de casas de campo']),
    ('Coloque em ordem cronológica as capitais do Brasil, da mais antiga para a mais recente:', 'Salvador, Rio de Janeiro, Brasília', ['Salvador, Rio de Janeiro, Brasília', 'Brasília, Rio de Janeiro, Salvador', 'Rio de Janeiro, Salvador, Brasília', 'Salvador, Brasília, Rio de Janeiro']),
    ('Salvador e Rio de Janeiro, as duas primeiras capitais, estão localizadas:', 'No litoral', ['No litoral', 'No interior do país', 'Na fronteira com outros países', 'Na região Sul']),
    ('Brasília foi inaugurada como capital em qual década?', '1960', ['1960', '1900', '1988', '1822']),
]
for enunciado, resposta, opcoes in capitais_brasil:
    criar_questao(historia, 'capitais_brasil', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 4 — CRESCIMENTO DAS CIDADES (INDUSTRIALIZAÇÃO)
# ══════════════════════════════════════════════════════════════════
print("\n🏭 Populando: História › Crescimento das Cidades...")

crescimento_cidades = [
    ('Quem investiu dinheiro na criação das primeiras indústrias brasileiras?', 'Os fazendeiros de café', ['Os fazendeiros de café', 'Os tropeiros', 'Os jesuítas', 'O governo português']),
    ('Qual atividade econômica gerou o dinheiro usado para investir nas primeiras indústrias?', 'A produção e venda de café', ['A produção e venda de café', 'A mineração de ouro', 'A pesca', 'O turismo']),
    ('Quais foram as duas principais cidades que mais cresceram com a industrialização?', 'São Paulo e Rio de Janeiro', ['São Paulo e Rio de Janeiro', 'Salvador e Recife', 'Belém e Manaus', 'Fortaleza e Natal']),
    ('O que são cortiços?', 'Moradias simples e apertadas, com pouca estrutura', ['Moradias simples e apertadas, com pouca estrutura', 'Casas grandes com piscina', 'Apartamentos de luxo', 'Hotéis para turistas']),
    ('O que eram as vilas operárias?', 'Moradias construídas pelas empresas perto das fábricas', ['Moradias construídas pelas empresas perto das fábricas', 'Casas de fazendeiros ricos', 'Palácios do governo', 'Escolas públicas']),
    ('Coloque em ordem, do mais antigo para o mais novo: bonde puxado por cavalos, bonde elétrico, ônibus e metrô.', 'Bonde puxado por cavalos, bonde elétrico, ônibus, metrô', ['Bonde puxado por cavalos, bonde elétrico, ônibus, metrô', 'Metrô, ônibus, bonde elétrico, bonde puxado por cavalos', 'Ônibus, metrô, bonde elétrico, bonde puxado por cavalos', 'Bonde elétrico, bonde puxado por cavalos, metrô, ônibus']),
    ('Como era feito o comércio nas cidades antigas?', 'Por vendedores ambulantes nas ruas', ['Por vendedores ambulantes nas ruas', 'Em grandes shoppings', 'Pela internet', 'Apenas em supermercados']),
    ('Como eram chamados os escravizados que trabalhavam nas ruas, vendendo produtos e prestando serviços, e entregavam o dinheiro a seus donos?', 'Escravizados de ganho', ['Escravizados de ganho', 'Escravizados de corte', 'Escravizados domésticos', 'Candangos']),
    ('Por que muitas pessoas saíram do campo para morar nas cidades a partir de 1950?', 'Em busca de trabalho e melhores condições de vida', ['Em busca de trabalho e melhores condições de vida', 'Por causa do frio no campo', 'Porque foram expulsas pelo governo', 'Para fugir de animais selvagens']),
    ('Um problema comum quando muitas pessoas chegam rapidamente às cidades é:', 'Falta de moradia', ['Falta de moradia', 'Excesso de empregos', 'Falta de pessoas', 'Redução do trânsito']),
    ('Qual documento, criado em 1988, reúne os direitos e deveres dos brasileiros?', 'A Constituição Federal', ['A Constituição Federal', 'O Código de Trânsito', 'O Estatuto da Cidade', 'A Carta Régia']),
    ('A falta de moradia se tornou um problema nas cidades durante o crescimento das indústrias?', 'Sim, foi um problema real', ['Sim, foi um problema real', 'Não, havia moradia de sobra', 'Não, esse problema só existe hoje', 'Sim, mas só no campo']),
    ('Qual das opções NÃO é uma mudança causada pelo crescimento das cidades?', 'Diminuição dos moradores das cidades', ['Diminuição dos moradores das cidades', 'Construção de fábricas', 'Crescimento do comércio', 'Surgimento de novos meios de transporte']),
    ('Hoje em dia, qual é um dos meios de transporte coletivo mais utilizados nas cidades?', 'Ônibus', ['Ônibus', 'Bonde puxado por cavalos', 'Carroça', 'Navio a vapor']),
    ('As primeiras fábricas do Brasil produziam principalmente:', 'Roupas e tecidos', ['Roupas e tecidos', 'Computadores', 'Automóveis', 'Aviões']),
]
for enunciado, resposta, opcoes in crescimento_cidades:
    criar_questao(historia, 'crescimento_cidades', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 5 — CIDADANIA: DIREITOS E DEVERES
# ══════════════════════════════════════════════════════════════════
print("\n⚖️  Populando: História › Cidadania...")

cidadania = [
    ('O que é cidadania?', 'Fazer parte de uma sociedade, respeitando as regras e as outras pessoas', ['Fazer parte de uma sociedade, respeitando as regras e as outras pessoas', 'Ter muito dinheiro', 'Morar em uma cidade grande', 'Ser dono de uma empresa']),
    ('Qual documento reúne os direitos e deveres de todos os brasileiros?', 'A Constituição Federal', ['A Constituição Federal', 'O Regimento Escolar', 'O Código Civil apenas', 'A Carta de Direitos dos EUA']),
    ('Em que ano foi criada a Constituição Federal do Brasil atual?', '1988', ['1988', '1822', '1500', '1960']),
    ('Qual das opções abaixo é um DIREITO garantido pela Constituição?', 'Educação', ['Educação', 'Jogar lixo na rua', 'Desrespeitar os outros', 'Ignorar as leis']),
    ('Qual das opções abaixo é um DEVER do cidadão?', 'Respeitar as leis e o meio ambiente', ['Respeitar as leis e o meio ambiente', 'Ganhar presentes', 'Assistir televisão', 'Dormir tarde']),
    ('Quem faz as leis do município?', 'A Câmara Municipal (vereadores)', ['A Câmara Municipal (vereadores)', 'A Prefeitura sozinha', 'O Governo Federal', 'A escola']),
    ('Quem administra o município, no dia a dia?', 'O prefeito, através da Prefeitura', ['O prefeito, através da Prefeitura', 'Os vereadores sozinhos', 'O presidente do Brasil', 'Os professores']),
    ('A área urbana de um município também é chamada de:', 'Cidade', ['Cidade', 'Campo', 'Estado', 'País']),
    ('A área rural de um município também é chamada de:', 'Campo', ['Campo', 'Cidade', 'Bairro', 'Distrito']),
    ('Somente a área urbana deve ser atendida pelo governo municipal?', 'Não, a área rural também deve ser atendida', ['Não, a área rural também deve ser atendida', 'Sim, só a área urbana importa', 'Sim, o campo se vira sozinho', 'Não existe diferença entre as áreas']),
    ('Uma criança pode praticar a cidadania no dia a dia ao:', 'Respeitar os colegas e cuidar da escola', ['Respeitar os colegas e cuidar da escola', 'Jogar lixo no chão', 'Gritar com as pessoas', 'Ignorar as regras']),
    ('Cite uma solução para os problemas urbanos de moradia:', 'Construção de moradias populares', ['Construção de moradias populares', 'Ignorar o problema', 'Aumentar o preço dos imóveis', 'Proibir a construção de casas']),
    ('Cite uma solução para os problemas urbanos de transporte:', 'Melhoria do transporte público e criação de ciclovias', ['Melhoria do transporte público e criação de ciclovias', 'Fechar todas as ruas', 'Proibir ônibus', 'Aumentar o preço das passagens']),
    ('Os cidadãos podem colaborar com a comunidade por meio de:', 'Associações de moradores, ONGs e trabalho voluntário', ['Associações de moradores, ONGs e trabalho voluntário', 'Reclamações sem nenhuma ação', 'Brigas com vizinhos', 'Isolamento total']),
    ('Cada município no Brasil faz parte de um dos 26 estados, com exceção de qual unidade federativa?', 'Distrito Federal', ['Distrito Federal', 'Rio de Janeiro', 'São Paulo', 'Minas Gerais']),
]
for enunciado, resposta, opcoes in cidadania:
    criar_questao(historia, 'cidadania', enunciado, resposta, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE HISTÓRIA CONCLUÍDA!")
print("=" * 55)
for modulo, nome in [
    ('primeiras_vilas', 'Primeiras Vilas do Brasil'),
    ('ciclo_do_ouro', 'Ciclo do Ouro'),
    ('capitais_brasil', 'Capitais do Brasil'),
    ('crescimento_cidades', 'Crescimento das Cidades'),
    ('cidadania', 'Cidadania'),
]:
    total = BancoQuestao.objects.filter(disciplina=historia, modulo=modulo).count()
    print(f"   {nome:.<32} {total}")
