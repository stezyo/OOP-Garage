guarage =[]

import Parking_modules

while True:
    command = input(""" Welcome to Rangers Lot
what would you like to do? Park/Leave  """).lower()
    if command == 'park':
        print("that will be $ 10 an hour")
        choice = input(''' 
what kind of vehicle do you have? options are 
1 - Sedan
2 -Suv
3 -Truck
4 -Motorcycle
    ''').lower()
        if choice == "sedan":
            print("Please stay on the first level")
            continue

        #             Parking_modules.Car()
        #             Parking_modules.add_a_car(choice)

        elif choice == "suv":
            print("Please continue to the second floor for this car")
            continue

        elif choice == "truck":
            print("Please continue to the third floor")
            continue

        elif choice == "motorcycle":
            print("Basement parking spots are available for Motorcycles")
            continue

        else:
            print("Sorry! I didn't get that")
            pass
    elif command == "leave":
        print("gate is closed, have a great day")

#         elif command == "truck":
#             print("we are going to the third floor for this car")    
#             spot_list_1 = [i for i in range(10)]
#             print(spot_list_1)

#                     # print(need to be defined somewhere spot_list)
        
#         elif command == "motorcycle" :
#             print("we are going to the forth floor for this car")
        
#         else:
#             print('sorry we have nothing available ')
#             break
        
#         elif command == "leave"

#             hours = int(input("Enter hours (0 if under 1 hour): "))
#                 total_fee = calc_parking_fee(hours)
#                 print(f'${total_fee:.2f}')
#  print(spot_list_1)
# we need a ticket list
#  and a parking spot dict


# it should take out the assigned spot from each one of those

# creat a function with a dict to figure
        
#         if they decided to park print prices

#     assign a spot + take a ticket
#         if they decided to leave tell them they have to pay
#         if they pay tell them they can leave
        
#     here is all the functions are coming next for this type


      

#     here is all the functions are coming next for this type

      


#             here is all the functions are coming next for this type

