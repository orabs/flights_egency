
import datetime
import uuid
from random import randint
import db_functions as db
from faker import Faker
from flight import Flight
from hotel import Hotel
from vehicle import Vehicle


def generate_id():
    return str(uuid.uuid4())


def generate_flights(num):
    for i in range(0, num):
        faker_data = Faker()
        start_date = faker_data.date_between_dates(date_start=datetime.datetime.now(),
                                                   date_end=datetime.datetime.now() + datetime.timedelta(days=365))
        flight = Flight(id=generate_id(),
                        max_sits=randint(50, 400), start_place=faker_data.country(),
                        target_place=faker_data.country(),
                        flight_duration=randint(1, 14), flight_date=start_date,
                        flight_time=faker_data.time(pattern="%H:%M:%S", end_datetime=None))


        db.add_or_update_entity(flight)


def generate_hotels(num):
    for i in range(0, num):
        faker_data = Faker()
        start_date = faker_data.date_between_dates(date_start=datetime.datetime.now(),
                                                   date_end=datetime.datetime.now() + datetime.timedelta(days=365))
        hotel = Hotel(id=generate_id(),
                      max_rooms=randint(1, 10), location=faker_data.country(),
                      price=randint(100, 5000),
                      stars=randint(1, 14))

        db.add_or_update_entity(hotel)


def generate_vehicle(num):
    for i in range(0, num):
        faker_data = Faker()

        vehicle = Vehicle(id=generate_id(),
                        max_seats=randint(1,10),
                        price=randint(1, 14),
                        car_agency=faker_data.name())

        db.add_or_update_entity(vehicle)


# generate_vehicle(5)
generate_hotels(5)
# generate_flights(5)

# print(db.get_all_certain_entity('Flight'))
# print(db.get_all_certain_entity('Hotel').keys())
# print("adgasdashah")
print(len(db.get_all_certain_entity('Hotel')))

# print(db.get_all_certain_entity('Vehicle'))

