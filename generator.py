import datetime
import uuid
from random import randint
import db_functions as db
from faker import Faker
from flight import Flight
from hotel import Hotel
from room import Room
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
                        flight_time=faker_data.time(pattern="%H:%M:%S", end_datetime=None),price=randint(100,1500))

        db.add_or_update_entity(flight)


def generate_hotels(num):
    for i in range(0, num):
        faker_data = Faker()
        max_rooms = randint(10, 600)
        rooms_dict = generate_room(max_rooms)

        hotel = Hotel(id=generate_id(),
                      location=faker_data.country(),
                      stars=randint(1, 5), rooms=rooms_dict)

        db.add_or_update_entity(hotel)


def generate_room(num):
    room_dict = {}
    for i in range(1, num + 1):
        room = Room(id=generate_id(), room_beds=randint(2, 10),
                    view=randint(0, 1), balcony=randint(0, 1),
                    stage=randint(0, 10),
                    price=randint(100, 1000))

        room_dict[i] = room
    return room_dict


def generate_vehicle(num):
    for i in range(0, num):
        faker_data = Faker()

        vehicle = Vehicle(id=generate_id(),
                          max_seats=randint(1, 10),
                          price=randint(1, 14),
                          car_agency=faker_data.name())

        db.add_or_update_entity(vehicle)


# generate_vehicle(100)
# generate_hotels(100)
# generate_flights(100)
