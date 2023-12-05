from hashlib import sha256

from django.db import models
from django.forms import forms


class User(models.Model):
    username = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=64, null=False)

    friends = models.ManyToManyField('self', null=False, symmetrical=True)

    def __str__(self):
        return self.username

    @classmethod
    def login(cls, username: str, password: str):
        try:
            user = User.objects.get(username=username.strip())
        except:
            return None

        if user.password != cls.make_password(password):
            return None

        return user

    @classmethod
    def make_password(cls, password: str):
        return sha256(
            password.strip().encode('utf-8')
        ).hexdigest()


class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password')
