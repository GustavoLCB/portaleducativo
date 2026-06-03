import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RegistroJogada

def index(request):
    return render(request, 'jogo.html')

# O csrf_exempt permite que o Javascript envie os dados de forma simplificada
@csrf_exempt
def salvar_jogada(request):
    if request.method == 'POST':
        try:
            # Recebe o pacote de dados enviado pelo Javascript
            dados = json.loads(request.body)
            
            # Salva no banco de dados usando o modelo que você criou
            RegistroJogada.objects.create(
                numero_1=dados['numero_1'],
                numero_2=dados['numero_2'],
                resposta_aluno=dados['resposta_aluno'],
                acertou=dados['acertou'],
                tempo_segundos=dados['tempo_segundos']
            )
            return JsonResponse({'status': 'sucesso'})
        except Exception as e:
            return JsonResponse({'status': 'erro', 'mensagem': str(e)})
            
    return JsonResponse({'status': 'metodo_invalido'})