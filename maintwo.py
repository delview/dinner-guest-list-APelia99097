# Great User
def great_user():
    print("Hello User, This is a Dinner Guest List Program") # prints a message
    user_name = input("What's your name? ") # user input for gathering users name

# Ask the user how many people they want to invite
def get_num_people():
    while True: # loop
        try:
            num_people = int(input("How many people would you like to invite to your guest list? ")) # asks user number of people they would like to invite
            if 1 <= num_people <= 1000000000000000000000000000000000000000000000000000000000000000000000000000: # if the number is inbetween theese numbers
                return num_people # return num_people
            else: # otherwise
                print("Please enter a number between 1 and 100,000.") # print a message informing the user of what they need to type
        except ValueError: # if they type a letter
            print("Please enter a valid number.") # prints a message to let them know

# User can now add the guest names
def add_guest(num_people, guest): 
    for num in range(num_people): # runs this for as many people the user likes to invite
        guest_name = input("What's the name of the guest you would like to invite? ") # akses for there name
        guest.append(guest_name) # adds the name to a list
        print("Name Added!") # feedback to the user

def add_new_guest(guest): # function so that you can add new people to the list
    new_guest = input("Whats the name of the person you would like to add? ") # askes the name of the person they wanna invite
    guest.append(new_guest) # adds them to the list
    print(f"{new_guest} has been added to the list") # feedback to the user
    
def remove_guest(guest): # to remove people
    remove_guest = input("Whats the name of the person you would like to remove") # asks the user name of the person they wanna kick of the list
    if remove_guest in guest: # if the person is in the list
        guest.remove(remove_guest) # removes the guest 
    else: # if there name is not in the list
        print("Given name is already not in list ") # lets the user know person isnt in the list

def generate_list(guest): # generates the list functon
    if not guest: # checks if the list is empty
        print("No guests have been added yet.") # tells user no people in list
    else: # otherwise
        print("Here are the invitation messages for your guests:") # informs user of whats about to happen
        for name in guest: # for each name in the guest list
            print(f"Dear {name}, you have been invited to my dinner party") # prints a message to each invited person

def do_something(guest): # kind of like the main thing that calls all functions
    while True:  # Keeps asking until the user chooses to generate the list
        do_smt = input("Would you like to [A]dd, [R]emove, or [G]enerate the final list? ").capitalize() # options for user
        if do_smt == "A": # if they choose add person
            add_new_guest(guest) # calls the function to add people
            print(f"Guest list: {', '.join(guest)}") #prints guest list
        elif do_smt == "R": # if they chose remove smt
            remove_guest(guest) # calls the function
            print(f"Guest list: {', '.join(guest)}") # prints the list
        elif do_smt == "G": # if they choose to genereate final list
            generate_list(guest) # calls the function
            break  # Exit the loop after generating the list
        else: # otherwise 
            print("Invalid option, please choose A, R, or G.") # informs the user its invalid

        
def do_again(): # functon to redo the program
    repeat = input("Would you like to use this program again? [Y] or [N] ").capitalize() # asks user if they want to repeat
    if repeat == "Y": # if yes
        main() # run main func again
    else: # otherwise
        print("PCE") # prints pce


# Main Program Flow
def main():
    great_user() # function to call user
    num_people = get_num_people() 
    guest = []  # Initialize the guest list
    add_guest(num_people, guest) # call func
    print(f"Guest list: {', '.join(guest)}") #prints initial guest list
    do_something(guest) # calls function
    do_again() # calls function

# Run the main function
if __name__ == "__main__":
    main()
