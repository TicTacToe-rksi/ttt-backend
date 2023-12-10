import json

from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from backend.dataclasses.responses import Body, Status
from backend.models_dir.Challenge import Challenge
from backend.models_dir.Game import Game
from backend.models_dir.User import User


@csrf_exempt
def challenges_to_me(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    user = User.objects.get(pk=body['self'])

    print(request.path)
    match request.path:
        case '/challenge/me':
            challenge = Challenge.objects.filter(to_user=user).last()
        case '/challenge/my':
            challenge = Challenge.objects.filter(from_user=user).filter(accepted=False)
        case _:
            return JsonResponse(
                data=Body.NOT_FOUND,
                status=Status.NOT_FOUND)

    print(challenge)

    if not challenge:
        return JsonResponse(data=[{}], safe=False, status=Status.OK)
    data = serializers.serialize('json', list(challenge))
    return HttpResponse(
        data,
        status=Status.OK,
        content_type='application/json')


@csrf_exempt
def accept_challenge(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    user = User.objects.get(pk=body['self'])

    challenge_id = body.get('challenge')
    if not challenge_id:
        return JsonResponse(
            data=Body.INVALID_FORM_BODY,
            status=Status.INVALID)

    try:
        challenge = Challenge.objects.get(pk=challenge_id)
    except:
        return JsonResponse(
            data=Body.NOT_FOUND,
            status=Status.NOT_FOUND)

    if challenge.from_user == user:
        return JsonResponse(
            data=Body.FORBIDDEN,
            status=Status.FORBIDDEN)

    challenge.accepted = True
    challenge.save()

    game = Game.create(
        creator=challenge.from_user,
        opponent=challenge.to_user
    )

    data = serializers.serialize('json', [game])
    return HttpResponse(
        data,
        status=Status.OK,
        content_type='application/json')


@csrf_exempt
def send_challenge(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    creator = User.objects.get(pk=body['self'])
    opponent_id = body.get('opponent')

    if not opponent_id:
        return JsonResponse(
            data=Body.INVALID_FORM_BODY,
            status=Status.INVALID)
    try:
        opponent = User.objects.get(pk=opponent_id)
    except:
        return JsonResponse(
            data=Body.NOT_FOUND,
            status=Status.CONFLICT)

    not_finished_challenges = Challenge.objects.filter(from_user=creator)
    if not_finished_challenges:
        return JsonResponse(
            data=Body.FORBIDDEN,
            status=Status.FORBIDDEN
        )

    challenge = Challenge.objects.create(from_user=creator, to_user=opponent)

    return JsonResponse(
        data={"challenge": challenge.pk},
        status=Status.CREATED)


@csrf_exempt
def recall_challenge(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    user_id = body['self']
    challenge_id = body.get('challenge')

    if not challenge_id:
        return JsonResponse(
            data=Body.INVALID_FORM_BODY,
            status=Status.INVALID)

    challenge = Challenge.objects.get(pk=challenge_id)

    if challenge.accepted:
        return JsonResponse(
            data=Body.CAN_NOT_BE_DELETED,
            status=Status.FORBIDDEN)

    user = User.objects.get(pk=user_id)

    if user != challenge.from_user:
        return JsonResponse(
            data=Body.FORBIDDEN,
            status=Status.FORBIDDEN)

    challenge.delete()

    return JsonResponse(
        data=Body.DELETED,
        status=Status.DELETED)
