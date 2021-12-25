from rest_framework import serializers

from store.api.fields import GeoPointField
from store.models import Store, Employee, Visit


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name')


class StoreSerializer(serializers.ModelSerializer):

    employee = EmployeeSerializer()

    class Meta:
        model = Store
        fields = ('id', 'name', 'employee')


class VisitSerializer(serializers.ModelSerializer):

    coordinates = GeoPointField()

    class Meta:
        model = Visit
        fields = ('id', 'date', 'store', 'coordinates')
        read_only_fields = ('date',)
