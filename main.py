import os
import django


def initialize_django():
    # Initialize Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
    django.setup()


# Initialize Django
initialize_django()


def serialize_car_object(car):
    from car.serializers import CarSerializer

    # Serialize the car object
    car_serialized = CarSerializer(car)
    return car_serialized.data


def deserialize_car_object(data):
    from car.serializers import CarSerializer

    # Deserialize the car data
    serialized_car = CarSerializer(data=data)
    if serialized_car.is_valid():
        return serialized_car.save()
    else:
        # Handle validation errors
        print("Deserialization failed:", serialized_car.errors)
        return None


def template_creation():
    from car.models import Car

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
    serialized_object = serialize_car_object(car)
    print("Serialized Car Data:", serialized_object)

    # Deserialize the car data
    deserialized_object = deserialize_car_object(data)
    print("Deserialized Car Data:", deserialized_object)


# Call the template_creation function
template_creation()
