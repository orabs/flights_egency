import utils
import db_functions as db


class Vehicle:

    def __init__(self, id, car_agency, max_seats, price):
        self.id = id
        self.car_agency = car_agency
        self.max_seats = max_seats
        self.price = price
        self.reserved_dates = []

    def is_vehicle_available(self, required_date):
        for date in self.reserved_dates:
            if not utils.is_available_date(date, required_date):
                return False
        return True

    def get_reserved_dates(self):
        self.reserved_dates = db.get_entity_by_id(self.id, "Vehicle").reserved_dates

    def __repr__(self):
        return "Vehicle_id:{0}\n car_agency:{1}\n max_seats:{2}\n price:{3}\n reserved_dates:{4}\n".format(
            self.id, self.car_agency, self.max_seats,self.price,self.reserved_dates)

