"""
popular_ciencias.py
----------------------
Execute na raiz do projeto:
    python popular_ciencias.py

Popula o banco com questões de Ciências em 6 módulos:
  - plantas (partes, fotossíntese, dispersão de sementes, germinação)
  - sons (naturais x artificiais, poluição sonora, instrumentos)
  - solo (tipos, preparo, degradação e conservação)
  - petroleo (o que é, usos, riscos)
  - sistema_solar (rotação, translação, planetas)
  - diversidade_modos_vida (ambientes, alimentação, reprodução dos animais)

Baseado no material real de Ciências do 3º ano (Colégio Santo Agostinho).
Pode rodar de novo sem problema — não duplica questões existentes.
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
    print(f"  {status} {enunciado[:65]}")


print("\n🔬 Criando disciplina Ciências...")
ciencias, _ = Disciplina.objects.get_or_create(
    nome='ciencias', defaults={'nome_exibicao': 'Ciências'}
)
print("  ✅ Ciências pronta.")


# ══════════════════════════════════════════════════════════════════
# MÓDULO 1 — PLANTAS
# ══════════════════════════════════════════════════════════════════
print("\n🌱 Populando: Ciências › Plantas...")

plantas = [
    ('Qual parte da planta fixa a planta no solo e absorve água e nutrientes?', 'Raiz', ['Raiz', 'Caule', 'Folha', 'Flor']),
    ('Qual parte da planta é responsável por sustentar e transportar substâncias?', 'Caule', ['Caule', 'Raiz', 'Fruto', 'Semente']),
    ('Em qual parte da planta acontece principalmente a fotossíntese?', 'Folhas', ['Folhas', 'Raiz', 'Flor', 'Fruto']),
    ('Qual parte da planta participa da reprodução, atraindo polinizadores?', 'Flor', ['Flor', 'Raiz', 'Caule', 'Fruto']),
    ('Qual parte da planta protege a semente?', 'Fruto', ['Fruto', 'Raiz', 'Caule', 'Folha']),
    ('Qual parte da planta dá origem a uma nova planta?', 'Semente', ['Semente', 'Raiz', 'Caule', 'Flor']),
    ('Na fotossíntese, a planta usa a luz do sol, água e qual gás do ar para produzir alimento?', 'Gás carbônico',
     ['Gás carbônico', 'Gás oxigênio', 'Gás nitrogênio', 'Gás hidrogênio']),
    ('Durante a fotossíntese, a planta libera qual gás?', 'Gás oxigênio', ['Gás oxigênio', 'Gás carbônico', 'Gás nitrogênio', 'Vapor de água']),
    ('O que é a dispersão das sementes?', 'É quando as sementes são levadas da planta-mãe para outros locais',
     ['É quando as sementes são levadas da planta-mãe para outros locais', 'É quando a planta morre', 'É quando a raiz cresce', 'É quando a flor murcha']),
    ('Quais são as formas de dispersão de sementes citadas no material?', 'Vento, água e animais',
     ['Vento, água e animais', 'Somente pelo vento', 'Somente por máquinas', 'Somente pela chuva']),
    ('Os polinizadores são animais que:', 'Transportam o pólen de uma flor para outra',
     ['Transportam o pólen de uma flor para outra', 'Comem as raízes das plantas', 'Destroem as sementes', 'Impedem a germinação']),
    ('Para germinar, a semente precisa especialmente de:', 'Água e ar (oxigênio)',
     ['Água e ar (oxigênio)', 'Apenas luz do sol', 'Apenas terra seca', 'Apenas vento']),
    ('A anta é chamada de "jardineira da floresta" porque:', 'Come frutos e espalha as sementes pelas fezes',
     ['Come frutos e espalha as sementes pelas fezes', 'Planta sementes com as patas', 'Rega as plantas', 'Corta as árvores']),
    ('O carrapicho consegue se espalhar porque:', 'Tem espinhos que grudam no pelo dos animais e roupas',
     ['Tem espinhos que grudam no pelo dos animais e roupas', 'Voa sozinho pelo ar', 'Nada até outro lugar', 'Pula como um sapo']),
    ('Qual é a ordem correta: o que acontece primeiro na vida de uma planta?', 'Germinação da semente',
     ['Germinação da semente', 'Produção de frutos', 'Floração', 'Formação de novas sementes']),
    ('O corpo das plantas é formado principalmente por:', 'Raízes, caule e folhas',
     ['Raízes, caule e folhas', 'Apenas flores', 'Apenas frutos', 'Apenas sementes']),
    ('Todas as plantas têm exatamente o mesmo tamanho, formato e cor?', 'Não, elas são muito diferentes entre si',
     ['Não, elas são muito diferentes entre si', 'Sim, todas são iguais', 'Só a cor muda', 'Só o tamanho muda']),
    ('As plantas têm um ciclo de vida que inclui:', 'Nascer, crescer e se reproduzir',
     ['Nascer, crescer e se reproduzir', 'Apenas nascer', 'Apenas crescer', 'Nascer e morrer sem crescer']),
]
for enunciado, resposta, opcoes in plantas:
    criar_questao(ciencias, 'plantas', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 2 — SONS
# ══════════════════════════════════════════════════════════════════
print("\n🔊 Populando: Ciências › Sons...")

sons = [
    ('Sons produzidos pela natureza, como o vento e os pássaros, são chamados de:', 'Sons naturais',
     ['Sons naturais', 'Sons artificiais', 'Sons elétricos', 'Sons mecânicos']),
    ('O som de um carro ou de uma buzina é um exemplo de som:', 'Artificial (produzido pelo homem)',
     ['Artificial (produzido pelo homem)', 'Natural', 'Silencioso', 'Invisível']),
    ('A poluição sonora acontece quando há:', 'Excesso de barulho no ambiente',
     ['Excesso de barulho no ambiente', 'Falta de som', 'Muita luz', 'Muito vento']),
    ('Qual é o sentido responsável por perceber os sons?', 'Audição', ['Audição', 'Visão', 'Olfato', 'Paladar']),
    ('Qual órgão é responsável pela audição?', 'Orelha (ouvido)', ['Orelha (ouvido)', 'Olho', 'Nariz', 'Língua']),
    ('A exposição a ruídos elevados pode causar:', 'Estresse, dor de cabeça e perda de audição',
     ['Estresse, dor de cabeça e perda de audição', 'Melhora da visão', 'Mais energia', 'Nenhum efeito']),
    ('Quantos tipos principais de instrumentos musicais existem?', '3', ['3', '2', '5', '1']),
    ('Quais são os três tipos principais de instrumentos musicais?', 'Corda, sopro e percussão',
     ['Corda, sopro e percussão', 'Grave, agudo e médio', 'Alto, baixo e forte', 'Rápido, lento e pausado']),
    ('Um violão é um instrumento de:', 'Corda', ['Corda', 'Sopro', 'Percussão', 'Vento']),
    ('Um tambor é um instrumento de:', 'Percussão', ['Percussão', 'Corda', 'Sopro', 'Vento']),
    ('Uma flauta é um instrumento de:', 'Sopro', ['Sopro', 'Corda', 'Percussão', 'Vidro']),
    ('Um instrumento musical produz som quando:', 'Alguma de suas partes vibra',
     ['Alguma de suas partes vibra', 'Fica parado', 'É guardado na caixa', 'É pintado']),
    ('Sons podem causar sensações como:', 'Agitação, incômodo, felicidade ou tranquilidade',
     ['Agitação, incômodo, felicidade ou tranquilidade', 'Apenas alegria', 'Nenhuma sensação', 'Apenas medo']),
    ('O barulho excessivo pode prejudicar:', 'A aprendizagem das crianças e a qualidade de vida',
     ['A aprendizagem das crianças e a qualidade de vida', 'Apenas os adultos', 'Apenas os animais', 'Nada, é inofensivo']),
    ('A Organização Mundial da Saúde considera a poluição sonora um problema de:', 'Saúde pública',
     ['Saúde pública', 'Trânsito apenas', 'Educação apenas', 'Meio ambiente apenas, sem afetar pessoas']),
]
for enunciado, resposta, opcoes in sons:
    criar_questao(ciencias, 'sons', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 3 — SOLO
# ══════════════════════════════════════════════════════════════════
print("\n🪨 Populando: Ciências › Solo...")

solo = [
    ('O solo é formado por:', 'Minerais, materiais orgânicos, ar e água',
     ['Minerais, materiais orgânicos, ar e água', 'Apenas água e areia', 'Apenas rochas', 'Apenas plantas']),
    ('A formação do solo é um processo:', 'Lento e contínuo, resultado do desgaste das rochas',
     ['Lento e contínuo, resultado do desgaste das rochas', 'Rápido e instantâneo', 'Feito só pelo homem', 'Que não muda nunca']),
    ('O solo humoso (terra preta) é formado principalmente pela ação de:', 'Minhocas',
     ['Minhocas', 'Formigas apenas', 'Chuva apenas', 'Vento apenas']),
    ('O húmus é:', 'Uma terra escura e rica em nutrientes',
     ['Uma terra escura e rica em nutrientes', 'Um tipo de rocha dura', 'Um produto químico industrial', 'Um tipo de água']),
    ('O solo arenoso possui grande quantidade de:', 'Areia', ['Areia', 'Argila', 'Húmus', 'Minhocas']),
    ('O solo argiloso é formado por partículas:', 'Menores e mais macias que as do solo arenoso',
     ['Menores e mais macias que as do solo arenoso', 'Maiores e mais duras', 'Do mesmo tamanho da areia', 'Invisíveis a olho nu']),
    ('A aração é a etapa do preparo do solo que:', 'Revira a terra, facilitando o plantio',
     ['Revira a terra, facilitando o plantio', 'Remove o excesso de água', 'Fornece água às plantações', 'Adiciona nutrientes ao solo']),
    ('A irrigação é a etapa do preparo do solo que:', 'Fornece água para as plantações',
     ['Fornece água para as plantações', 'Revira a terra', 'Remove o excesso de água', 'Adiciona nutrientes']),
    ('A drenagem é a etapa do preparo do solo que:', 'Remove o excesso de água do solo',
     ['Remove o excesso de água do solo', 'Fornece água às plantas', 'Revira a terra', 'Planta as sementes']),
    ('A adubação é a etapa do preparo do solo que:', 'Adiciona nutrientes para aumentar a fertilidade',
     ['Adiciona nutrientes para aumentar a fertilidade', 'Remove a água em excesso', 'Revira a terra', 'Retira as pedras do solo']),
    ('Porosidade do solo é:', 'A capacidade do solo de permitir a passagem de água e ar',
     ['A capacidade do solo de permitir a passagem de água e ar', 'A cor do solo', 'O peso do solo', 'O cheiro do solo']),
    ('Solo compactado é um solo:', 'Apertado e duro, sem espaço entre as partículas',
     ['Apertado e duro, sem espaço entre as partículas', 'Solto e fofo', 'Cheio de água', 'Rico em nutrientes']),
    ('A contaminação do solo pode ser causada por:', 'Uso excessivo de agrotóxicos e esgoto doméstico',
     ['Uso excessivo de agrotóxicos e esgoto doméstico', 'Chuva limpa', 'Plantio de árvores', 'Adubação natural']),
    ('A erosão do solo acontece quando:', 'O vento e a chuva carregam o solo',
     ['O vento e a chuva carregam o solo', 'As plantas crescem demais', 'O solo fica muito fértil', 'Chove pouco']),
    ('O desmatamento causa degradação do solo porque:', 'Elimina a proteção natural do solo',
     ['Elimina a proteção natural do solo', 'Deixa o solo mais protegido', 'Aumenta a fertilidade', 'Não tem nenhum efeito']),
    ('As queimadas prejudicam o solo porque:', 'Destroem a vegetação e reduzem a matéria orgânica',
     ['Destroem a vegetação e reduzem a matéria orgânica', 'Aumentam os nutrientes', 'Protegem contra erosão', 'Não afetam o solo']),
    ('Uma prática de conservação do solo é:', 'Evitar o desmatamento e as queimadas',
     ['Evitar o desmatamento e as queimadas', 'Desmatar mais rápido', 'Usar mais agrotóxicos', 'Ignorar o cuidado com a água']),
    ('Manter a cobertura vegetal ajuda a:', 'Proteger o solo da chuva e do vento',
     ['Proteger o solo da chuva e do vento', 'Aumentar a erosão', 'Contaminar o solo', 'Diminuir a fertilidade']),
    ('O solo é essencial para a produção de alimentos porque precisa ser:', 'Fértil, fornecendo nutrientes, água e ar',
     ['Fértil, fornecendo nutrientes, água e ar', 'Seco e duro', 'Compactado', 'Sem nenhum nutriente']),
    ('Além da produção de alimentos, o solo também é usado pelos seres humanos para:', 'Construir moradias e extrair minérios',
     ['Construir moradias e extrair minérios', 'Apenas respirar', 'Apenas nadar', 'Apenas voar']),
]
for enunciado, resposta, opcoes in solo:
    criar_questao(ciencias, 'solo', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 4 — PETRÓLEO
# ══════════════════════════════════════════════════════════════════
print("\n🛢️  Populando: Ciências › Petróleo...")

petroleo = [
    ('O petróleo é:', 'Um líquido escuro encontrado na natureza', ['Um líquido escuro encontrado na natureza', 'Um tipo de rocha', 'Um metal', 'Um gás incolor']),
    ('O petróleo é formado a partir de:', 'Restos de seres vivos acumulados no fundo de rios e mares',
     ['Restos de seres vivos acumulados no fundo de rios e mares', 'Água do mar pura', 'Areia compactada', 'Lixo industrial']),
    ('O petróleo é usado para produzir, entre outras coisas:', 'Combustíveis para os meios de transporte',
     ['Combustíveis para os meios de transporte', 'Apenas alimentos', 'Apenas roupas', 'Apenas remédios']),
    ('Qual das opções abaixo é um produto que pode ter origem do petróleo?', 'Sacola plástica',
     ['Sacola plástica', 'Copo de vidro', 'Caderno de papel', 'Fruta']),
    ('O asfalto das ruas é um produto derivado do:', 'Petróleo', ['Petróleo', 'Solo argiloso', 'Ar', 'Água do mar']),
    ('A fase de bombeamento do petróleo para fora da terra é considerada:', 'Uma fase delicada, que pode causar vazamentos',
     ['Uma fase delicada, que pode causar vazamentos', 'Uma fase sem nenhum risco', 'Uma fase que não usa tecnologia', 'Uma fase que só ocorre no mar']),
    ('Um vazamento de petróleo no meio ambiente pode:', 'Afetar animais, plantas e o homem',
     ['Afetar animais, plantas e o homem', 'Melhorar a qualidade da água', 'Ajudar as plantas a crescer', 'Não causar nenhuma consequência']),
    ('Devemos evitar o desperdício de materiais feitos a partir do petróleo porque:', 'É um recurso natural que pode acabar e polui o ambiente',
     ['É um recurso natural que pode acabar e polui o ambiente', 'Ele se renova em poucos dias', 'Não tem nenhum impacto ambiental', 'É um recurso infinito']),
    ('A gasolina é um exemplo de produto derivado do:', 'Petróleo', ['Petróleo', 'Solo humoso', 'Ar', 'Água']),
    ('O plástico é um material geralmente derivado do:', 'Petróleo', ['Petróleo', 'Solo arenoso', 'Água do mar', 'Minério de ferro']),
    ('Com o passar do tempo, as tecnologias para extração do petróleo:', 'Foram melhorando',
     ['Foram melhorando', 'Pararam de existir', 'Ficaram piores', 'Nunca mudaram']),
    ('Por que o petróleo é considerado importante para a vida das pessoas atualmente?', 'Está presente em muitos objetos do dia a dia',
     ['Está presente em muitos objetos do dia a dia', 'Não é usado em nada', 'Só é usado em foguetes', 'Só é usado em remédios']),
]
for enunciado, resposta, opcoes in petroleo:
    criar_questao(ciencias, 'petroleo', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 5 — SISTEMA SOLAR
# ══════════════════════════════════════════════════════════════════
print("\n🪐 Populando: Ciências › Sistema Solar...")

sistema_solar = [
    ('O movimento em que a Terra gira ao redor do Sol se chama:', 'Translação (revolução)',
     ['Translação (revolução)', 'Rotação', 'Gravidade', 'Órbita reversa']),
    ('O movimento de rotação é responsável por:', 'Criar o dia e a noite',
     ['Criar o dia e a noite', 'Criar as estações do ano', 'Criar a gravidade', 'Criar as marés']),
    ('Qual é o maior planeta do Sistema Solar?', 'Júpiter', ['Júpiter', 'Mercúrio', 'Terra', 'Marte']),
    ('Qual planeta é famoso por seus anéis?', 'Saturno', ['Saturno', 'Vênus', 'Marte', 'Mercúrio']),
    ('O objeto mais brilhante do Sistema Solar é:', 'O Sol', ['O Sol', 'A Lua', 'Júpiter', 'Uma estrela distante']),
    ('O Sol é classificado como:', 'Uma estrela', ['Uma estrela', 'Um planeta', 'Uma lua', 'Um cometa']),
    ('Qual é o planeta mais próximo do Sol?', 'Mercúrio', ['Mercúrio', 'Vênus', 'Terra', 'Marte']),
    ('Quantos planetas existem no Sistema Solar?', '8', ['8', '7', '9', '10']),
    ('A Lua é um(a):', 'Satélite natural da Terra', ['Satélite natural da Terra', 'Planeta', 'Estrela', 'Cometa']),
    ('O planeta em que vivemos se chama:', 'Terra', ['Terra', 'Marte', 'Vênus', 'Netuno']),
    ('Marte é conhecido como o planeta:', 'Vermelho', ['Vermelho', 'Azul', 'Verde', 'Amarelo']),
    ('O conjunto formado pelo Sol e os planetas que giram ao seu redor é chamado de:', 'Sistema Solar',
     ['Sistema Solar', 'Via Láctea', 'Galáxia distante', 'Universo inteiro']),
]
for enunciado, resposta, opcoes in sistema_solar:
    criar_questao(ciencias, 'sistema_solar', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO 6 — DIVERSIDADE DE MODOS DE VIDA (novo)
# ══════════════════════════════════════════════════════════════════
print("\n🐾 Populando: Ciências › Diversidade de Modos de Vida...")

diversidade_modos_vida = [
    ('Animais que vivem em rios, lagos ou no mar habitam um ambiente:', 'Aquático',
     ['Aquático', 'Terrestre', 'Aéreo', 'Subterrâneo']),
    ('Animais que vivem sobre o solo, como o cachorro e o leão, habitam um ambiente:', 'Terrestre',
     ['Terrestre', 'Aquático', 'Aéreo', 'Marinho']),
    ('Animais que se alimentam apenas de plantas são chamados de:', 'Herbívoros',
     ['Herbívoros', 'Carnívoros', 'Onívoros', 'Insetívoros']),
    ('Animais que se alimentam de outros animais são chamados de:', 'Carnívoros',
     ['Carnívoros', 'Herbívoros', 'Onívoros', 'Vegetarianos']),
    ('Animais que se alimentam tanto de plantas quanto de outros animais são chamados de:', 'Onívoros',
     ['Onívoros', 'Herbívoros', 'Carnívoros', 'Fotossintéticos']),
    ('O leão é um exemplo de animal:', 'Carnívoro', ['Carnívoro', 'Herbívoro', 'Onívoro', 'Vegetariano']),
    ('A vaca é um exemplo de animal:', 'Herbívoro', ['Herbívoro', 'Carnívoro', 'Onívoro', 'Insetívoro']),
    ('O processo pelo qual um animal gera um filhote é chamado de:', 'Reprodução',
     ['Reprodução', 'Respiração', 'Digestão', 'Fotossíntese']),
    ('Animais que nascem de ovos são chamados de:', 'Ovíparos', ['Ovíparos', 'Vivíparos', 'Herbívoros', 'Onívoros']),
    ('Animais que se desenvolvem dentro do corpo da mãe e nascem vivos são chamados de:', 'Vivíparos',
     ['Vivíparos', 'Ovíparos', 'Carnívoros', 'Terrestres']),
    ('O cachorro é um animal:', 'Vivíparo', ['Vivíparo', 'Ovíparo', 'Herbívoro', 'Aquático']),
    ('A galinha é um animal:', 'Ovíparo', ['Ovíparo', 'Vivíparo', 'Carnívoro', 'Aquático']),
    ('Não podemos dizer que um gato passa por metamorfose porque:', 'Ele não nasce de ovo e já nasce parecido com um adulto',
     ['Ele não nasce de ovo e já nasce parecido com um adulto', 'Ele é herbívoro', 'Ele vive na água', 'Ele é muito pequeno']),
    ('Uma borboleta, ao contrário de um gato, passa por um processo chamado:', 'Metamorfose',
     ['Metamorfose', 'Reprodução simples', 'Hibernação', 'Fotossíntese']),
    ('O João-de-barro constrói seu próprio ninho de barro. Ele se alimenta principalmente de:', 'Insetos, como cupins, formigas e minhocas',
     ['Insetos, como cupins, formigas e minhocas', 'Apenas sementes e frutas', 'Apenas outros pássaros', 'Apenas plantas aquáticas']),
    ('Por que o João-de-barro é considerado um animal carnívoro?', 'Porque se alimenta de pequenos insetos',
     ['Porque se alimenta de pequenos insetos', 'Porque come apenas frutas', 'Porque vive na água', 'Porque não se reproduz']),
    ('O que aconteceria com os animais se a etapa da "reprodução" do ciclo de vida deixasse de existir?', 'Não haveria mais animais no mundo',
     ['Não haveria mais animais no mundo', 'Os animais ficariam mais fortes', 'Nada mudaria', 'Os animais se tornariam aquáticos']),
    ('Uma tartaruga e um jacaré vivem no mesmo grupo de animais porque ambos são:', 'Ovíparos',
     ['Ovíparos', 'Vivíparos', 'Herbívoros', 'Aquáticos apenas']),
]
for enunciado, resposta, opcoes in diversidade_modos_vida:
    criar_questao(ciencias, 'diversidade_modos_vida', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# MÓDULO NOVO — VERTEBRADOS E INVERTEBRADOS
# ══════════════════════════════════════════════════════════════════
print("\n🦴 Populando: Ciências › Vertebrados e Invertebrados...")

vertebrados_invertebrados = [
    ('Os animais vertebrados apresentam esqueletos internos com crânio e:', 'Coluna vertebral',
     ['Coluna vertebral', 'Exoesqueleto', 'Casco', 'Concha']),
    ('Os animais invertebrados não têm esqueleto interno, ou seja, não têm crânio nem:', 'Coluna vertebral',
     ['Coluna vertebral', 'Exoesqueleto', 'Antenas', 'Patas']),
    ('A coluna vertebral se conecta a qual estrutura?', 'Ao crânio',
     ['Ao crânio', 'Ao exoesqueleto', 'À pele', 'Às patas']),
    ('O crânio é composto de ossos que formam:', 'A cabeça',
     ['A cabeça', 'As patas', 'A cauda', 'O tronco']),
    ('Quais são os 5 principais grupos de vertebrados?', 'Peixes, anfíbios, répteis, aves e mamíferos',
     ['Peixes, anfíbios, répteis, aves e mamíferos', 'Insetos, aranhas e moluscos',
      'Apenas répteis e aves', 'Cnidários e equinodermos']),
    ('Os peixes são animais aquáticos com corpo geralmente coberto por:', 'Escamas',
     ['Escamas', 'Penas', 'Pelos', 'Exoesqueleto']),
    ('Os anfíbios costumam viver próximo a lagos e rios, e sua pele costuma ser:', 'Fina e úmida',
     ['Fina e úmida', 'Grossa e seca', 'Coberta de penas', 'Coberta de conchas']),
    ('A maioria dos répteis apresenta pele grossa, formada por escamas ou:', 'Carapaças',
     ['Carapaças', 'Penas', 'Pelos', 'Brânquias']),
    ('As aves são animais cobertos por penas e apresentam:', 'Bico',
     ['Bico', 'Brânquias', 'Carapaça', 'Exoesqueleto']),
    ('Os mamíferos alimentam seus filhotes com:', 'Leite materno',
     ['Leite materno', 'Insetos', 'Apenas plantas', 'Néctar']),
    ('Uma estrutura externa rígida que ajuda a sustentar o corpo de alguns invertebrados é chamada de:', 'Exoesqueleto',
     ['Exoesqueleto', 'Endoesqueleto', 'Coluna vertebral', 'Crânio']),
    ('Cnidários são um grupo de invertebrados que inclui corais, águas-vivas e:', 'Anêmonas',
     ['Anêmonas', 'Caramujos', 'Minhocas', 'Estrelas-do-mar']),
    ('Moluscos são um grupo de invertebrados que inclui caramujos, mexilhões, polvos e:', 'Lulas',
     ['Lulas', 'Aranhas', 'Corais', 'Minhocas']),
    ('Anelídeos são um grupo de invertebrados que inclui minhocas e:', 'Sanguessugas',
     ['Sanguessugas', 'Formigas', 'Águas-vivas', 'Estrelas-do-mar']),
    ('Equinodermos são um grupo de invertebrados que inclui estrelas-do-mar e:', 'Ouriços-do-mar',
     ['Ouriços-do-mar', 'Aranhas', 'Polvos', 'Sanguessugas']),
    ('Artrópodes são um grupo de invertebrados que inclui insetos, aranhas, caranguejos e:', 'Centopeias',
     ['Centopeias', 'Águas-vivas', 'Estrelas-do-mar', 'Minhocas']),
    ('Um gato é um exemplo de animal:', 'Vertebrado',
     ['Vertebrado', 'Invertebrado', 'Cnidário', 'Molusco']),
    ('Uma joaninha é um exemplo de animal:', 'Invertebrado',
     ['Invertebrado', 'Vertebrado', 'Mamífero', 'Réptil']),
]
for enunciado, resposta, opcoes in vertebrados_invertebrados:
    criar_questao(ciencias, 'vertebrados_invertebrados', enunciado, resposta, opcoes)


# ══════════════════════════════════════════════════════════════════
# BLOCO NOVO — a partir da atividade e do mapa mental de 14/08/2026
# (Unidade 3, capítulos 1 e 2 — "Seres humanos e outros animais")
# ══════════════════════════════════════════════════════════════════
print("\n🦴 Populando: Ciências › Vertebrados e Invertebrados (bloco novo)...")

vertebrados_invertebrados_novo = [
    ('O grupo dos aracnídeos, que possui esqueleto externo, inclui as aranhas e:', 'Os escorpiões',
     ['Os escorpiões', 'Os camarões', 'As minhocas', 'Os caramujos']),
    ('O grupo dos crustáceos, que possui esqueleto externo, inclui os camarões e:', 'Os caranguejos',
     ['Os caranguejos', 'As aranhas', 'As minhocas', 'Os caracóis']),
    ('Insetos como borboletas, abelhas e formigas pertencem ao grupo dos:', 'Invertebrados',
     ['Invertebrados', 'Vertebrados', 'Mamíferos', 'Répteis']),
    ('O bem-te-vi pertence a qual grupo de vertebrados?', 'Aves', ['Aves', 'Répteis', 'Mamíferos', 'Anfíbios']),
    ('O jacaré pertence a qual grupo de vertebrados?', 'Répteis', ['Répteis', 'Aves', 'Anfíbios', 'Mamíferos']),
    ('O tamanduá-bandeira pertence a qual grupo de vertebrados?', 'Mamíferos', ['Mamíferos', 'Répteis', 'Aves', 'Peixes']),
    ('O sapo pertence a qual grupo de vertebrados?', 'Anfíbios', ['Anfíbios', 'Répteis', 'Peixes', 'Mamíferos']),
    ('A tilápia pertence a qual grupo de vertebrados?', 'Peixes', ['Peixes', 'Anfíbios', 'Répteis', 'Mamíferos']),
    ('Um animal vive na água, respira por brânquias, possui nadadeiras e o corpo coberto por escamas. Esse animal pertence ao grupo dos:', 'Peixes',
     ['Peixes', 'Mamíferos', 'Aves', 'Anfíbios']),
    ('Um animal possui penas, tem bico e nasce de ovos. Esse animal pertence ao grupo dos:', 'Aves',
     ['Aves', 'Répteis', 'Mamíferos', 'Peixes']),
    ('Entre cachorro, borboleta, sapo, peixe, formiga, bem-te-vi, lagarto e polvo, quais são invertebrados?', 'Borboleta, formiga e polvo',
     ['Borboleta, formiga e polvo', 'Cachorro, sapo e peixe', 'Bem-te-vi e lagarto', 'Todos são invertebrados']),
    ('Entre cachorro, borboleta, sapo, peixe, formiga, bem-te-vi, lagarto e polvo, quais são vertebrados?', 'Cachorro, sapo, peixe, bem-te-vi e lagarto',
     ['Cachorro, sapo, peixe, bem-te-vi e lagarto', 'Borboleta, formiga e polvo', 'Apenas o cachorro', 'Todos são vertebrados']),
]
for enunciado, resposta, opcoes in vertebrados_invertebrados_novo:
    criar_questao(ciencias, 'vertebrados_invertebrados', enunciado, resposta, opcoes)


print("\n🐾 Populando: Ciências › Diversidade de Modos de Vida (bloco novo)...")

diversidade_modos_vida_novo = [
    ('A galinha vive em ambiente terrestre e se alimenta de grãos, sementes e pequenos insetos. Por isso, ela é classificada como:', 'Onívora',
     ['Onívora', 'Herbívora', 'Carnívora', 'Aquática']),
    ('A galinha se reproduz da seguinte forma:', 'É ovípara, pois nasce de ovos',
     ['É ovípara, pois nasce de ovos', 'É vivípara, pois nasce do corpo da mãe', 'Não se reproduz', 'É ovovivípara']),
    ('A vaca vive em ambiente terrestre, se alimenta de plantas e nasce do corpo da mãe. Sobre sua reprodução, podemos dizer que ela é:', 'Vivípara',
     ['Vivípara', 'Ovípara', 'Ovovivípara', 'Não se reproduz']),
    ('A baleia vive no ambiente aquático, mas, ao contrário dos peixes, ela é um animal:', 'Vivíparo e mamífero',
     ['Vivíparo e mamífero', 'Ovíparo e peixe', 'Ovíparo e réptil', 'Vivíparo e ave']),
    ('A baleia se alimenta de outros animais, sendo portanto classificada como:', 'Carnívora',
     ['Carnívora', 'Herbívora', 'Onívora', 'Fotossintética']),
    ('O bem-te-vi vive em ambiente terrestre e se alimenta tanto de insetos quanto de frutas. Por isso, é classificado como:', 'Onívoro',
     ['Onívoro', 'Herbívoro', 'Carnívoro', 'Aquático']),
    ('O cavalo vive, principalmente, em qual ambiente?', 'Terrestre', ['Terrestre', 'Aquático', 'Aéreo', 'Subterrâneo']),
    ('Animais como leões, elefantes, cachorros e formigas, que vivem sobre a terra, são chamados de animais:', 'Terrestres',
     ['Terrestres', 'Aquáticos', 'Aéreos', 'Arborícolas']),
    ('Animais como peixes, golfinhos, polvos e baleias, que vivem na água, são chamados de animais:', 'Aquáticos',
     ['Aquáticos', 'Terrestres', 'Aéreos', 'Anfíbios']),
    ('Humanos, ursos e porcos são exemplos de animais que se alimentam tanto de plantas quanto de outros animais, sendo por isso chamados de:', 'Onívoros',
     ['Onívoros', 'Herbívoros', 'Carnívoros', 'Vegetarianos']),
    ('Por que o ambiente em que um animal vive influencia o seu modo de vida?', 'Porque cada ambiente exige adaptações diferentes para a sobrevivência do animal',
     ['Porque cada ambiente exige adaptações diferentes para a sobrevivência do animal', 'O ambiente não influencia em nada o modo de vida do animal',
      'Porque todos os animais vivem exatamente da mesma forma, em qualquer lugar', 'Porque o ambiente só influencia a cor do animal']),
]
for enunciado, resposta, opcoes in diversidade_modos_vida_novo:
    criar_questao(ciencias, 'diversidade_modos_vida', enunciado, resposta, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE CIÊNCIAS CONCLUÍDA!")
print("=" * 55)
for modulo, nome in [
    ('plantas', 'Plantas'),
    ('sons', 'Sons'),
    ('solo', 'Solo'),
    ('petroleo', 'Petróleo'),
    ('sistema_solar', 'Sistema Solar'),
    ('diversidade_modos_vida', 'Diversidade de Modos de Vida'),
    ('vertebrados_invertebrados', 'Vertebrados e Invertebrados'),
]:
    total = BancoQuestao.objects.filter(disciplina=ciencias, modulo=modulo).count()
    print(f"   {nome:.<32} {total}")
