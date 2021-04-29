from django.db import models
from django.db.models.deletion import CASCADE
from prospecting.models import Negociator
from userprofile.models import UserCustomGroup
from user.models import AAUser
# Create your models here.

def get_sentinel_negociator():
    user = AAUser.objects.create(email="deleted@deleted.com", password='deleted')
    userCust = UserCustomGroup.objects.create(label="Negociator")
    negociator, created = Negociator.objects.get_or_create(firstname='DELETED', lastname='DELETED', custom_group=userCust, user=user)
    return negociator


class Property(models.Model) :
  name = models.CharField(
    max_length=255,
  )
  phone = models.CharField(
    max_length=12
  )
  address = models.CharField(
    max_length=255
  )
  endDate = models.DateField(
    verbose_name="Date de fin",
    auto_now_add=True
  )
  price = models.IntegerField(
    verbose_name="prix"
  )
  ref = models.CharField(
    verbose_name="Référence de l'offre",
    max_length=255,
  )
  prospecting = models.BooleanField(
    verbose_name="en prospection"
  )
  negociator = models.ForeignKey(
    Negociator,
    on_delete=models.SET(get_sentinel_negociator),
  )
  ground = models.FloatField(
    verbose_name="surface"
  )
  creation = models.DateField(
    verbose_name="Date de création",
    auto_now_add=True,
  )
  comment = models.CharField(
    verbose_name="commentaire sur l'offre",
    max_length=512
  )

  class Meta : 
    verbose_name = "Prospecté"
    verbose_name_plural = "Prospectés"