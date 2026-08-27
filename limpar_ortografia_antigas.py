"""
Remove as 4 questões ANTIGAS e erradas do módulo 'ortografia' que ficaram
esquecidas no banco depois que o enunciado delas foi corrigido no script
(o update_or_create não apaga a versão antiga quando o texto do enunciado
muda — ele cria uma nova e deixa a velha lá).

COMO USAR:
1) Rode este script primeiro (ele só LISTA o que vai apagar).
2) Confira se bate exatamente com as 4 questões erradas.
3) Mude EXECUTAR_DELETE para True e rode de novo para apagar de verdade.
4) Rode local primeiro. Depois repita no PythonAnywhere (git pull -> rodar
   lá também), já que os bancos são separados.

Rodar com: python limpar_ortografia_antigas.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import BancoQuestao

MODULO = 'ortografia'

# Texto EXATO das questões antigas e erradas (confirmado por Gustavo)
ENUNCIADOS_ANTIGOS = [
    'EMBAI___ADA (a bola ficou embai___ada)',
    'DE___ER (é gostoso o de___er de chocolate)',
    '___ARRAFA (a ___arrafa é um animal alto)',
    'PROFE___OR (o ___ da turma é gentil)',
]

# ── FASE 1: LISTAR (sempre roda) ──────────────────────────────────────
print("=" * 70)
print("Procurando as questões antigas/erradas no módulo 'ortografia'...")
print("=" * 70)

encontrados = list(
    BancoQuestao.objects.filter(modulo=MODULO, enunciado__in=ENUNCIADOS_ANTIGOS)
)

if not encontrados:
    print("\nNenhuma encontrada com o texto exato esperado.")
    print("Pode ser que o texto no banco tenha alguma diferença sutil")
    print("(espaço, acento, quantidade de '_'). Confira no admin:")
    print("  /admin/core/bancoquestao/  (filtre por módulo = ortografia)")
else:
    for q in encontrados:
        print(f"\n[ID {q.id}]")
        print(f"  Enunciado: {q.enunciado}")
        print(f"  Resposta : {q.resposta_correta}")
        print(f"  Opções   : {q.dados_extras.get('opcoes')}")

print("\n" + "=" * 70)
print(f"Total encontrado: {len(encontrados)} de {len(ENUNCIADOS_ANTIGOS)} esperado(s)")
print("=" * 70)

# ── FASE 2: DELETAR (só roda se você mudar para True abaixo) ─────────
EXECUTAR_DELETE = True  # <-- mude para True quando confirmar a lista acima

if EXECUTAR_DELETE:
    ids_para_apagar = [q.id for q in encontrados]
    apagados, _ = BancoQuestao.objects.filter(id__in=ids_para_apagar).delete()
    print(f"\n🗑️  {apagados} registro(s) apagado(s) com sucesso.")
else:
    print("\n⚠️  EXECUTAR_DELETE está False — nada foi apagado ainda.")
    print("Revise a lista acima. Se estiver certa, mude EXECUTAR_DELETE")
    print("para True neste arquivo e rode de novo.")
