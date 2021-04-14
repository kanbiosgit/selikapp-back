from django.db import models
from django.db.models.deletion import CASCADE
from userprofile.models import UserProfile

# Create your models here.

class Negociator(UserProfile) :
  color = models.CharField(max_length=10, default="black")

  class Meta :
    verbose_name = "Négociateur"
    verbose_name_plural = "Négociateurs"

class Map(models.Model) :
  creation = models.DateField(
    auto_now_add=True
  )
  archived = models.BooleanField(
    default=False
  )

  class Meta :
    verbose_name = "Map"
    verbose_name_plural = "Maps"


class Route(models.Model):
  negociator = models.ForeignKey(
    Negociator,
    on_delete=CASCADE
  )
  map = models.ForeignKey(
    Map,
    on_delete=CASCADE
  )
  date = models.DateField(
    auto_now_add=True
  )
  startLat = models.FloatField(
    verbose_name="Point de départ lattitude"
  )
  startLng = models.FloatField(
    verbose_name="Point de départ longitude"
  )
  endLat = models.FloatField(
    verbose_name="Point d'arrivé lattitude"
  )
  endLng = models.FloatField(
    verbose_name="point d'arrivé longitude"
  )

  class Meta : 
    verbose_name = "Route"
    verbose_name_plural = "Routes"