from django.db import models
from django.contrib.auth.models import User

class RegistroJogada(models.Model):
    # Por enquanto deixamos o usuário opcional (null=True) para podermos testar o jogo antes de criar a tela de login
    jogador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    numero_1 = models.IntegerField()
    numero_2 = models.IntegerField()
    resposta_aluno = models.IntegerField()
    acertou = models.BooleanField()
    tempo_segundos = models.FloatField()
    data_jogada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        resultado = "Acertou" if self.acertou else "Errou"
        return f"{self.numero_1} x {self.numero_2} | Resposta: {self.resposta_aluno} ({resultado})"