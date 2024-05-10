import io

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def serialize_car_object(car):
    from car.serializers import CarSerializer
    car_serialized = CarSerializer(car)
    json = JSONRenderer().render(car_serialized.data)
    return json


def deserialize_car_object(data):
    from car.serializers import CarSerializer
    stream = io.BytesIO(data)
    parsed_data = JSONParser().parse(stream)

    serializer = CarSerializer(data=parsed_data)

    if serializer.is_valid(raise_exception=True):
        return serializer.save()
