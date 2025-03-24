# Great User
def great_user():
    print("Hello User, This is a Dinner Guest List Program")
    user_name = input("What's your name? ")

# Ask the user how many people they want to invite
def get_num_people():
    while True:
        try:
            num_people = int(input("How many people would you like to invite to your guest list? "))
            if 1 <= num_people <= 100000:
                return num_people
            else:
                print("Please enter a number between 1 and 100,000.")
        except ValueError:
            print("Please enter a valid number.")

# User can now add the guest names
def add_guest(num_people, guest):
    for _ in range(num_people):
        guest_name = input("What's the name of the guest you would like to invite? ")
        guest.append(guest_name)
        print("Name Added!")

# Main Program Flow
def main():
    great_user()
    num_people = get_num_people()
    guest = []  # Initialize the guest list
    add_guest(num_people, guest)
    print(f"Your final guest list: {', '.join(guest)}")

# Run the main function
if __name__ == "__main__":
    main()
