import os
from django.contrib.auth import get_user_model
from django.core.management.commands.shell import Command as ShellCommand


def _create_superuser():
    user_model = get_user_model()
    if user_model.objects.filter(is_superuser=True).exists():
        print("Superuser already exists. Enjoy your experience")
        return

    user_model.objects.create_superuser(
        os.environ.get("SU_NAME"),
        email=os.environ.get("SU_EMAIL"),
        password=os.environ.get("SU_PASSWORD")
    )
    print("Superuser created. Enjoy your experience")


def _create_api_user():
    user_model = get_user_model()
    if user_model.objects.filter(username=os.environ.get("API_USER_NAME")).exists():
        print("API user already exists. Enjoy your experience")
        return

    user_model.objects.create_user(
        os.environ.get("API_USER_NAME"),
        email=os.environ.get("API_USER_EMAIL")
    )
    print("API user created. Enjoy your experience")


class Command(ShellCommand):
    """Create default superuser if does not exists"""

    def handle(self, **options) -> None:
        """Handle command."""

        _create_superuser()
        _create_api_user()
