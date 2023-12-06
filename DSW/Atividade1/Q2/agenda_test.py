from agenda import AppointmentBook

option = 0

contact = AppointmentBook()

while option != 6:
    print('1 - To add a contact\n')
    print('2 - To remove a contact\n')
    print('3 - To search a person by name\n')
    print('4 - To print your Appointment Book\n')
    print('5 - To detail a contact by index\n')
    print('6 - To Exit')
    option = int(input('Type your option:\n'))
    if option == 1:
        contact.save()
    elif option == 2:
        contact.remove_contact()
    elif option == 3:
        contact.search_contact()
    elif option == 4:
        contact.print()
    elif option == 5:
        contact.detail_contact()
    elif option == 6:
        break