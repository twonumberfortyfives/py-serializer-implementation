import os
import django

# Initialize Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
django.setup()

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> dict:
    # Serialize the car object
    car_serialized = CarSerializer(car)
    return car_serialized.data


def deserialize_car_object(data: dict) -> Car:
    # Deserialize the car data
    serialized_car = CarSerializer(data=data)
    if serialized_car.is_valid():
        return serialized_car.save()
    else:
        # Handle validation errors
        print("Deserialization failed:", serialized_car.errors)
        return None


# Create a car object
car = Car.objects.create(
    manufacturer="German",
    model="BMW",
    horse_powers=240,
    is_broken=False,
    problem_description=""
)

data = {
    "manufacturer": "Sweden",
    "model": "Volvo",
    "horse_powers": 24,
    "is_broken": False,
    "problem_description": "motor"
}


# Serialize the car object
serialize_object = serialize_car_object(car)
print("Serialized Car Data:", serialize_object)

non_serialized_object = deserialize_car_object(data)
print("Deserialized Car Data:", non_serialized_object)
