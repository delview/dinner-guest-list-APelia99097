
# Function that greats the user

print("Hello User this is a dinner inviting list ")
name = input("Whats your name ").capitalize()

# makes a empty guest list
guest = []
# asks the user how many people they would like to add to the list
num_people = int(input("How many people would you like to invite (number only) "))


# A Loop that runs until the num_people in the list are over
for num in range(num_people):
    # adds the name of the guest to the guest list
   guest_name = input("Whats the name of the guest you want to add: ")
   guest.append(guest_name)
   print("Name Added!")


# A loop that prints a message for each person
for guest_name in guest:
    print(f"Here is a message for {guest_name}: ")
    print(f"Hello {guest_name} you have been invited to {name}s dinner party" )

while True:
    kick = input("Would you like to remove someone from the list? [y] or [n]")
    if kick == 'y':
        destroy = input("Please Enter the name of the person you want to kick off the list: ")
        if destroy in guest:
            guest.remove(destroy)
            print(f"{destroy} has been removed from the list")
            print(guest)
        else:
           print("Given person is already not in the list")
    elif kick == 'n':
        create = input("would you like to add someone to the list? [y] or [n] ")
        if create == 'y':
            spawn = input("PLease enter the name of the person you would like to invite: ")
            guest.append(spawn)
            print(f"{spawn} has been added to the list")
        elif create == 'n':
            pls_stop = input("is this your final list? [y] or [n] ")
            if pls_stop == 'y':
                print(f"Here is your final list, im sick of this {guest}")
                print("BYEEEE! ")
                exit()
            elif pls_stop == 'n':
                print("Im done.")
                print(guest)
                exit()
        



