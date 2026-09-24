"""
popular_portugues_prova_3periodo.py
----------------------------------------
Execute na raiz do projeto:
    python popular_portugues_prova_3periodo.py

Popula o banco com o novo card de Português:
  - prova_3periodo (PORT - Prova 3º Período)

Baseado na Avaliação de Língua Portuguesa do 3º Período (08/09/2026)
— Colégio Santo Agostinho:
  - Texto 1: fábula "O camelo e o beija-flor" (Dilea Frate, Fábulas Tortas)
  - Dígrafo, sílabas, encontro vocálico, pronome pessoal, artigo,
    substantivo comum, verbo (tempo, infinitivo, conjugação), sons do X
  - Texto 2: "Como atrair beija-flor para a sua casa..." (Rádio Itatiaia)
  - Classe gramatical, gênero, adjetivos, plural
  - S inicial, S intervocálico e SS
  - Texto 3: tirinha Níquel Náusea

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


print("\n📚 Garantindo disciplina Português...")
portugues, _ = Disciplina.objects.get_or_create(nome='portugues', defaults={'nome_exibicao': 'Português'})
print("  ✅ Português pronto.")

print("\n🏆 Populando: Português › PORT - Prova 3º Período...")
T1 = '(Texto 1: "O camelo e o beija-flor")\n'
TRECHO = ('Trecho: "O beija-flor, que quase não tinha mais energia para continuar voando, '
          'suspirou fundo, fechou os olhos e deixou-se cair agonizante sobre a areia."\n')
T2 = '(Texto 2: "Como atrair beija-flor para a sua casa")\n'
questoes = [
    # ── Texto 1 — interpretação ──
    (T1 + 'Que tipo de texto é "O camelo e o beija-flor"?', 'Uma fábula',
     ['Uma receita', 'Uma notícia de jornal', 'Um poema']),
    (T1 + 'Onde o beija-flor morava?', 'Numa floresta tropical',
     ['No deserto', 'Num oásis', 'No jardim de uma casa']),
    (T1 + 'Por que o beija-flor precisava encontrar um lugar para descansar?',
     'Porque voou muito, estava cansado e perdido no deserto',
     ['Porque queria brincar com o camelo', 'Porque estava com frio na floresta', 'Porque queria comer areia']),
    (T1 + 'Qual afirmativa sobre a fábula é FALSA?', 'O texto apresenta informações científicas sobre os animais.',
     ['Os personagens vivem uma situação que transmite um ensinamento.',
      'Os personagens conversam e têm atitudes semelhantes às humanas.',
      'A história apresenta acontecimentos imaginários.']),
    (T1 + 'O que o camelo fez ao perceber que o beija-flor estava quase sem forças?',
     'Ofereceu para ele subir na sua corcova e o levou até o oásis',
     ['Mandou o beija-flor embora', 'Deu flores para o beija-flor', 'Fingiu que não viu o beija-flor']),
    (T1 + 'O camelo nunca tinha visto...', 'uma flor', ['um oásis', 'a areia', 'a água']),
    (T1 + 'Qual ensinamento combina MAIS com a fábula?', 'Pessoas diferentes podem ajudar umas às outras.',
     ['Cada um deve resolver sozinho suas dificuldades.', 'Só devemos ajudar quem é parecido conosco.',
      'Quem é pequeno não precisa de ajuda.']),
    (T1 + 'Qual característica combina com a atitude do camelo?', 'Generoso',
     ['Egoísta', 'Indiferente', 'Preguiçoso']),
    (T1 + 'Qual OUTRA característica combina com a atitude do camelo?', 'Solidário',
     ['Egoísta', 'Indiferente', 'Mentiroso']),
    (TRECHO + 'A expressão que melhor explica como o beija-flor se sentia é:', 'Quase sem forças',
     ['Cheio de disposição', 'Muito assustado', 'Muito feliz']),
    # Vocabulário
    (T1 + 'O que significa "ruminando"?', 'Mastigando novamente o alimento',
     ['Correndo muito rápido', 'Dormindo na areia', 'Bebendo muita água']),
    (T1 + 'O que é um "oásis"?', 'Lugar no deserto onde existe água e vegetação',
     ['Um tipo de camelo', 'Uma tempestade de areia', 'Uma flor do deserto']),
    (T1 + 'O que significa "agonizante"?', 'Muito enfraquecido, quase sem forças',
     ['Muito alegre', 'Muito rápido', 'Muito bravo']),
    (T1 + 'O que significa "escaldante"?', 'Muito quente', ['Muito frio', 'Muito molhado', 'Muito escuro']),

    # ── Gramática no trecho ──
    (TRECHO + 'Qual palavra do trecho é DISSÍLABA e tem DÍGRAFO?', 'tinha', ['areia', 'cair', 'suspirou']),
    (TRECHO + 'Qual palavra do trecho é POLISSÍLABA e tem ENCONTRO VOCÁLICO?', 'continuar',
     ['fechou', 'olhos', 'cair']),
    ('Trecho: "O beija-flor reuniu as últimas energias e subiu na corcova do camelo."\n'
     'Qual PRONOME PESSOAL pode substituir "O beija-flor", sem mudar o sentido?', 'Ele', ['Ela', 'Eles', 'Nós']),
    ('Trecho: "O camelo se aproximou, abaixou e falou no seu ouvido."\nQual é um ARTIGO DEFINIDO desse trecho?', 'o',
     ['um', 'seu', 'se']),
    ('Trecho: "O beija-flor reuniu as últimas energias e subiu na corcova do camelo."\n'
     'Qual palavra é um SUBSTANTIVO COMUM?', 'camelo', ['reuniu', 'últimas', 'subiu']),
    ('O verbo "subiu" está em qual tempo verbal?', 'Passado (pretérito)', ['Presente', 'Futuro', 'Infinitivo']),
    ('Qual é o INFINITIVO do verbo "subiu"?', 'subir', ['subia', 'subindo', 'sobe']),
    ('O verbo "subir" pertence a qual conjugação?', '3ª conjugação (-IR)',
     ['1ª conjugação (-AR)', '2ª conjugação (-ER)', 'Não tem conjugação']),
    ('Em "aproximou", a letra X tem som de SS. Em qual grupo TODAS as palavras têm esse mesmo som do X?',
     'auxílio – próximo – máximo', ['exemplo – exato – exercício', 'boxe – táxi – reflexo', 'xícara – peixe – caixa']),

    # ── Texto 2 ──
    (T2 + 'Verdadeiro ou falso: "Flores nativas e coloridas ajudam a atrair beija-flores."', 'Verdadeiro',
     ['Falso', 'O texto não fala disso', 'Só flores brancas atraem']),
    (T2 + 'Verdadeiro ou falso: "Os bebedouros não precisam ser higienizados."', 'Falso',
     ['Verdadeiro', 'Só no inverno', 'O texto não fala disso']),
    (T2 + 'Verdadeiro ou falso: "Para cuidar das aves, o ideal é mantê-las presas."', 'Falso',
     ['Verdadeiro', 'Só os filhotes', 'O texto não fala disso']),
    (T2 + 'Por que os bebedouros devem ser mantidos limpos?', 'Para evitar fungos e bactérias que causam doenças nas aves',
     ['Para ficarem mais bonitos', 'Para atrair abelhas', 'Para a água ficar gelada']),
    (T2 + 'Qual é uma atitude CERTA para cuidar do bem-estar dos beija-flores?',
     'Cultivar flores nativas e manter os bebedouros limpos',
     ['Prender os beija-flores em gaiolas', 'Cortar todas as árvores do jardim', 'Nunca limpar os bebedouros']),
    ('Frase: "Uma boa opção é cultivar flores nativas e coloridas."\nQual é a classe gramatical da palavra "flores"?',
     'Substantivo', ['Adjetivo', 'Verbo', 'Artigo']),
    ('Frase: "Uma boa opção é cultivar flores nativas e coloridas."\nA palavra "flores" é do gênero...', 'feminino',
     ['masculino', 'neutro', 'plural']),
    ('Frase: "Uma boa opção é cultivar flores nativas e coloridas."\nQuais são os dois ADJETIVOS que caracterizam as flores?',
     'nativas e coloridas', ['boa e opção', 'cultivar e flores', 'uma e boa']),
    ('Passe para o PLURAL: "O pequeno pássaro visitou o jardim."', 'Os pequenos pássaros visitaram os jardins.',
     ['Os pequeno pássaros visitou os jardim.', 'Os pequenos pássaros visitou o jardim.',
      'O pequenos pássaro visitaram os jardins.']),

    # ── S inicial, S intervocálico, SS ──
    ('Na palavra SOMBRA, o S é...', 'S inicial', ['S intervocálico', 'SS', 'S final']),
    ('Na palavra CAUSAR, o S é...', 'S intervocálico (entre vogais, som de Z)', ['S inicial', 'SS', 'S final']),
    ('Na palavra ESSES, aparece...', 'SS', ['S inicial', 'Só S intervocálico', 'Nenhum S']),
    ('Na palavra SÃO, o S é...', 'S inicial', ['S intervocálico', 'SS', 'S final']),
    ('Qual palavra tem S INTERVOCÁLICO (com som de Z)?', 'casa', ['sapo', 'passo', 'sol']),

    # ── Texto 3 — tirinha Níquel Náusea ──
    ('Tirinha: "Sabia que o beija-flor bate a asa setenta vezes por segundo?" ... "Incrível é quem contou!"\n'
     'O que realmente deixou o ratinho impressionado?', 'Alguém ter conseguido contar tantas batidas das asas',
     ['O beija-flor saber conversar', 'O beija-flor não saber quantas vezes bate as asas', 'O beija-flor ser muito grande']),
    ('Nos três textos, o beija-flor aparece de maneiras diferentes. Qual texto apresenta INFORMAÇÕES REAIS sobre a ave?',
     'Texto 2 (como atrair beija-flores)', ['Texto 1 (a fábula)', 'Texto 3 (a tirinha)', 'Nenhum deles']),
    ('Qual texto apresenta o beija-flor como PERSONAGEM DE UMA FÁBULA?', 'Texto 1 (O camelo e o beija-flor)',
     ['Texto 2 (como atrair beija-flores)', 'Texto 3 (a tirinha)', 'Nenhum deles']),
    ('Qual texto apresenta uma CURIOSIDADE de maneira DIVERTIDA?', 'Texto 3 (a tirinha)',
     ['Texto 1 (a fábula)', 'Texto 2 (como atrair beija-flores)', 'Nenhum deles']),
]
for enunciado, resposta, erradas in questoes:
    criar_questao(portugues, enunciado, resposta, erradas)

total = BancoQuestao.objects.filter(disciplina=portugues, modulo=MODULO).count()
print(f"\n🎉 Pronto! O card 'PORT - Prova 3º Período' tem {total} questões.")
