from django.db import models

from backend.models_dir.Game import Game
from backend.models_dir.User import User


class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=False)

    to_position = models.CharField(max_length=3)

    def __str__(self):
        return '{game} {member} {to_pos}'.format(
            game=self.game.pk,
            member=self.member,
            to_pos='line: {} column: {}'.format(
                self.to_position.split()[0]+1,
                self.to_position.split()[1]+1))
