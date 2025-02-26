
# Function that greats the user
# remove function for testing
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


for num in range(num_people):
    print(f"Here is a message for {guest_name}: ")
    print(f"Hello {guest_name} you have been invited to {name}s dinner party" )