import json

from django.http import JsonResponse

from backend.dataclasses.responses import Body, Status
from backend.models_dir.User import UserForm, User


def register(request):
    if request.method != 'POST':
        return JsonResponse(
            body=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST)

    try:
        body = json.loads(request.body.decode('utf-8'))
    except:
        body = request.POST

    username = body.get('username')
    password = body.get('password')

    form = UserForm(body)
    if not form.is_valid():
        return JsonResponse(
            body=Body.INVALID_FORM_BODY,
            status=Status.CONFLICT)

    user = form.save(commit=False)
    user.password = User.make_password(user.password)
    user.save()

    return JsonResponse(
        body=Body.CREATED,
        status=Status.OK)
