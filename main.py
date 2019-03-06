# from random import randint
# from hotel import Hotel
# from room import Room
# from vehicle import Vehicle
# from flight import Flight

from db_functions import get_entity_list_by_properties, get_all_certain_entity, add_or_update_entity
from generator import generate_id
from orders import Order


def hotel_dialog(location, start_date, end_date):
    hotels = get_all_certain_entity("Hotel")
    for hotel in hotels:
        print(hotels[hotel])
        print("------------------------------------------------------")
    hotel_results = []

    stars = raw_input("How many stars?\n")

    hotels = get_entity_list_by_properties("Hotel", stars=stars, location=location)

    if hotels:
        view = raw_input("With a view?   (0/1)\n")
        room_beds = raw_input("How many beds  (0/1)?\n")
        balcony = raw_input("With a Balcony  (0/1)?\n")
        price = raw_input("Maximum Price?\n")
        for hotel in hotels:
            room_list = hotel.get_rooms_list_by_properties(price=price, balcony=balcony, room_beds=room_beds,
                                                           view=view)
            available_room_list = []
            for room in room_list:
                if room.is_room_available((start_date, end_date)):
                    available_room_list.append(room)
            if available_room_list:
                hotel_results.append(hotel)
    return hotel_results


def flight_dialog(location, flight_date):
    flight_results = []
    flights = get_all_certain_entity("Flight")
    price = raw_input("Maximum Price?\n")
    for flight in flights:
        print(flights[flight])
        print("------------------------------------------------------")
    flights = get_entity_list_by_properties("Flight", flight_date=flight_date, target_place=location, price=price)
    print("flights {0}".format(flights))
    for flight in flights:

        if flight.is_flight_available():
            flight_results.append(flight)
    return flight_results


def vehicle_dialog(location, travel_date, ):
    vehicle_results = []
    vehicles = get_all_certain_entity("Vehicle")
    for vehicle in vehicles:
        print(vehicles[vehicle])
        print("------------------------------------------------------")

    price = raw_input("Maximum Price?\n")
    max_seats = raw_input("How many seats?\n")
    car_agency = raw_input("Do want a special agency ?  (leave empty if not)\n")
    vehicles = get_entity_list_by_properties("Vehicle", price=price,
                                             max_seats=max_seats, car_agency=car_agency)
    for vehicle in vehicles:
        if travel_date:
            if vehicle.is_vehicle_available():
                vehicle_results.append(vehicle)
        else:
            vehicle_results.append(vehicle)
    return vehicle_results


def main():
    while True:

        flight_id = None
        hotel_id = None
        vehicle_id = None
        print("Welcome to FL Travailing Agency System  Please insert only Y/N ,\n")

        customer_id = raw_input("Please Insert Customer ID \n")
        start_date = raw_input("When the customer want to trip? (dd-mm-YY) Format \n")
        end_date = raw_input("WHen the Customer want to return? (dd-mm-YY) Format \n")
        location = raw_input("Where? \n")
        answer = raw_input("Is the customer need a hotel \n")

        if answer.lower() == "y":
            hotel_results = hotel_dialog(location=location, start_date=start_date, end_date=end_date)
            hotel_id = raw_input(
                "Those are the hotels we have : \n {0} \n, please choose an ID \n ".format(hotel_results))

        answer = raw_input("Is the customer need a Flight \n")
        if answer.lower() == "y":
            flights_results = flight_dialog(location, start_date)
            flight_id = raw_input(
                "Those are the flights that we have : \n {0} \n, please choose an ID \n ".format(flights_results))

        answer = raw_input("Is the customer need a Vehicle \n")

        if answer.lower() == "y":
            vehicle_results = vehicle_dialog(location, start_date)
            vehicle_id = raw_input(
                "Those are the vehicles that we have : \n {0} \n, please choose an ID \n ".format(vehicle_results))

        order = Order(generate_id(), customer_id, flight_id, vehicle_id, vehicle_id)
        add_or_update_entity(order)
        answer = raw_input("Order has been saved successfully , DO you want another one?")
        if answer.lower() != "y":
            break


main()
# flights = get_entity_list_by_properties("Flight", flight_date=None, target_place="Morocco", price="10000")
# print(flights)
# a=get_all_certain_entity("Flight")
#
# print(a)
