import db_functions as db


class Flight():
    # all_flights = db.get_all_certain_entity("Flight")

    def __init__(self, id, max_sits, start_place, target_place, flight_duration, flight_date, flight_time):
        self.id = id
        self.max_sits = max_sits
        self.start_place = start_place
        self.target_place = target_place
        self.flight_duration = flight_duration
        self.flight_date = flight_date
        self.flight_time = flight_time
        self.used_seats = 0

    def is_flight_available(self):
        return self.used_seats < self.max_sits

    def get_availability_seats(self):
        self.used_seats = db.get_entity_by_id(self.id,"Flight").used_seats
