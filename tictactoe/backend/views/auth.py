import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend.dataclasses.responses import Body, Status
from backend.models_dir.User import UserForm, User


@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST)

    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    username = body.get('username')
    password = User.make_password(body.get('password'))

    form = UserForm(body)
    if not form.is_valid():
        return JsonResponse(
            data=Body.INVALID_FORM_BODY,
            status=Status.CONFLICT)

    User(
        username=username,
        password=password
    ).save()

    return JsonResponse(
        data=Body.CREATED,
        status=Status.OK)


@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST)

    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    username = body.get('username')
    password = body.get('password')

    user = User.login(username, password)

    if not user:
        return JsonResponse(
            data=Body.AUTHORIZED_FALSE,
            status=Status.UNAUTHORIZED)

    return JsonResponse(
        data=Body.AUTHORIZED_TRUE,
        status=Status.OK)
