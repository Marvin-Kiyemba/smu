from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .managers import UserManager
from django.contrib.auth.models import Permission
#from . import constants as user_constants

from django.conf import settings
User = settings.AUTH_USER_MODEL
class User(AbstractUser):
    SUPER_USER = 1
    STAFF = 2

    USER_TYPE_CHOICES =(
        (SUPER_USER, 'super_user'),
        (STAFF, 'staff'),
    )


    OPS = 'OPS'
    FIN = 'FIN'
    MEL = 'MEL'
    IT = 'IT'
    GOV_EDUC = 'GOV_EDUC'
    GOVT_HEALTH = 'GOVT_HEALTH'
    TELE = 'TELE'
    CPA = 'CPA'
    NGO = 'NGO'
    HRA = 'HRA'

    DEPARTMENT_CHOICES = (
        ('OPS', 'Operations'),
        ('FIN', 'Finance'),
        ('MEL', 'Monitoring Evaluation and learning'),
        ('IT','IT & DIGITAL PLATFORMS'),
        ('GOV_EDUC', 'Government Education'),
        ('GOVT_HEALTH', 'Government Health'),
        ('TELE', 'Teletherapy'),
        ('CPA', 'Communications Advocacy and Partnerships'),
        ('NGO', 'Non Government Organization'),
        ('HRA', 'Human Resource and Administration'),
    )

    username = None # remove username field, we will use email as unique identifier
    email = models.EmailField(unique=True, null=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="user_profile")
    phone = models.CharField(max_length=255,blank=True,null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email 

class DepartmentAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices=User.DEPARTMENT_CHOICES)

    def __str__(self):
        return self.user.email
 
class ViewOwnDepartmentAdminPermission(Permission):
    codename = 'view_own_departmentadmin'
    name = 'Can view own department admin'

    class Meta:
        proxy = True