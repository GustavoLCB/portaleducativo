from django.contrib import admin
from .models import RegistroJogada, Disciplina, BancoQuestao


@admin.register(RegistroJogada)
class RegistroJogadaAdmin(admin.ModelAdmin):
    list_display = ('jogador', 'operacao', 'nivel', 'numero_1', 'numero_2',
                     'resposta_aluno', 'acertou', 'tempo_segundos', 'data_jogada')
    list_filter = ('operacao', 'nivel', 'acertou', 'data_jogada')
    search_fields = ('jogador__username', 'jogador__first_name', 'operacao', 'nivel')
    list_select_related = ('jogador',)
    ordering = ('-data_jogada',)


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_exibicao')


@admin.register(BancoQuestao)
class BancoQuestaoAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'modulo', 'tipo', 'enunciado_curto', 'resposta_correta', 'ativo')
    list_filter = ('disciplina', 'modulo', 'tipo', 'ativo')
    search_fields = ('enunciado', 'resposta_correta')

    def enunciado_curto(self, obj):
        return obj.enunciado[:60]
    enunciado_curto.short_description = 'Enunciado'