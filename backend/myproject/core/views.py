#from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

from .models import User, Departamento

class UserViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides `list` and `detail` actions.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Recupera a lista de usuarios
@csrf_exempt
def getUsers(request):
    users_list = get_list_or_404(User)
    #return render(request, 'get_user.html', context)
    data = serializers.serialize('json', users_list)
    #return JsonResponse(users_list)
    return HttpResponse(data, content_type="application/json")

# Recuperar e atualizar um usuario a partir do id
@csrf_exempt
def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'GET':
        return JsonResponse({'nome': user.nome, 'idade': user.idade, 'funcao': user.funcao, 'departamento': user.departamento.pk})
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user.nome = body["nome"]
        user.idade = body["idade"]
        user.funcao = body["funcao"]
        dpt = get_object_or_404(Departamento, pk=body["departamento"])
        user.departamento = dpt
        user.save()
    elif request.method == 'DELETE':
        user.delete()
    else: 
         raise Http404
    return JsonResponse({'message': 'Success'})


@csrf_exempt
def createUser(request):
    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    dpt = get_object_or_404(Departamento, pk=body["departamento"])
    user = User(nome = body["nome"], funcao = body["funcao"], idade = body["idade"], departamento = dpt)
    user.save()
    return JsonResponse({'message': 'Success'})

@csrf_exempt
def getDepartamentos(request):
    departamento_list = get_list_or_404(Departamento)
    
    data = serializers.serialize('json', departamento_list)

    return HttpResponse(data, content_type="application/json")