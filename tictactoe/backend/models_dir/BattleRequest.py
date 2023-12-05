from django.db import models

from backend.models_dir.User import User


class BattleRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sent_battle_requests')
    to_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='received_battle_requests')

    size = models.SmallIntegerField()
