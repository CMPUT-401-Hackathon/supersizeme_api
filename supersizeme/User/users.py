from django.contrib.auth.models import User
import requests

data = {
  "username": "user",
  "password": "pass",
}

URL = 'http://example.com'
r = requests.post(URL, data=data)