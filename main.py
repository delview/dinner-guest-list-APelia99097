# Create a program that will take user input about dinner guests they are inviting, 
# add names to a list, and print out invitations for each dinner guest. At the beginning of the program, ask the user how many guests they want to 
# invite and then create a loop that will keep appending names to the list until the maximum number is reached before printing out all the invitation messages.

def great_user():
    print("Hello User this is a dinner inviting list ")
    name = input("Whats your name ")

guest = []
num_people = int(input("How many people would you like to invite (number only) "))
for num in range(num_people):
    guest.append(input("Person To add to the list: "))
