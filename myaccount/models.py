from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.

class MyUserManager(BaseUserManager):

    def create_user(self,email,name,username,organization,address,phone,password=None):
        if not email:
            raise ValueError("Please enter the valid email address to register yourself")
        user = self.model(
        email= self.normalize_email(email),
        name=name,
        username=username,
        organization=organization,
        address=address,
        phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,name,password=None):
        user = self.model(
        username=username,
        name=name,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Myuser(AbstractBaseUser):
    name =  models.CharField(max_length=50)
    username = models.CharField(max_length=100,unique=True)
    organization = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=False)
    address = models.CharField(max_length=100)
    phone =  models.CharField(max_length=10)
    points = models.IntegerField(null=True)
    password = models.CharField(max_length=30)
    re_password = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    object = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self,app_label):
        return True


    @property

    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


    def get_short_name(self):
        return self.name
