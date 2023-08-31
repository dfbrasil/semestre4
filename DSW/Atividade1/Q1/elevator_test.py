from elevator import Elevator

option = '0'

capacity = int(input('What is the capacity of the elevator?'))
number_of_floors = int(input('How many floors are there in the building?'))
actual_floor = 0

elevator = Elevator(0,number_of_floors,capacity,0)



while(option != '9'):
    option = input('1 - to get in \n2 - to get out \n3 - to go up \n4 - to go down \n5 - to get capacity \n6 - to get actual floor \n7 - to get numbers of floors \n9 - to exit \n')
    if option == '1':
        elevator.get_in(capacity)
    elif option == '2':
        elevator.get_out()
    elif option == '3':
        elevator.go_up()
    elif option == '4':
        elevator.go_down()
    elif option == '5':
        elevator.get_capacity()
    elif option == '6':
        elevator.get_actual_floor()
    elif option == '7':
        elevator.get_number_of_floors()
    elif option == '9':
        print ('Goodby Elevator')
        break