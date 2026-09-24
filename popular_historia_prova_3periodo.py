"""
popular_historia_prova_3periodo.py
----------------------------------------
Execute na raiz do projeto:
    python popular_historia_prova_3periodo.py

Popula o banco com o novo card de História:
  - prova_3periodo (HIST - Prova 3º Período)

Baseado na Avaliação de História do 3º Período (15/09/2026) —
Colégio Santo Agostinho:
  - Texto "A terra e a vida dos povos indígenas"
  - A chegada dos portugueses, doenças, contribuições indígenas
  - A menina indígena Lia (V ou F)
  - Por que foram chamados de "índios"
  - Cultura (tirinha: "Não há saber mais ou saber menos. Há saberes diferentes.")
  - Povos formadores da cultura brasileira e heranças culturais
  - Escambo, conhecimentos indígenas, primeiros encontros
  - Texto de completar (portugueses, indígenas, culturas, pau-brasil,
    religião, armas, doenças)

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


print("\n🏛️ Garantindo disciplina História...")
historia, _ = Disciplina.objects.get_or_create(nome='historia', defaults={'nome_exibicao': 'História'})
print("  ✅ História pronta.")

print("\n🏆 Populando: História › HIST - Prova 3º Período...")
T = '(Texto: "A terra e a vida dos povos indígenas")\n'
questoes = [
    # ── Texto e povos indígenas ──
    (T + 'Há quanto tempo os povos indígenas vivem no território brasileiro?', 'Há milhares de anos',
     ['Há 10 anos', 'Desde 1988', 'Há 100 anos']),
    (T + 'Em que ano os portugueses chegaram ao Brasil?', '1500', ['1822', '1888', '1988']),
    ('Existem mais de 260 povos indígenas no Brasil. Qual afirmativa está CORRETA?',
     'Há diferentes povos indígenas e diferentes modos de eles viverem no Brasil.',
     ['Todos os povos indígenas vivem isolados na floresta.', 'Os povos indígenas vivem de uma única maneira.',
      'Não existem mais povos indígenas no Brasil.']),
    ('Qual exemplo mostra uma contribuição indígena que continua presente no Brasil de hoje?',
     'O uso de alimentos, palavras e modos de viver ensinados pelos povos indígenas.',
     ['A construção de igrejas com grandes torres e sinos.', 'A chegada de imigrantes europeus para trabalhar nas cidades.',
      'O uso de moedas de ouro de Portugal.']),
    ('Por que a terra é importante para a sobrevivência e a cultura dos povos indígenas?',
     'Porque a terra garante alimento, espaço para viver e preservação de sua cultura.',
     ['Porque é nela que podem construir prédios para viver.', 'Porque é usada apenas para vender e conseguir dinheiro.',
      'Porque a terra não é importante para eles.']),
    ('Com os europeus chegaram doenças como gripe, tuberculose e varíola. É correto afirmar que:',
     'Muitos indígenas ficaram doentes porque não tinham a mesma defesa do corpo contra essas doenças.',
     ['As doenças não causaram nenhum problema aos povos indígenas.',
      'As doenças fizeram desaparecer todas as culturas indígenas.', 'Os indígenas já conheciam essas doenças.']),
    (T + 'O que aconteceu com muitos povos indígenas depois da chegada dos portugueses?',
     'Tiveram suas terras ocupadas e sofreram com doenças, conflitos e expulsões.',
     ['Ficaram mais ricos vendendo ouro.', 'Mudaram-se todos para Portugal.', 'Nada mudou na vida deles.']),
    (T + 'Hoje, proteger as terras indígenas também significa...', 'respeitar a história, a cultura e os direitos dos povos indígenas',
     ['construir mais cidades nessas terras', 'proibir os indígenas de estudar', 'acabar com as florestas']),

    # ── Lia ──
    ('Lia é uma menina indígena que vai à escola e participa das celebrações do seu povo. Verdadeiro ou falso: '
     '"As crianças indígenas podem aprender conhecimentos tradicionais de seu povo e também frequentar escolas."',
     'Verdadeiro', ['Falso', 'Só os meninos', 'Só na cidade']),
    ('Sobre as crianças indígenas, verdadeiro ou falso: '
     '"Todas as crianças indígenas vivem da mesma maneira e possuem os mesmos costumes."',
     'Falso', ['Verdadeiro', 'Só na floresta', 'Só no Norte']),
    ('Sobre as crianças indígenas, verdadeiro ou falso: '
     '"Atualmente, algumas crianças indígenas utilizam tecnologias, como celulares e computadores."',
     'Verdadeiro', ['Falso', 'Só os adultos', 'É proibido']),
    ('Sobre as crianças indígenas, verdadeiro ou falso: '
     '"As tradições indígenas deixaram de existir porque os povos indígenas passaram a ter contato com outras culturas."',
     'Falso', ['Verdadeiro', 'Só algumas', 'Só na cidade']),

    # ── "Índios" ──
    ('Por que os povos que viviam no território que hoje chamamos de Brasil foram chamados de "índios" pelos portugueses?',
     'Porque os portugueses achavam que tinham chegado às Índias',
     ['Porque esse era o nome que eles davam a si mesmos', 'Porque moravam perto de um rio chamado Índio',
      'Porque falavam a língua portuguesa']),

    # ── Cultura ──
    ('O que é CULTURA?', 'Tudo o que um povo aprende, vive e compartilha, como comidas, festas, músicas, palavras e costumes',
     ['Apenas aquilo que vemos nos museus', 'Apenas o que herdamos dos portugueses', 'Apenas os livros antigos']),
    ('Na tirinha de Paulo Freire: "Não há saber mais ou saber menos. Há saberes ___."', 'diferentes',
     ['iguais', 'errados', 'melhores']),
    ('Quais povos contribuíram para a formação da cultura brasileira?', 'Indígenas, portugueses e africanos',
     ['Apenas os portugueses', 'Apenas os indígenas', 'Chineses, japoneses e russos']),
    ('Qual é uma herança cultural deixada pelos AFRICANOS?', 'A capoeira e o samba',
     ['A língua portuguesa', 'A rede de dormir', 'O pau-brasil']),
    ('Qual é uma herança cultural deixada pelos INDÍGENAS?', 'O uso da mandioca e da rede de dormir',
     ['A língua portuguesa', 'A capoeira', 'As moedas de ouro']),
    ('Qual é uma herança cultural deixada pelos PORTUGUESES?', 'A língua portuguesa',
     ['A capoeira', 'A rede de dormir', 'O uso da mandioca']),

    # ── Relacionar ──
    ('O que foi o ESCAMBO?', 'Troca de objetos e produtos, sem o uso de dinheiro',
     ['Um tipo de moeda portuguesa', 'Uma festa indígena', 'Um navio português']),
    ('Os CONHECIMENTOS INDÍGENAS estão ligados a...', 'plantas, animais, alimentos e caminhos',
     ['navios e armas de fogo', 'moedas e bancos', 'prédios e fábricas']),
    ('O que foram os PRIMEIROS ENCONTROS?', 'Momentos em que indígenas e portugueses conheceram diferentes modos de vida e realizaram trocas',
     ['Reuniões na escola', 'Festas em Portugal', 'Jogos de futebol']),

    # ── Completar o texto ──
    ('Complete: "Quando os portugueses e os indígenas se encontraram, perceberam diferenças entre suas ______."',
     'culturas', ['armas', 'doenças', 'religião']),
    ('Complete: "Os portugueses trouxeram ______ e ferramentas de metal."', 'armas',
     ['culturas', 'pau-brasil', 'indígenas']),
    ('Complete: "No início, houve trocas de objetos e coleta de ______."', 'pau-brasil',
     ['doenças', 'armas', 'religião']),
    ('Complete: "Depois, ocorreram conflitos, escravização e imposição de ______."', 'religião',
     ['pau-brasil', 'culturas', 'armas']),
    ('Complete: "Além disso, ______ trazidas pelos europeus causaram muitas mortes entre os indígenas."', 'doenças',
     ['culturas', 'armas', 'religiões']),
]
for enunciado, resposta, erradas in questoes:
    criar_questao(historia, enunciado, resposta, erradas)

total = BancoQuestao.objects.filter(disciplina=historia, modulo=MODULO).count()
print(f"\n🎉 Pronto! O card 'HIST - Prova 3º Período' tem {total} questões.")
