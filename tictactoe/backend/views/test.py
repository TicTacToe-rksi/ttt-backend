from django.http import HttpResponse

from backend.models_dir.Challenge import Challenge
from backend.models_dir.Game import Game


def delete(request):
    Challenge.objects.all().delete()
    Game.objects.all().delete()

    return HttpResponse('ok')
