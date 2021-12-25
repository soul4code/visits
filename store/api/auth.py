import os

from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.utils.translation import gettext_lazy as _

from store.models import Employee


class PhoneNumberAuth(BaseAuthentication):

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'phone':
            return None

        if len(auth) == 1:
            msg = _('Invalid header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        phone = str(auth[1])

        try:
            Employee.objects.get(phone=phone)
            user = get_user_model().objects.get(username=os.environ.get("API_USER_NAME"))
        except Employee.DoesNotExist:
            msg = _('Invalid phone. Employee with this credentials does not exists')
            raise exceptions.AuthenticationFailed(msg)

        return user, phone
