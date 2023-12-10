from django.db import models

from backend.models_dir.User import User


class Challenge(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_battle_requests')
    to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='received_battle_requests')

    accepted = models.BooleanField(default=False)

