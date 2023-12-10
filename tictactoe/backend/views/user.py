import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from backend.dataclasses.responses import Body, Status
from backend.models_dir.User import User


@csrf_exempt
def get_empty_user(request):
    if request.method != 'POST':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST)

    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    username = body.get('username')

    print(body)

    if not username:
        return JsonResponse(
            data=Body.INVALID_FORM_BODY,
            status=Status.INVALID)

    try:
        user = User.objects.get(username=username)
    except:
        return JsonResponse(
            data=Body.NOT_FOUND,
            status=Status.NOT_FOUND
        )

    return JsonResponse(
        data={
            'id': user.pk,
            'username': user.username
        },
        status=Status.OK)


def user_exists(request):
    if request.method != 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST)

    body = request.GET

    username = body.get('username')

    if not username:
        return JsonResponse(
            data=Body.INVALID_FORM_BODY,
            status=Status.INVALID)

    if User.exists(username):
        return JsonResponse(
            data={'exists': True},
            status=Status.OK)

    return JsonResponse(
        data={'exists': False},
        status=Status.OK)
