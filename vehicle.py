import utils
import pickle
import db_functions as db


class Vehicle:

    # all_vehicles= db.get_all_certain_entity("Vehicle")

    def __init__(self, id, car_agency, max_seats, price):
        self.id = id
        self.car_agency = car_agency
        self.max_seats = max_seats
        self.price = price
        self.reserved_dates = []

    def is_vehicle_available(self,required_date):
        for date in self.reserved_dates:
            if not utils.is_available_date(date,required_date):
                return False
        return True


    def get_reserved_dates(self):
        self.reserved_dates = db.get_entity_by_id(self.id,"Vehicle").reserved_dates

    @staticmethod
    def get_all_available_vehicles(self,start_date,end_date,max_seats=None,price=None):
        global all_vahicles
        available_vehicles=[]
        for vehicle in all_vahicles:
            if vehicle.is_vehicle_available(start_date,end_date):

                available_vehicles.append(vehicle)



