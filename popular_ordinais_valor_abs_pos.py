"""
popular_ordinais_valor_abs_pos.py
------------------------------------
Execute na raiz do projeto:
    python popular_ordinais_valor_abs_pos.py

Popula o banco com questões de Matemática — "Números Ordinais, Valor
Absoluto e Posicional": ordens, classes, algarismos, posição e nome
das ordens, valor absoluto e posicional, e números ordinais
(sequência e escrita por extenso).

Card criado especificamente porque este é o recorte de conteúdo
cobrado na Avaliação de Matemática do 2º Período (Colégio Santo
Agostinho, 3º ano) — ver Caderno 9 (Valor Absoluto e Posicional),
Caderno 10 (Números Ordinais) e a prova-modelo (fl. 57).

Combina dois grupos de questões, de propósito:
  1) com os MESMOS números que aparecem nas folhas e na prova-modelo
     (1.935, 5.539 etc.) — para o aluno reconhecer o padrão do
     material que já estudou;
  2) com números autorais (4.827, 6.827 etc.) — para o aluno aplicar
     o raciocínio em cima de números que nunca viu, e não apenas
     decorar a resposta.

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
    print(f"  {status}: {enunciado[:65]}")


print("\n🧮 Criando disciplina Matemática (se ainda não existir)...")
matematica, _ = Disciplina.objects.get_or_create(
    nome='matematica', defaults={'nome_exibicao': 'Matemática'}
)
print("  ✅ Matemática pronta.")

print("\n#️⃣ Populando: Matemática › Números Ordinais, Valor Absoluto e Posicional...")

questoes = [
    # Valor posicional (números da folha "Valor Absoluto e Posicional" e da prova)
    ('No número 1.935, qual é o valor posicional do algarismo 5 (que ocupa a ordem das unidades)?', '5', ['5', '50', '500', '15']),
    ('No número 1.935, qual é o valor posicional do algarismo 3 (que ocupa a ordem das dezenas)?', '30', ['30', '300', '40', '3']),
    ('No número 1.935, qual é o valor posicional do algarismo 9 (que ocupa a ordem das centenas)?', '900', ['900', '90', '910', '1.000']),
    ('No número 1.935, qual é o valor posicional do algarismo 1 (que ocupa a ordem das unidades de milhar)?', '1.000', ['1.000', '10', '100', '1.010']),
    ('No número 569, qual é o valor posicional do algarismo 5 (que ocupa a ordem das centenas)?', '500', ['500', '50', '510', '600']),
    ('No número 478, qual é o valor posicional do algarismo 8 (que ocupa a ordem das unidades)?', '8', ['8', '80', '800', '18']),
    ('No número 2.054, qual é o valor posicional do algarismo 2 (que ocupa a ordem das unidades de milhar)?', '2.000', ['2.000', '20', '200', '2.010']),
    ('No número 1.653, qual é o valor posicional do algarismo 6 (que ocupa a ordem das centenas)?', '600', ['600', '60', '610', '700']),

    # Valor absoluto (números da folha e da prova)
    ('No número 154, qual é o valor absoluto do algarismo 5 (que ocupa a ordem das dezenas)?', '5', ['5', '1', '4', '6']),
    ('No número 9.143, qual é o valor absoluto do algarismo 9 (que ocupa a ordem das unidades de milhar)?', '9', ['9', '1', '3', '4']),
    ('No número 3.299, qual é o valor absoluto do algarismo 9 (que ocupa a ordem das unidades)?', '9', ['9', '2', '3', '10']),
    ('No número 854, qual é o valor absoluto do algarismo 8 (que ocupa a ordem das centenas)?', '8', ['8', '4', '5', '9']),
    ('No número 5.539, qual é o valor absoluto do algarismo 3 (que ocupa a ordem das dezenas)?', '3', ['3', '5', '9', '4']),
    ('No número 5.539, qual é o valor absoluto do algarismo 9 (que ocupa a ordem das unidades)?', '9', ['9', '3', '5', '10']),

    # Ordens, classes e algarismos (número da prova: 5.539 / número da folha: 1.935)
    ('Quantas ordens tem o número 5.539?', '4', ['4', '2', '5', '3']),
    ('Quantas classes tem o número 5.539?', '2', ['2', '4', '1', '3']),
    ('Quantos algarismos tem o número 5.539?', '4', ['4', '5', '2', '3']),
    ('Trocando os algarismos da 1ª ordem com a 4ª ordem no número 5.539, obtemos:', '9.535', ['9.535', '5.539', '3.559', '9.553']),
    ('Qual é a soma dos valores absolutos dos algarismos de 5.539?', '22', ['22', '21', '23', '18']),
    ('No número 1.935, qual algarismo ocupa a 3ª ordem (centena)?', '9', ['9', '1', '3', '5']),
    ('No número 1.935, qual algarismo ocupa a 4ª ordem (unidade de milhar)?', '1', ['1', '9', '3', '5']),
    ('Com os algarismos de 5.539, qual é o maior numeral que podemos formar?', '9.553', ['9.553', '9.535', '5.539', '3.559']),
    ('Trocarmos a ordem dos algarismos de um número faz com que ele:', 'Mude de valor', ['Mude de valor', 'Continue com o mesmo valor', 'Vire uma fração', 'Vire negativo']),

    # Números ordinais — sequência e vizinhos (folha das formiguinhas)
    ('Qual número ordinal vem imediatamente antes do 23º?', '22º', ['22º', '24º', '21º', '20º']),
    ('Qual número ordinal vem imediatamente depois do 28º?', '29º', ['29º', '27º', '30º', '26º']),
    ('Qual número ordinal vem imediatamente antes do 37º?', '36º', ['36º', '38º', '35º', '39º']),
    ('Qual número ordinal vem imediatamente depois do 16º?', '17º', ['17º', '15º', '18º', '14º']),
    ('Qual número ordinal vem imediatamente antes do 11º?', '10º', ['10º', '12º', '9º', '13º']),
    ('Qual número ordinal vem imediatamente depois do 2º?', '3º', ['3º', '1º', '4º', '5º']),
    ('Se a 5ª formiguinha da fila está ligada à 7ª (2 posições à frente), seguindo o mesmo padrão, a 7ª deve se ligar a qual?', '9ª', ['9ª', '8ª', '10ª', '6ª']),

    # Números ordinais — escrita por extenso (folha das formiguinhas)
    ('Como se escreve por extenso a posição 8º?', 'Oitavo', ['Oitavo', 'Oito', 'Octogésimo', 'Nono']),
    ('Como se escreve por extenso a posição 13º?', 'Décimo terceiro', ['Décimo terceiro', 'Trigésimo', 'Décimo terceira', 'Terceiro']),
    ('Como se escreve por extenso a posição 17º?', 'Décimo sétimo', ['Décimo sétimo', 'Décimo sexto', 'Sétimo', 'Décimo oitavo']),
    ('Como se escreve por extenso a posição 20º?', 'Vigésimo', ['Vigésimo', 'Vinte', 'Décimo', 'Trigésimo']),
    ('Qual numeral ordinal corresponde a "Vigésimo"?', '20º', ['20º', '12º', '2º', '10º']),
    ('Qual numeral ordinal corresponde a "Quadragésimo"?', '40º', ['40º', '14º', '4º', '24º']),
    ('Qual numeral ordinal corresponde a "Quinquagésimo"?', '50º', ['50º', '15º', '5º', '25º']),
    ('Qual numeral ordinal corresponde a "Trigésimo"?', '30º', ['30º', '13º', '3º', '33º']),
    # Valor posicional (números autorais, não usados nas folhas/prova)
    ('No número 4.827, qual é o valor posicional do algarismo 7 (que ocupa a ordem das unidades)?', '7', ['7', '70', '700', '17']),
    ('No número 4.827, qual é o valor posicional do algarismo 2 (que ocupa a ordem das dezenas)?', '20', ['20', '200', '30', '2']),
    ('No número 4.827, qual é o valor posicional do algarismo 8 (que ocupa a ordem das centenas)?', '800', ['800', '80', '810', '900']),
    ('No número 4.827, qual é o valor posicional do algarismo 4 (que ocupa a ordem das unidades de milhar)?', '4.000', ['4.000', '40', '400', '4.010']),
    ('No número 736, qual é o valor posicional do algarismo 3 (que ocupa a ordem das dezenas)?', '30', ['30', '300', '40', '3']),
    ('No número 951, qual é o valor posicional do algarismo 1 (que ocupa a ordem das unidades)?', '1', ['1', '10', '100', '11']),
    ('No número 3.164, qual é o valor posicional do algarismo 3 (que ocupa a ordem das unidades de milhar)?', '3.000', ['3.000', '30', '300', '3.010']),
    ('No número 2.708, qual é o valor posicional do algarismo 7 (que ocupa a ordem das centenas)?', '700', ['700', '70', '710', '800']),

    # Valor absoluto (números autorais, não usados nas folhas/prova)
    ('No número 6.052, qual é o valor absoluto do algarismo 6 (que ocupa a ordem das unidades de milhar)?', '6', ['6', '0', '2', '5']),
    ('No número 483, qual é o valor absoluto do algarismo 8 (que ocupa a ordem das dezenas)?', '8', ['8', '3', '4', '9']),
    ('No número 719, qual é o valor absoluto do algarismo 7 (que ocupa a ordem das centenas)?', '7', ['7', '1', '9', '8']),
    ('No número 8.346, qual é o valor absoluto do algarismo 3 (que ocupa a ordem das centenas)?', '3', ['3', '4', '6', '8']),
    ('No número 275, qual é o valor absoluto do algarismo 5 (que ocupa a ordem das unidades)?', '5', ['5', '2', '7', '6']),
    ('No número 6.827, qual é o valor absoluto do algarismo 8 (que ocupa a ordem das centenas)?', '8', ['8', '2', '6', '7']),
    # Ordens, classes e algarismos (número autoral: 6.827)
    ('Quantas ordens tem o número 6.827?', '4', ['4', '2', '5', '3']),
    ('Quantas classes tem o número 6.827?', '2', ['2', '4', '1', '3']),
    ('Quantos algarismos tem o número 6.827?', '4', ['4', '5', '2', '3']),
    ('Trocando os algarismos da 1ª ordem com a 4ª ordem no número 6.827, obtemos:', '7.826', ['7.826', '6.827', '2.867', '7.862']),
    ('Qual é a soma dos valores absolutos dos algarismos de 6.827?', '23', ['23', '22', '24', '17']),
    ('No número 4.309, qual algarismo ocupa a 3ª ordem (centena)?', '3', ['3', '4', '0', '9']),
    ('No número 4.309, qual algarismo ocupa a 4ª ordem (unidade de milhar)?', '4', ['4', '3', '0', '9']),
    ('Com os algarismos de 6.827, qual é o maior numeral que podemos formar?', '8.762', ['8.762', '7.826', '6.827', '2.678']),
    ('Trocarmos a ordem dos algarismos de um número faz com que ele:', 'Mude de valor', ['Mude de valor', 'Continue com o mesmo valor', 'Vire uma fração', 'Vire negativo']),

    # Números ordinais — sequência e vizinhos (números autorais)
    ('Qual número ordinal vem imediatamente antes do 31º?', '30º', ['30º', '32º', '29º', '28º']),
    ('Qual número ordinal vem imediatamente depois do 44º?', '45º', ['45º', '43º', '46º', '42º']),
    ('Qual número ordinal vem imediatamente antes do 19º?', '18º', ['18º', '20º', '17º', '21º']),
    ('Qual número ordinal vem imediatamente depois do 9º?', '10º', ['10º', '8º', '11º', '12º']),
    ('Qual número ordinal vem imediatamente antes do 25º?', '24º', ['24º', '26º', '23º', '27º']),
    ('Qual número ordinal vem imediatamente depois do 33º?', '34º', ['34º', '32º', '35º', '36º']),
    ('Se a 4ª formiguinha da fila está ligada à 6ª (2 posições à frente), seguindo o mesmo padrão, a 6ª deve se ligar a qual?', '8ª', ['8ª', '7ª', '9ª', '5ª']),

    # Números ordinais — escrita por extenso (números autorais)
    ('Como se escreve por extenso a posição 6º?', 'Sexto', ['Sexto', 'Seis', 'Sexagésimo', 'Sétimo']),
    ('Como se escreve por extenso a posição 15º?', 'Décimo quinto', ['Décimo quinto', 'Quinquagésimo', 'Décimo quinta', 'Quinto']),
    ('Como se escreve por extenso a posição 19º?', 'Décimo nono', ['Décimo nono', 'Décimo oitavo', 'Nono', 'Nonagésimo']),
    ('Como se escreve por extenso a posição 27º?', 'Vigésimo sétimo', ['Vigésimo sétimo', 'Vigésimo sexto', 'Sétimo', 'Trigésimo sétimo']),
    ('Qual numeral ordinal corresponde a "Sexto"?', '6º', ['6º', '16º', '60º', '7º']),
    ('Qual numeral ordinal corresponde a "Décimo quinto"?', '15º', ['15º', '50º', '5º', '14º']),
    ('Qual numeral ordinal corresponde a "Vigésimo sétimo"?', '27º', ['27º', '72º', '17º', '37º']),
    ('Qual numeral ordinal corresponde a "Quadragésimo terceiro"?', '43º', ['43º', '34º', '13º', '44º']),
]

for enunciado, resposta, opcoes in questoes:
    criar_questao(matematica, 'ordinais_valor_abs_pos', enunciado, resposta, opcoes)

total = BancoQuestao.objects.filter(disciplina=matematica, modulo='ordinais_valor_abs_pos').count()
print(f"\n✅ Concluído! Total de questões de Números Ordinais, Valor Absoluto e Posicional: {total}")


# ══════════════════════════════════════════════════════════════════
# LIMPEZA — remove do "Sistema de Numeração" as questões que tinham
# sido colocadas lá por engano antes de decidirmos criar este card
# separado. Só tem efeito se você chegou a rodar o popular_numeracao.py
# com aquela versão intermediária — rodar isto de novo não faz mal.
# ══════════════════════════════════════════════════════════════════
enunciados_para_remover_do_sistema_numeracao = [q[0] for q in questoes]

removidas, _ = BancoQuestao.objects.filter(
    disciplina=matematica,
    modulo='sistema_numeracao',
    enunciado__in=enunciados_para_remover_do_sistema_numeracao,
).delete()

if removidas:
    print(f"\n🧹 Limpeza: removidas {removidas} questões duplicadas que estavam em 'sistema_numeracao'.")
