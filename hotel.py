import utils
from db_functions import get_entity_by_id


class Hotel:

    def __init__(self, id, location, stars, rooms):
        self.id = id
        self.location = location
        self.stars = stars
        self.rooms = rooms

    def is_hotel_available(self, required_date):
        for date in self.reserved_dates:
            if not utils.is_available_date(date, required_date):
                return False
        return True

    def get_reserved_dates(self):

        self.reserved_dates = get_entity_by_id(self.id, "Hotel").reserved_dates

    def get_rooms_list_by_properties(self, **kwargs):
        results_list = []
        all_rooms = [x for x in self.rooms.values()]

        for item in all_rooms:
            flag = True
            for key in kwargs:

                if key == "room_beds" or key == "balcony" or key == "view" or key == "stage":
                    if int(getattr(item, key)) < int(kwargs[key]):
                        flag = False
                elif key == "price":
                    if int(getattr(item, key)) > int(kwargs[key]):
                        flag = False
                elif getattr(item, key) != kwargs[key]:
                    flag = False
            if flag:
                results_list.append(item)

        return results_list

    def __repr__(self):
        return "hotel_id:{0}\n location:{1}\n stars:{2}\n ".format(self.id, self.location, self.stars)
