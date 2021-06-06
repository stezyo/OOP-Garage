# from random import
class Garage():
    slots = [1,2,3,4,5,6,7,8,9,10]
    tickets = {1,2,3,4,5,6,7,8,9,10}


# total_parking_spots = 10
# available_spots = []
# unavailable_spots = []
# parked_car_list = []


def calc_parking_fee(garage):
    if hours <= 1:
        fee = 10.00

    elif 1 <= hours < 12:
        fee = 10.00 * hours

    elif hours >= 10:
        fee = 100.00

    return fee


# list of available places
def reset_place(list_of_places, place_number):
    for place in range(1, place_number + 1):
        list_of_places.append(place)
        print(list_of_places)


def add_a_car(choice):
    choosen_number = input("please pick a spot")
    parked_car_list.append(the_car)
    print(f'{make} {model} added to parking at place n {choosen_number}')


# after a car leaves we put that spot back in list
def make_a_place_available(place_number):
    unavailable_spots.remove(place_number)
    available_spots.append(place_number)
    print(f'Place in {place_number} is now available.')


# class Car():
#     make = input('what is the make?')
#     model = input('what is the model for your car? ')

#     print(" you will stay in level one")


    def __init__(self, make, model):
        self.make = make
        self.model = model
