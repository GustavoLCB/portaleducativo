from django.db import models
from django.contrib.auth.models import User


class RegistroJogada(models.Model):
    """
    Cada linha aqui = uma resposta que o aluno deu em algum jogo.
    O relatório de desempenho é inteiramente calculado a partir desta tabela.
    """
    jogador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    operacao = models.CharField(max_length=50, default='multiplicacao')
    nivel = models.CharField(max_length=50, default='unidades')

    numero_1 = models.IntegerField(default=0)
    numero_2 = models.IntegerField(default=0)
    resposta_aluno = models.CharField(max_length=200, default='0')
    acertou = models.BooleanField()
    tempo_segundos = models.FloatField()
    data_jogada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        resultado = "Acertou" if self.acertou else "Errou"
        return f"{self.operacao} ({self.nivel}): {self.numero_1} e {self.numero_2} | Resp: {self.resposta_aluno} ({resultado})"


class Disciplina(models.Model):
    """Ex: matemática, português, geografia, história, ciências, inglês."""
    nome = models.CharField(max_length=50, unique=True)
    nome_exibicao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_exibicao


class BancoQuestao(models.Model):
    """
    Banco de questões usado pelos jogos de quiz (Geografia, História,
    Ciências, Sistema de Numeração de Matemática, etc.) — os jogos de
    cálculo (adição/subtração/multiplicação/divisão) não usam esta tabela,
    eles geram os números direto no JavaScript.
    """
    TIPOS = [
        ('multipla_escolha', 'Múltipla Escolha'),
        ('completar_frase', 'Completar Frase'),
        ('vocabulario', 'Vocabulário'),
        ('classificacao', 'Classificação'),
    ]
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    modulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30, choices=TIPOS)
    enunciado = models.TextField()
    resposta_correta = models.CharField(max_length=200)
    dados_extras = models.JSONField(default=dict, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.disciplina}][{self.modulo}] {self.enunciado[:50]}"