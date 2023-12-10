from django.urls import path

from backend.views.auth import *
from backend.views.game import *
from backend.views.challenge import *
from backend.views.user import *
from backend.views.test import delete

urlpatterns = [
    path('auth/register', register),
    path('auth/login', login),
    path('challenge/me', challenges_to_me),
    path('challenge/my', challenges_to_me),
    path('challenge/accept', accept_challenge),
    path('challenge/send', send_challenge),
    path('challenge/recall', recall_challenge),
    path('game/current', get_current),
    path('user/exists/', user_exists),
    path('user/get_empty', get_empty_user),
    path('delete', delete),
]
