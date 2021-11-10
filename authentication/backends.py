from django.contrib.auth.backends import ModelBackend
from django.utils import timezone

from authentication.models import User


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request=None, email=None, password=None, username=None, **kwargs):
        if not email:
            email = username
        if not (email and password):
            return None
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                return user
        except User.DoesNotExist:
            return None