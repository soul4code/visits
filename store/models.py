from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models as gis_models
from phonenumber_field.modelfields import PhoneNumberField


class Employee(models.Model):
    name = models.CharField("Name", max_length=100)
    phone = PhoneNumberField()

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField("Name", max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Visit(models.Model):
    date = models.DateTimeField("Visit Date", auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    coordinates = gis_models.PointField(geography=True)

    def __str__(self):
        return f"{self.date} {self.store}"

    @property
    def longitude(self):
        return self.coordinates.x

    @property
    def latitude(self):
        return self.coordinates.y
