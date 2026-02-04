# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:41:10 2026

@author: Naveen
"""



# -------------------------------
# Ticket Booking – Age Restricted
# -------------------------------


# Total capacity available for sale
total_no_of_seats = 350  # total number of seats that can be sold overall

# Cumulative counters
sold = 0          # total tickets sold across all successful bookings
bookings = 0      # number of successful bookings (transactions)
rejected = 0      # number of rejected bookings due to age restriction or invalid request

# Keep accepting bookings until we sell out all seats
# NOTE: This loop also ends if the user enters 0 seats or requests too many seats (see break below)
while sold != total_no_of_seats:  # continue taking bookings while there are seats left
    # Ask user how many seats they want to book in this transaction
    no_of_seats_to_book = int(input("No of seats to book: "))  # capture requested seat count for this booking

    # If the user enters 0, or requests more seats than remain, stop taking bookings
    # Also, if the user requests more than 15 seats in a single booking, reject it
    if no_of_seats_to_book == 0 or no_of_seats_to_book == total_no_of_seats - sold or no_of_seats_to_book>15:
        break  # exit the main loop entirely (stop the booking process)
        
    # For each seat in the requested booking, collect the age
    # If any one passenger is under 12, the *entire booking* is rejected
    for seat in range(no_of_seats_to_book):  # iterate once per seat to get each passenger's age
        age = int(input("Enter age: "))  # input the age for the current seat index

        # If any audience member is younger than 12, reject this entire booking
        if age < 12:  # check the age restriction condition
            print("BOOKING REJECTED - Age restriction")  # inform user that the age rule was violated
            rejected += 1   # count this booking as rejected due to age restriction

            # break out of the per-seat age collection loop (do not confirm booking)
            break  # stop collecting further ages for this booking and return to outer loop

        # If we've successfully collected ages for the last requested seat, confirm the booking
        elif seat == no_of_seats_to_book - 1:  # this condition is true only for the last seat index
            bookings += 1  # increment successful bookings counter
            print(f"BOOKING CONFIRMED - {no_of_seats_to_book} tickets")  # acknowledge the successful booking
            sold += no_of_seats_to_book  # update total sold seats by the number requested in this booking

        else:
            # Continue collecting ages for the rest of the seats in this booking
            continue  # proceed to next passenger age input within the same booking

# Print final summary after loop ends (sold out OR user stopped)
print(
    f"Final Report: "  # heading for the summary report
    f"Total Bookings: {bookings}, "  # total number of successful transactions
    f"Total Tickets Sold: {sold}, "  # total tickets that were sold successfully
    f"Rejected Bookings= {rejected}, "  # total number of rejected booking attempts
    f"Remaining Seats: {total_no_of_seats - sold}"  # seats still available after the process ends
)  # end of summary print

