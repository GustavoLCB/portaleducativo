from django.db import models
from django.contrib.auth.models import User

class RegistroJogada(models.Model):
    jogador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Estas são as colunas que estavam faltando!
    operacao = models.CharField(max_length=20, default='multiplicacao') 
    nivel = models.CharField(max_length=20, default='unidades')
    
    numero_1 = models.IntegerField()
    numero_2 = models.IntegerField()
    resposta_aluno = models.IntegerField()
    acertou = models.BooleanField()
    tempo_segundos = models.FloatField()
    data_jogada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        resultado = "Acertou" if self.acertou else "Errou"
        return f"{self.operacao} ({self.nivel}): {self.numero_1} e {self.numero_2} | Resp: {self.resposta_aluno} ({resultado})"