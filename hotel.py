import utils
import pickle
import db_functions as db


class Hotel:

    # all_hotel= db.get_all_certain_entity("Hotel")

    def __init__(self, id, location, max_rooms, price, stars):
        self.id = id
        self.location = location
        self.max_rooms = max_rooms
        self.price = price
        self.stars = stars
        self.reserved_dates = []

    def is_hotel_available(self,required_date):
        for date in self.reserved_dates:
            if not utils.is_available_date(date,required_date):
                return False
        return True

    def get_reserved_dates(self):
        self.reserved_dates = db.get_entity_by_id(self.id,"Hotel").reserved_dates

    def get_all_available_vehicles(self):
        pass


