# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db import models

#Create your models here.


class loginInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255, unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'username'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

#     # groups = models.ManyToManyField(
#     #     Group,
#     #     blank=True,
#     #     related_name='user_management_users',
#     #     verbose_name=('groups'),
#     #     help_text=(
#     #         'The groups this user belongs to. A user will get all permissions '
#     #         'granted to each of their groups.'
#     #     ),
#     #     related_query_name='user_management_user',
#     # )

#     # user_permissions = models.ManyToManyField(
#     #     Permission,
#     #     blank=True,
#     #     related_name='user_management_users',
#     #     verbose_name=('user permissions'),
#     #     help_text=('Specific permissions for this user.'),
#     #     related_query_name='user_management_user',
#     # )

#     def __str__(self):
#         return self.username