from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserAccountManager(BaseUserManager):
  def create_user(self, username, email, password, name, **extra_fields):
    user = self.model(username=username, email=self.normalize_email(email), name=name, **extra_fields)
    user.set_password(password)
    user.save()
    return user
  def create_superuser(self, username, email, password, name, **extra_fields):
    user = self.create_user(username=username,email=email,password=password, name=name, is_staff=True, is_superuser=True, **extra_fields)
    return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100, unique=True)
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=200, unique=True)
  phone = models.CharField(max_length=20)
  created = models.DateTimeField(auto_now_add=True, auto_now=False)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserAccountManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ('username', 'name')

  def __str__(self):
    return self.email


