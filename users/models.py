from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    zoom = models.CharField(_('zoom'),max_length=255)
    role = models.CharField(max_length=255)
    fpo_name = models.CharField(max_length=255)
    delete_status = models.BooleanField(default=1)
    phone_number=models.CharField(max_length=10)
    image = models.ImageField(upload_to='user_profile/', null=True)

    def __str__(self):
        return self.email

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class ForgetPassMailVerify(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    link=models.CharField(max_length=500)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class FpoEmailVerify(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    link = models.CharField(max_length=500)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.user