from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .utils import ChoiceEnum
# Create your models here.
#Reference
'''
Tabian, M. [CodingWithMitch]. (2019, June 20) Creating a Custom User Model (Django). []. 
Retrieved July, 20, 2020, from https://www.youtube.com/watch?v=eCeRC7E8Z7Y 
'''
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username.")
        if not firstname:
            raise ValueError("Users must have a first name.")
        if not lastname:
            raise ValueError("Users must have a last name.")
            
        user = self.model(
                email = self.normalize_email(email),
                username = username,
                firstname = firstname,
                lastname = lastname,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, username, firstname, lastname, password):
        user = self.create_user(
                email = self.normalize_email(email),
                username = username,
                firstname = firstname,
                lastname = lastname,
                password = password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

#Reference
'''
Tabian, M. [CodingWithMitch]. (2019, June 20) Creating a Custom User Model (Django). []. 
Retrieved July, 20, 2020, from https://www.youtube.com/watch?v=eCeRC7E8Z7Y 
'''        
class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    firstname       = models.CharField(max_length=20)
    lastname        = models.CharField(max_length=20)
    
    class RosterSide(ChoiceEnum):
    		A = 'A'
    		B = 'B'
    		
    roster_side = models.CharField(max_length=5, choices=RosterSide.choices(), default='None')
    current_leave_total = models.FloatField(default=250.00)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.firstname + " " + self.lastname
        
    def has_perm(self, perm, obj=None):
        return self.is_admin
        
    def has_module_perms(self, app_label):
        return True
        
    def get_short_name(self):
        return self.firstname
