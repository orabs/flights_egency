class Order:

    def __init__(self, id, customer, flight=None, vehicle=None,hotel=None):
        self.id = id
        self.customer_id = customer
        self.flight_id = flight
        self.vehicle_id = vehicle
        self.hotel_id = hotel


    def __repr__(self):
        return "order_id:{0}\n customer_id:{1}\n flight_id:{2}\n vehicle_id:{3}\n hotel_id:{4}\n".format(
            self.id, self.customer, self.flight,self.vehicle,self.hotel)


