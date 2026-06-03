from django.contrib import admin
from .models import RegistroJogada

# Isso cria uma visualização organizada em colunas no painel
class RegistroJogadaAdmin(admin.ModelAdmin):
    list_display = ('numero_1', 'numero_2', 'resposta_aluno', 'acertou', 'tempo_segundos', 'data_jogada')
    list_filter = ('acertou', 'numero_1', 'numero_2')

admin.site.register(RegistroJogada, RegistroJogadaAdmin)