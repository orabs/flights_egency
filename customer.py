import pickle
import json

filename = "data.pickle"


class Customer:

    def __init__(self, id, first_name, last_name, phone_numbers, credit_card):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_numbers = phone_numbers
        self.credit_card = credit_card
        self.orders_history = []
        self.set_orders_history()

    @property
    def credit_card(self):
        pass

    @credit_card.setter
    def credit_card(self, credit_card):
        answer = raw_input('Do you agree to save your credit card details (Y/N) ? ')

        while True:
            if answer.upper() == "Y":
                self.credit_card = credit_card
                print("Credit Card has been saved")
                break
            elif answer.upper() == "N":
                print("Credit Card hasn't been saved")
                break

    def set_orders_history(self):
        try:
            with open(filename, 'rb+') as file:
                all_customers = pickle.load(file)['customer']

                if self.id in all_customers:
                    self.orders_history = all_customers[self.id].orders_history
        except IOError:
            print("History is empty")

    def get_history_orders(self):

        for order in self.orders_history:
            print(order)

    def get_places_counter(self):

        places_counter = {}
        for order in self.orders_history:

            if order._target_place in places_counter:
                places_counter[order._target_place] += 1
            else:
                places_counter[order._target_place] = 1
        return places_counter
    #
    # @staticmethod
    # def insert_new_customer(customer):
    #
    #     with open(filename, 'rb+') as file:
    #         try:
    #             data=pickle.load(file)
    #             all_customers=data['customers']
    #         except EOFError:
    #             all_customers={}
    #     all_customers[customer.id]=customer
    #
    #     with open(filename, 'wb+') as file:
    #         pickle.dump(all_customers, file)
    #     print("Customer has been added successfully ! ")
    #
    #
    # @staticmethod
    # def get_customer_by_id(id):
    #     with open(filename, 'rb') as file:
    #
    #         data = pickle.load(file)
    #     all_customers=data['customers']
    #     if id in all_customers:
    #         return all_customers[id]
    #     return False
    #
    # @staticmethod
    # def get_all_customers():
    #     with open(filename, 'rb') as customers_file:
    #         all_customers = pickle.load(customers_file)['customers']
    #     return all_customers

# a = Customer("asf", "37", "asf", "3477", "asf")
#
# Customer.insert_new_customer(a)

# print(a.get_customer_by_id("asf"))
