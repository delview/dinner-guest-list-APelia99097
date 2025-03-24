
# Function that greats the user
def greet_user():
    print("Hello User this is a dinner inviting list ")
    name = input("Whats your name ").capitalize()

def get_user_name():
    # makes a empty guest list
    guest = []
    # asks the user how many people they would like to add to the list
    num_people = int(input("How many people would you like to invite (number only) "))
    return name

def add_guests(num_people):
    # A Loop that runs until the num_people in the list are over
    for num in range(num_people):
        # adds the name of the guest to the guest list
        guest_name = input("Whats the name of the guest you want to add: ")
        guest.append(guest_name)
        print("Name Added!")
        return guest_list



def send_invitations(guest_list, name):
    # A loop that prints a message for each person
    for guest_name in guest:
        print(f"Here is a message for {guest_name}: ")
        print(f"Hello {guest_name} you have been invited to {name}s dinner party" )
        for guest_name in guest_list:


def remove_guest(guest_list):
    destroy = input("Please enter the name of the person you want to kick off the list: ")
    if destroy in guest_list:
        guest_list.remove(destroy)
        print(f"{destroy} has been removed from the list.")
    else:
        print(f"{destroy} is not in the list.")


# Function to add a new guest to the list
def add_guests(guest_list):
    spawn = input("Please enter the name of the person you would like to invite: ")
    guest_list.append(spawn)
    print(f"{spawn} has been added to the list")

# Main function that controls the program flow
def main():
    greet_user()
    name = get_user_name()
    num_people = int(input("How many people would you like to invite (number only): "))
    
    guest_list = add_guests(num_people)
    send_invitations(guest_list, name)
    
    while True:
        kick = input("Would you like to remove someone from the list? [y] or [n]: ").lower()
        if kick == 'y':
            remove_guest(guest_list)
            print(guest_list)
        elif kick == 'n':
            create = input("Would you like to add someone to the list? [y] or [n]: ").lower()
            if create == 'y':
                add_guests(guest_list)
            elif create == 'n':
                pls_stop = input("Is this your final list? [y] or [n]: ").lower()
                if pls_stop == 'y':
                    print(f"Here is your final list: {guest_list}")
                    print("BYEEEE!")
                    break
                elif pls_stop == 'n':
                    print("Im done.")
                    break
            print(guest_list)

if __name__ == "__main__":
    main()


