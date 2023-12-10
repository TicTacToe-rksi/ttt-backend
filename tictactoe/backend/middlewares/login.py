import json

from django.http import JsonResponse

from backend.dataclasses.responses import Status, Body
from backend.models_dir.User import User


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.paths = ('challenge/send', 'challenge/me', 'challenge/my',
                      'challenge/accept', 'challenge/send', 'game/current',
                      'user/exists', 'challenge/recall')

    def __call__(self, request):
        print('Request path:', request.path)

        if request.path in self.paths:
            if request.method != 'POST':
                return JsonResponse(
                    data=Body.BAD_REQUEST,
                    status=Status.BAD_REQUEST)

            try:
                body = json.loads(request.body.decode('utf-8'))
            except:
                body = request.POST

            id = body.get('self')
            password = body.get('password')

            print(not (id and id is int) and not (password and password is str))

            if not (id and id is int) and not (password and password is str):
                return JsonResponse(
                    data=Body.INVALID_FORM_BODY,
                    status=Status.INVALID
                )

            user = User.login_by_id(id, password)
            if not user:
                return JsonResponse(
                    data=Body.AUTHORIZED_FALSE,
                    status=Status.UNAUTHORIZED
                )
            elif request.path == '/auth/login':
                return JsonResponse(
                    data=Body.AUTHORIZED_TRUE,
                    status=Status.OK
                )
        response = self.get_response(request)
        return response
