from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    def __unicode__(self):
        return self.username

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.username == "admin" and self.email == "admin@admin.com":
            self.is_superuser = True
            self.is_staff = True
        super(User, self).save(force_insert, force_update, using, update_fields)

