import db_functions as db


class Flight():

    def __init__(self, id, max_sits, start_place, target_place, flight_duration, flight_date, flight_time, price):
        self.id = id
        self.max_sits = max_sits
        self.start_place = start_place
        self.target_place = target_place
        self.flight_duration = flight_duration
        self.flight_date = flight_date
        self.flight_time = flight_time
        self.used_seats = 0
        self.price = price

    def is_flight_available(self):
        return self.used_seats < self.max_sits

    def get_availability_seats(self):
        self.used_seats = db.get_entity_by_id(self.id, "Flight").used_seats

    def __repr__(self):
        return "Flight_id:{0}\n max_sits:{1}\n start_place:{2}\n target_place:{3}\n " \
               "flight_duration:{4}\n flight_date:{5}\n flight_time:{6}\n price:{7}\n".format(
                self.id, self.max_sits, self.start_place,
                self.target_place, self.flight_duration, self.flight_time,self.used_seats, self.price)
