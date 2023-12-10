import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from backend.dataclasses.responses import *
from backend.models_dir.Game import Game
from backend.models_dir.User import User


@csrf_exempt
def get_current(request):
    if request.method != 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST)

    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    user_id = body['self']
    user = User.objects.get(pk=user_id)

    game = Game.get_current(user)

    data = serializers.serialize('game', game)

    return HttpResponse(
        data,
        status=Status.OK,
        content_type='application/json')
