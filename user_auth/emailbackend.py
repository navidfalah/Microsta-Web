
from django.contrib.auth.backends import ModelBackend
from .models import User


class EmailBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        print(kwargs)
        if 'email' in kwargs:
            email = kwargs['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                pass
