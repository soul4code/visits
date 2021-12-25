from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty
from rest_framework_gis.fields import GeometryField


class GeoPointField(GeometryField):

    def to_internal_value(self, value):
        if not isinstance(value, list) or len(value) != 2:
            raise ValidationError(
                'Invalid format: Accept only array with 2 coordinates: [<latitude>, <longitude>]'
            )

        return super().to_internal_value(f"POINT({value[0]} {value[1]})")

    def get_value(self, dictionary):
        return dictionary.getlist(self.field_name, empty)

    def to_representation(self, value):
        return super().to_representation(value)['coordinates']
