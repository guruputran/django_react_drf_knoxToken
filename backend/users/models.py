from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from django.conf import settings
 
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
    (1, 'superadmin'),
    (2, 'admin'),
    (3, 'normaluser'),
)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, default= 3)
    isNormalUser = models.BooleanField(default=True)
    isAdminUser = models.BooleanField(default=False)
    isSuperUser = models.BooleanField(default=False)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

    


  
