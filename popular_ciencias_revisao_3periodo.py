"""
popular_ciencias_revisao_3periodo.py
----------------------------------------
Execute na raiz do projeto:
    python popular_ciencias_revisao_3periodo.py

Popula o banco com o novo módulo de Ciências:
  - revisao_3periodo (CIEN - Revisão 3º Período)

Baseado no material "Revisão de Ciências" (3º ano, Colégio Santo Agostinho),
cobrindo: ambientes dos animais, alimentação, reprodução, vertebrados x
invertebrados, os 5 grupos de vertebrados, metamorfose e fases da vida
humana.

Mesmo padrão do popular_ciencias.py — pode rodar de novo sem problema,
não duplica questões existentes (usa update_or_create).
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


print("\n🔬 Garantindo disciplina Ciências...")
ciencias, _ = Disciplina.objects.get_or_create(
    nome='ciencias', defaults={'nome_exibicao': 'Ciências'}
)
print("  ✅ Ciências pronta.")


# ══════════════════════════════════════════════════════════════════
# MÓDULO NOVO — REVISÃO 3º PERÍODO
# ══════════════════════════════════════════════════════════════════
print("\n📝 Populando: Ciências › Revisão 3º Período...")

revisao_3periodo = [
    # ── Ambiente em que os animais vivem ──
    ('Animais que vivem na terra firme, como florestas, desertos e campos, habitam um ambiente:', 'Terrestre',
     ['Terrestre', 'Aquático', 'Aéreo', 'Subterrâneo']),
    ('Animais que vivem na água — seja em rios, lagos ou mares — habitam um ambiente:', 'Aquático',
     ['Aquático', 'Terrestre', 'Aéreo', 'Anfíbio']),
    ('Leão, elefante, formiga e cobra são exemplos de animais que vivem em ambiente:', 'Terrestre',
     ['Terrestre', 'Aquático', 'Aéreo', 'Misto']),
    ('Peixe, baleia, polvo e caranguejo são exemplos de animais que vivem em ambiente:', 'Aquático',
     ['Aquático', 'Terrestre', 'Aéreo', 'Subterrâneo']),

    # ── Alimentação ──
    ('Animais que se alimentam de outros animais são chamados de:', 'Carnívoros',
     ['Carnívoros', 'Herbívoros', 'Onívoros', 'Vegetarianos']),
    ('Animais que se alimentam apenas de plantas são chamados de:', 'Herbívoros',
     ['Herbívoros', 'Carnívoros', 'Onívoros', 'Insetívoros']),
    ('Animais que comem tanto plantas quanto carne são chamados de:', 'Onívoros',
     ['Onívoros', 'Herbívoros', 'Carnívoros', 'Fotossintéticos']),
    ('Leão, tubarão e coruja são exemplos de animais:', 'Carnívoros',
     ['Carnívoros', 'Herbívoros', 'Onívoros', 'Ovíparos']),
    ('Vaca, coelho e girafa são exemplos de animais:', 'Herbívoros',
     ['Herbívoros', 'Carnívoros', 'Onívoros', 'Vivíparos']),
    ('Humano, urso e galinha são exemplos de animais:', 'Onívoros',
     ['Onívoros', 'Herbívoros', 'Carnívoros', 'Aquáticos']),

    # ── Reprodução ──
    ('Animais que nascem de ovos são chamados de:', 'Ovíparos',
     ['Ovíparos', 'Vivíparos', 'Onívoros', 'Herbívoros']),
    ('Animais que se desenvolvem dentro da barriga da mãe e nascem já formados são chamados de:', 'Vivíparos',
     ['Vivíparos', 'Ovíparos', 'Carnívoros', 'Terrestres']),
    ('Pássaros, cobras, peixes e tartarugas são exemplos de animais:', 'Ovíparos',
     ['Ovíparos', 'Vivíparos', 'Herbívoros', 'Aquáticos']),
    ('Cães, gatos, baleias e humanos são exemplos de animais:', 'Vivíparos',
     ['Vivíparos', 'Ovíparos', 'Carnívoros', 'Terrestres']),

    # ── Agrupando os animais: vertebrados x invertebrados ──
    ('O principal critério usado pelos cientistas para separar os animais em grandes grupos é a presença ou não de:', 'Coluna vertebral',
     ['Coluna vertebral', 'Pelos', 'Patas', 'Asas']),
    ('Animais que possuem esqueleto interno com coluna vertebral são chamados de:', 'Vertebrados',
     ['Vertebrados', 'Invertebrados', 'Onívoros', 'Ovíparos']),
    ('Insetos, aracnídeos, moluscos, vermes e crustáceos são exemplos de animais:', 'Invertebrados',
     ['Invertebrados', 'Vertebrados', 'Mamíferos', 'Répteis']),
    ('Aproximadamente qual porcentagem das espécies de animais conhecidas na Terra é de invertebrados?', 'Mais de 95%',
     ['Mais de 95%', 'Menos de 10%', 'Exatamente 50%', 'Nenhuma']),

    # ── Vertebrados: os 5 grupos ──
    ('Os animais vertebrados são divididos em quantos grupos (classes)?', '5',
     ['5', '3', '7', '2']),
    ('Animais que têm pelos, são vivíparos e as fêmeas amamentam os filhotes pertencem ao grupo dos:', 'Mamíferos',
     ['Mamíferos', 'Aves', 'Répteis', 'Anfíbios']),
    ('Animais que têm penas, bico e asas, e a maioria voa, pertencem ao grupo das:', 'Aves',
     ['Aves', 'Répteis', 'Mamíferos', 'Peixes']),
    ('Animais que têm escamas, são ovíparos e de sangue frio pertencem ao grupo dos:', 'Répteis',
     ['Répteis', 'Anfíbios', 'Aves', 'Mamíferos']),
    ('Animais que vivem na água e na terra, têm pele úmida e passam por metamorfose pertencem ao grupo dos:', 'Anfíbios',
     ['Anfíbios', 'Répteis', 'Peixes', 'Mamíferos']),
    ('Animais que vivem na água, respiram por brânquias e têm o corpo coberto de escamas pertencem ao grupo dos:', 'Peixes',
     ['Peixes', 'Anfíbios', 'Répteis', 'Aves']),

    # ── Metamorfose ──
    ('A transformação que alguns animais passam ao longo da vida, mudando de forma até chegar à fase adulta, é chamada de:', 'Metamorfose',
     ['Metamorfose', 'Reprodução', 'Digestão', 'Fotossíntese']),
    ('Na metamorfose da borboleta, qual é a primeira fase do ciclo?', 'Ovos',
     ['Ovos', 'Lagarta', 'Pupa', 'Borboleta adulta']),

    # ── Fases da vida do ser humano ──
    ('A fase da vida humana que vai do nascimento até os 12 anos é chamada de:', 'Infância',
     ['Infância', 'Adolescência', 'Fase adulta', 'Velhice']),
    ('A fase da vida humana marcada pela puberdade, entre 12 e 18 anos, é chamada de:', 'Adolescência',
     ['Adolescência', 'Infância', 'Fase adulta', 'Velhice']),
    ('A fase da vida humana em que a pessoa trabalha, se relaciona e pode constituir família, dos 18 aos 60 anos, é chamada de:', 'Fase adulta',
     ['Fase adulta', 'Infância', 'Adolescência', 'Velhice']),
    ('A fase da vida humana que começa a partir dos 60 anos é chamada de:', 'Velhice',
     ['Velhice', 'Infância', 'Adolescência', 'Fase adulta']),
]
for enunciado, resposta, opcoes in revisao_3periodo:
    criar_questao(ciencias, 'revisao_3periodo', enunciado, resposta, opcoes)


# ── RESUMO ──────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("✅ POPULAÇÃO DE CIÊNCIAS › REVISÃO 3º PERÍODO CONCLUÍDA!")
print("=" * 55)
total = BancoQuestao.objects.filter(disciplina=ciencias, modulo='revisao_3periodo').count()
print(f"   {'Revisão 3º Período':.<32} {total}")
