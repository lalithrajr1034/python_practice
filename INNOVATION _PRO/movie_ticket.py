# Movie Ticket Booking System

# Show timings
show_timings = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"]

# Seats categorized
seats = {
    "VIP": list(range(1, 21)),          # ₹500
    "PREMIUM": list(range(21, 51)),     # ₹250
    "REGULAR": list(range(51, 101))     # ₹150
}

prices = {
    "VIP": 500,
    "PREMIUM": 250,
    "REGULAR": 150
}

# Display welcome
print("Welcome to the Movie Ticket Booking System")
print("--------------------------------------------------")
print("Available Seat Categories:\n1. VIP (₹500)\n2. PREMIUM (₹250)\n3. REGULAR (₹150)")
print("\nAvailable Show Timings:")
for i, time in enumerate(show_timings, start=1):
    print(f"{i}. {time}")
print("--------------------------------------------------")

# User selects timing
time_choice = int(input("Select show timing (1-4): "))
selected_time = show_timings[time_choice - 1]

# User selects seat type
seat_type_input = int(input("Select seat category (1: VIP, 2: PREMIUM, 3: REGULAR): "))
seat_type_map = {1: "VIP", 2: "PREMIUM", 3: "REGULAR"}

if seat_type_input not in seat_type_map:
    print("Invalid seat type selected.")
    exit()

seat_type = seat_type_map[seat_type_input]
available_seats = seats[seat_type]

# Display available seats
print(f"\nYou selected {seat_type} seats. Available seats: {available_seats}")

# Number of seats to book
num_to_book = int(input("How many seats do you want to book? "))

booked_seats = []

for i in range(num_to_book):
    seat_no = int(input(f"Enter seat number {i+1}: "))
    if seat_no in available_seats:
        available_seats.remove(seat_no)
        booked_seats.append(seat_no)
        print(f" Seat {seat_no} booked.")
    else:
        print(f"Seat {seat_no} is not available. Please choose a different one.")
        seat_no = int(input(f"Re-enter seat number {i+1}: "))
        if seat_no in available_seats:
            available_seats.remove(seat_no)
            booked_seats.append(seat_no)
            print(f" Seat {seat_no} booked.")
        else:
            print(" Booking failed for that seat.")
            continue

# Cost calculation
total_cost = prices[seat_type] * len(booked_seats)

# Booking receipt
print("\n Booking Receipt")
print("----------------------")
print(f"Show Time: {selected_time}")
print(f"Seat Type: {seat_type}")
print(f"Booked Seats: {booked_seats}")
print(f"Number of Tickets: {len(booked_seats)}")
print(f"Total Amount: ₹{total_cost}")
print("Thank you for booking with us!")
