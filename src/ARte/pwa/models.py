from django.db import models
from django.conf import settings
from boogie.apps.users.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    email = models.EmailField(
        'Email address',
        unique=True,
        help_text='Your e-mail address'
    )

    objects = UserManager()

    @property
    def username(self):
        self.email.replace('@', '_')

# class Profile(models.Model):
#     """
#     User profile.
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='raw_profile')


class Exhibition(models.Model):
    author = models.ForeignKey(
        'User',
        related_name='exhibitions',
        on_delete=models.PROTECT
    )
    name = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    artworks = models.ManyToManyField('Artwork', related_name='artworks')


class Artwork(models.Model):
    name = models.CharField(max_length=50)
    marker = models.ForeignKey(
        'Marker',
        related_name='artworks',
        on_delete=models.PROTECT
    )
    art = models.ForeignKey(
        'Art',
        related_name='artworks',
        on_delete=models.PROTECT
    )
    art_scale = models.CharField(default="1 1", max_length=50)
    art_position = models.CharField(default="0 0 0", max_length=50)
    art_rotation = models.CharField(default="270 0 0", max_length=50)


class Marker(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="markers/")
    patt = models.FileField(upload_to="patts/")


class Art(models.Model):
    name = models.CharField(max_length=50)
    source = models.FileField(upload_to="arts/")