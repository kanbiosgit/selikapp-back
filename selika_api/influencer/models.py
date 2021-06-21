from django.db import models

# Create your models here.

class Influencer(models.Model) :
  lastname = models.CharField(
    max_length=255,
    default="test"
  )
  firstname = models.CharField(
    max_length=255,
    default="test"
  )
  phone = models.CharField(
    max_length=12
  )
  email = models.EmailField(default="test@test.fr")
  creation = models.DateField(
    verbose_name="Date de création",
    auto_now_add=True,
  )
  comment = models.CharField(
    max_length=1024
  )
  lat = models.FloatField(
    verbose_name="latitude"
  )
  lng = models.FloatField(
    verbose_name="longitude"
  )