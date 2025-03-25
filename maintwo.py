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
    for num in range(num_people):
        guest_name = input("What's the name of the guest you would like to invite? ")
        guest.append(guest_name)
        print("Name Added!")

def add_new_guest(guest):
    new_guest = input("Whats the name of the person you would like to add? ")
    guest.append(new_guest)
    print(f"{new_guest} has been added to the list")
    
def remove_guest(guest):
    remove_guest = input("Whats the name of the person you would like to remove")
    if remove_guest in guest:
        guest.remove(remove_guest)
    else:
        print("Given name is already not in list ")

def generate_list(guest):
    if not guest:
        print("No guests have been added yet.")
    else:
        print("Here are the invitation messages for your guests:")
        for name in guest:
            print(f"Dear {name}, you have been invited to my dinner party")

def do_something(guest):
    while True:  # Keeps asking until the user chooses to generate the list
        do_smt = input("Would you like to [A]dd, [R]emove, or [G]enerate the final list? ").capitalize()
        if do_smt == "A":
            add_new_guest(guest)
            print(f"Guest list: {', '.join(guest)}")
        elif do_smt == "R":
            remove_guest(guest)
            print(f"Guest list: {', '.join(guest)}")
        elif do_smt == "G":
            generate_list(guest)
            break  # Exit the loop after generating the list
        else:
            print("Invalid option, please choose A, R, or G.")

        
            

# Main Program Flow
def main():
    great_user()
    num_people = get_num_people()
    guest = []  # Initialize the guest list
    add_guest(num_people, guest)
    print(f"Your final guest list: {', '.join(guest)}")
    do_something(guest)

# Run the main function
if __name__ == "__main__":
    main()
