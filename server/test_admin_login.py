import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

client = Client()
login_success = client.login(username='admin', password='adminpassword123')
print(f"Django Admin Login Success: {login_success}")

response = client.get('/admin/auth/user/')
print(f"Admin Users page status code: {response.status_code}")
if response.status_code == 200:
    print("Successfully accessed AUTHENTICATION AND AUTHORIZATION -> Users page in Django Admin!")
