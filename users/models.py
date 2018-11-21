from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    #ampliacion del modelo de usuario para campos especiales
    is_member = models.BooleanField(default=False)
    is_executive = models.BooleanField(default=False)
    is_operative = models.BooleanField(default=False)

    def __str__(self):
        return self.email