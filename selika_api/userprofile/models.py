from enum import unique
from django.db import models
from user.models import AAUser


class UserCustomGroup(models.Model):
    date_created = models.DateTimeField(
        verbose_name="Date de création",
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name="Date de modification",
        auto_now=True
    )
    label = models.CharField(
        verbose_name="Nom du groupe",
        max_length=255
    )

    class Meta:
        ordering = ['label']
        verbose_name = "Groupe de l'utilisateur"
        verbose_name_plural = "Groupes de l'utilisateur"

    def __str__(self):
        return self.label


class UserProfile(models.Model):
    date_created = models.DateTimeField(
        verbose_name="Date de création",
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name="Date de modification",
        auto_now=True
    )
    user = models.OneToOneField(
        AAUser,
        related_name="userprofile",
        on_delete=models.CASCADE
    )
    custom_group = models.ForeignKey(
        UserCustomGroup,
        related_name="userprofiles",
        on_delete=models.PROTECT
    )
    lastname = models.CharField(
        verbose_name="Prénom",
        max_length=255,
        unique=False
    )
    firstname = models.CharField(
        verbose_name="Nom",
        max_length=255,
        unique=False
    )

    class Meta:
        ordering = ['firstname']
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.firstname + ' ' + self.lastname