from django.db import models
from django.contrib.auth.models import User
# from phone_field import PhoneField
# Create your models here.

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_mobile = models.CharField(max_length=10,null=False,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='user_profile'
    
    def __str__(self):
        return "{}".format(self.user)

class roles(models.Model):
    role_name = models.CharField(max_length=20,unique=True)
    user = models.ManyToManyField(User,through='user_roles')
    class Meta:
        db_table='roles'
    def __str__(self):
        return f"Role Name:{self.role_name}"

class user_roles(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey(roles,on_delete=models.CASCADE)
    class Meta:
        db_table='user_roles'