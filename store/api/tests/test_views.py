import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from store.models import Employee, Store


@pytest.mark.django_db
def test_stores_only_for_authorized(client):
    """This test ensures that only authorized user can get stores."""

    url = reverse("api:stores-list")

    response = client.get(url)
    assert response.status_code == HTTP_403_FORBIDDEN

    header = {"HTTP_AUTHORIZATION": "Phone +79992223322"}
    response = client.get(url, **header)
    assert response.status_code == HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_stores_for_authorized(client, default_users):
    """This test ensures that authorized user can get stores."""

    Employee.objects.create(name="Test", phone="+79992223322")

    url = reverse("api:stores-list")

    header = {"HTTP_AUTHORIZATION": "Phone +79992223322"}
    response = client.get(url, **header)
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_visit(client, default_users):
    """This test ensures that authorized user can get stores."""

    employee = Employee.objects.create(name="Test", phone="+79992223322")
    store = Store.objects.create(name="Test", employee=employee)

    url = reverse("api:visit-list")

    header = {"HTTP_AUTHORIZATION": "Phone +79992223322"}
    response = client.post(
        url, content_type='application/json', data={"store": store.id, "coordinates": [13, 13]}, **header
    )
    assert response.status_code == HTTP_201_CREATED

    assert response.data["coordinates"] == [13, 13]
