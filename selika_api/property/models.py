from django.db import models
from django.db.models.deletion import CASCADE
from prospecting.models import Negociator

# Create your models here.


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
    on_delete=CASCADE,
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