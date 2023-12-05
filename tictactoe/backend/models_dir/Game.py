from django.db import models

from backend.models_dir.User import User


class Game(models.Model):
    size = models.SmallIntegerField(null=False)
    members = models.ManyToManyField(User, related_name='games')
    area = models.TextField()
    finished = models.BooleanField(default=False, null=False)

    def __str__(self):
        return 'Game#{id} | {members}'.format(
            id=self.pk,
            members=' VS '.join(self.members))
