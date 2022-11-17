from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.





class CustomeUserManager(BaseUserManager):
    """Manager for the CustomeUserManager"""
    def  create_user(self,name,email,password=None):
        "Create a new user profile"
        if not email:
            raise ValueError("Email must be defined")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        """create and save the superuser"""
        user=self.create_user(name,email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class CustomeUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=250)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects=CustomeUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']


    def __str__(self):
        return self.name