import pytest
from django.test import RequestFactory
from django.urls import reverse
from store.api.serializers import EmployeeSerializer, StoreSerializer, VisitSerializer


@pytest.mark.django_db
def test_store_serializer_enough_fields(db_service):
    """This test ensure that returns enough fields."""

    rf = RequestFactory()

    url = reverse("api:stores-list")

    request = rf.get(url)
    serializer = StoreSerializer(context={"request": request})

    assert set(serializer.fields.keys()) == {"id", "name", "employee"}


@pytest.mark.django_db
def test_employee_serializer_enough_fields(db_service):
    """This test ensure that returns enough fields."""

    serializer = EmployeeSerializer()

    assert set(serializer.fields.keys()) == {
        "id",
        "name",
    }


@pytest.mark.django_db
def test_visit_serializer_enough_fields(db_service):
    """This test ensure that returns enough fields."""

    serializer = VisitSerializer()

    assert set(serializer.fields.keys()) == {"id", "date", "store", "coordinates"}
