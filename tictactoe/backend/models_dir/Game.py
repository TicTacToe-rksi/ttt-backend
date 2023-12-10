import json

from django.db import models
from django.db.models import Q

from backend.logic.tictactoe import TicTacToe
from backend.models_dir.User import User


class Game(models.Model):
    cross = models.ForeignKey(User, related_name='cross_games', on_delete=models.SET_NULL, null=True)
    zero = models.ForeignKey(User, related_name='zero_games', on_delete=models.SET_NULL, null=True)
    area = models.CharField(
        max_length=60,
        default=json.dumps(TicTacToe.board()),
        null=False)
    is_finished = models.BooleanField(default=False, null=True)
    is_drawn = models.BooleanField(default=False, null=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='won_games')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Game#{id} | {members}'.format(
            id=self.pk,
            members=' VS '.join(self.members))

    @classmethod
    def create(cls, creator: User, opponent: User):
        for user in creator, opponent:
            in_game = cls.get_current(user)
            if in_game:
                return

        game = Game.objects.create(
            cross=creator,
            zero=opponent
        )

        return game

    def cross_or_zero(self, user: User) -> int:
        match user:
            case self.cross:
                return 1
            case self.zero:
                return 0

    @classmethod
    def get_current(cls, user: User):
        game = Game.objects.filter(Q(cross=user) | Q(zero=user)).filter(is_finished=False).first()
        return game
