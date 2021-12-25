import os

import psycopg2
import pytest
from django.conf import settings
from django.core.management import call_command
from psycopg2 import OperationalError


def pytest_configure():
    """Configure django settings."""

    # use fast password hashers for tests
    settings.PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

    # django to store outgoing mails in locmem backend.
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

    settings.DEBUG = True


def db_is_responsive(docker_ip) -> bool:
    try:
        conn_settings = settings.DATABASES["default"]
        conn = psycopg2.connect(
            f"dbname='{conn_settings['NAME']}' "
            f"user='{conn_settings['USER']}' "
            f"host='{docker_ip}' "
            f"port='{os.environ.get('TEST_POSTGRES_PORT')}' "
            f"password='{conn_settings['PASSWORD']}' "
            f"connect_timeout=1 "
        )
        conn.close()
        return True
    except OperationalError:
        return False


@pytest.fixture(scope="session")
def db_service(docker_ip, docker_services):
    """Ensure that docker database service is up and responsive."""

    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: db_is_responsive(docker_ip)
    )
    settings.DATABASES["default"]["HOST"] = docker_ip
    settings.DATABASES["default"]["PORT"] = os.environ.get("TEST_POSTGRES_PORT")
    return


@pytest.fixture
def default_users(db):
    call_command("defaultuser_create")


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "docker-compose.test.yml")
