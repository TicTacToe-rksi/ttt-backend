import json

from django.db import models

from backend.logic.tictactoe import TicTacToe
from backend.models_dir.Game import Game
from backend.models_dir.User import User


class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False, related_name='moves')
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    line = models.SmallIntegerField()
    column = models.SmallIntegerField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{game} {member} {to_pos}'.format(
            game=self.game.pk,
            member=self.member,
            to_pos='line: {} column: {}'.format(
                self.to_position.split()[0],
                self.to_position.split()[1]))

    def create(self, game: Game, user: User, position: tuple | list):
        if game.is_finished:
            return

        last_move = game.moves.objects.order_by('-timestamp').first()
        if last_move.member == user:
            return

        ttt = TicTacToe(json.loads(str(game.area)))
        c_or_z = game.cross_or_zero(user)

        new_area = ttt.move(c_or_z, *position)

        if not new_area:
            return

        self.objects.create(
            game=game,
            member=user,
            line=position[0],
            column=position[1]
        )

        filled = ttt.filled
        winner = ttt.winner
        if not winner is None:
            game.is_finished = True
            match winner:
                case 0:
                    game.winner = game.zero
                case 1:
                    game.winner = game.cross

        if filled and winner is None:
            game.is_finished = True
            game.is_drawn = True

        game.save()
        return game
