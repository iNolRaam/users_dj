from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    username = models.CharField('Nombre de usuario',
                                max_length=10,
                                unique=True)
    email = models.EmailField('Correo', max_length=50)
    first_name = models.CharField('Primer nombre', max_length=30, blank=True)
    second_name = models.CharField('Segundo nombre', max_length=30, null=True, blank=True)
    first_last_name = models.CharField('Primer apellido', max_length=30, blank=True)
    second_last_name = models.CharField('Segundo apellido',
                                        max_length=30,
                                        null=True,
                                        blank=True)
    gender = models.CharField('Género',
                              max_length=1,
                              choices=GENDER_CHOICES,
                              blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
    
    objects = UserManager()

    class Meta:
        """Meta definition for User."""
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'

def get_short_name(self):
    return self.username

def get_full_name(self):

    full_name = self.first_name

    if self.second_name and self.second_name != '':
            full_name += ' ' + self.second_name

    full_name += ' ' + self.first_last_name

    if self.second_last_name and self.second_last_name != '':
            full_name += ' ' + self.second_last_name

    return full_name

def __str__(self):
    return str(self.id) + ' ' + get_short_name()
