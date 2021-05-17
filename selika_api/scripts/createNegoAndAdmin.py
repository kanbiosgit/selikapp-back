from user.models import AAUser
from userprofile.models import UserProfile, UserCustomGroup
from prospecting.models import Negociator


def run():
  negociatorUser = AAUser.objects.create_superuser(email="negociateur.selika@selika.fr", password="selikaApp")

  admin = AAUser.objects.create_superuser(email="admin.selika@selika.fr", password="selikaApp")


  negociatorCustomGroup = UserCustomGroup.objects.create(label="Negociator")
  adminCustomGroup = UserCustomGroup.objects.create(label="Admin")
  negociatorUserProfile, created = Negociator.objects.get_or_create(firstname="Negociateur", lastname="Negociateur", custom_group=negociatorCustomGroup, user=negociatorUser, color="#b13939")
  adminUserProfile, created = UserProfile.objects.get_or_create(firstname="Admin", lastname="Admin", custom_group=adminCustomGroup, user=admin)

  negociatorUserProfile.save()
  adminUserProfile.save()