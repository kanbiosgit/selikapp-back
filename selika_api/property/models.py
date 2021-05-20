from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from prospecting.models import Negociator
from userprofile.models import UserCustomGroup, UserProfile
from user.models import AAUser
from datetime import datetime
# Create your models here.

def get_sentinel_negociator():
    user = AAUser.objects.get(email="deleted@deleted.com")
    if user is None :
      user = AAUser.objects.create(email="deleted@deleted.com", password='deleted')
      userCust = UserCustomGroup.objects.create(label="Negociator")
      negociator, created = Negociator.objects.get_or_create(firstname='DELETED', lastname='DELETED', custom_group=userCust, user=user)
    else :
      userProfile = UserProfile.objects.get(user=user)
      negociator, created = Negociator.objects.get_or_create(firstname='DELETED', lastname='DELETED', custom_group=userProfile.custom_group, user=user)
    return negociator

def get_sentinel_property():
  return Property.objects.last()


class Property(models.Model) :
  name = models.CharField(
    max_length=255,
  )
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
  address = models.CharField(
    max_length=255
  )
  email = models.EmailField(default="test@test.fr")
  endDate = models.DateField(
    verbose_name="Date de fin",
    default=datetime.now().replace(year = datetime.now().year + 1).date()
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
  support = models.CharField(
    max_length=255,
    default="SeLoger"
  )
  lat = models.FloatField(
    verbose_name="latitude"
  )
  lng = models.FloatField(
    verbose_name="longitude"
  )

  class Meta : 
    verbose_name = "Prospecté"
    verbose_name_plural = "Prospectés"

class Comment(models.Model) :
  creation = models.DateField(
    auto_now_add=True
  )

  text = models.CharField(
    max_length=1024
  )

  property = models.ForeignKey(
    Property,
    on_delete=CASCADE
  )