from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin,
)
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator



class AAUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Un utilisateur doit avoir une adresse email')

        user = self.model(email=email, )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email=email, password=password, )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class AAUser(AbstractBaseUser, PermissionsMixin):
    date_created = models.DateTimeField(verbose_name="Date de création", auto_now_add=True, )
    email = models.EmailField(unique=True)
    first_connexion = models.BooleanField(default=True)
    last_connexion = models.DateTimeField(null=True, blank=True)
    first_password = models.CharField(max_length=255, default='firstpwdnotintended')
    token = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    connected_as = models.IntegerField(verbose_name="Connecte en tant que", blank=True, null=True)
    objects = AAUserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.first_password = get_random_string(
                length=4,
                allowed_chars='AZERTYUIOPQSDFGHJKLMWXCVBN123456789'
            ) + '-' + get_random_string(
                length=4,
                allowed_chars='AZERTYUIOPQSDFGHJKLMWXCVBN123456789'
            ) + '-' + get_random_string(
                length=4,
                allowed_chars='AZERTYUIOPQSDFGHJKLMWXCVBN123456789'
            )
        if self.pk:
            self.token = get_random_string(
                    length=128,
                    allowed_chars='1234567890azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN'
            )
        super(AAUser, self).save(*args, **kwargs)


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin