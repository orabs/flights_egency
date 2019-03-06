import utils
from db_functions import get_entity_by_id


class Room:

    def __init__(self, id, view, room_beds, balcony, stage, price, reserved_dates=[]):
        self.id = id
        self.view = view
        self.room_beds = room_beds
        self.balcony = balcony
        self.stage = stage
        self.price = price
        self.reserved_dates = reserved_dates

    def is_room_available(self, required_date):
        for date in self.reserved_dates:
            if not utils.is_available_date(date, required_date):
                return False
        return True

    def get_reserved_dates(self):
        self.reserved_dates = get_entity_by_id(self.id, "Room").reserved_dates

    def __repr__(self):
        return "room_id:{0}\n view:{1}\n room_beds:{2}\n balcony:{3}\n stage:{4}\n price:{5}\n" \
               " reserved_dates:{6}\n".format(
                    self.id, self.view, self.room_beds, self.balcony, self.stage, self.price, self.reserved_dates)
