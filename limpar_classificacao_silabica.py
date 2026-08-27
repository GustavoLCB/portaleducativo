"""
Script para localizar e remover questões erradas/duplicadas do módulo
'classificacao_silabica' em Português.

COMO USAR:
1) Rode este script primeiro (ele só LISTA, não apaga nada).
2) Confira no terminal se as questões listadas são exatamente as erradas
   que você quer remover.
3) Se estiver tudo certo, mude EXECUTAR_DELETE para True (lá embaixo) e
   rode de novo — aí sim ele apaga.
4) Rode local primeiro. Depois, repita o mesmo processo no PythonAnywhere
   (git pull -> rodar este script lá também), porque os bancos de dados
   são separados.

Rodar com: python limpar_classificacao_silabica.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import BancoQuestao

# Trechos bem distintivos das questões erradas (não precisa ser a frase
# inteira, só um pedaço que só aparece nelas).
TRECHOS_ERRADOS = [
    'EMBAI',      # EMBAI___ADA
    'DE___ER',    # DE___ER
    '___ARRAFA',  # ___ARRAFA
    'PROFE___OR', # PROFE___OR
]

MODULO = 'classificacao_silabica'

# ── FASE 1: LISTAR (sempre roda) ──────────────────────────────────────
print("=" * 70)
print("Questões encontradas no módulo 'classificacao_silabica':")
print("=" * 70)

encontrados = []
for trecho in TRECHOS_ERRADOS:
    qs = BancoQuestao.objects.filter(modulo=MODULO, enunciado__icontains=trecho)
    for q in qs:
        encontrados.append(q)
        print(f"\n[ID {q.id}] trecho buscado: '{trecho}'")
        print(f"  Enunciado atual: {q.enunciado}")
        print(f"  Resposta certa : {q.resposta_correta}")
        print(f"  Opções         : {q.dados_extras.get('opcoes')}")

if not encontrados:
    print("\nNenhuma questão encontrada com esses trechos.")
    print("Isso pode significar que:")
    print("  - elas já foram corrigidas/substituídas corretamente, ou")
    print("  - o texto no banco é diferente do esperado (confira manualmente")
    print("    no admin do Django: /admin/core/bancoquestao/).")

print("\n" + "=" * 70)
print(f"Total encontrado: {len(encontrados)} questão(ões)")
print("=" * 70)

# ── FASE 2: DELETAR (só roda se você mudar para True abaixo) ─────────
EXECUTAR_DELETE = False  # <-- mude para True quando confirmar a lista acima

if EXECUTAR_DELETE:
    ids_para_apagar = [q.id for q in encontrados]
    apagados, _ = BancoQuestao.objects.filter(id__in=ids_para_apagar).delete()
    print(f"\n🗑️  {apagados} registro(s) apagado(s) com sucesso.")
else:
    print("\n⚠️  EXECUTAR_DELETE está False — nada foi apagado.")
    print("Revise a lista acima, e se estiver certa, mude EXECUTAR_DELETE")
    print("para True neste arquivo e rode o script de novo.")
