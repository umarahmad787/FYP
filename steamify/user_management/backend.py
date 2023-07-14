from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db import connection

# class XamppAuthBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", [username, password])
#                 row = cursor.fetchone()
#                 if row:
#                     user = UserModel.objects.get(username=username)
#                     return user
#         except UserModel.DoesNotExist:
#             return None