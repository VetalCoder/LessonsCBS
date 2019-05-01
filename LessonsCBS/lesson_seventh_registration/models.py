from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Adding additional info for users via creating another model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)