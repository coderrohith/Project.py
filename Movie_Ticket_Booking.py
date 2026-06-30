seats=10

while seats > 0:
    print("Available Seats :",seats)

    ticket=int(input("How many tickets?:"))

    if ticket <= seats:
        seats -= ticket
        print("Booking Successful")
    else:
        print("Not Enough Seats")

        if seats == 0:
            print("House Full")