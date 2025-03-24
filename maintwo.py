# Great User
def great_user():
    print("Hello User, This is a Dinner Guest List Program")
    user_name = input("Whats your name? ")

# ask the user how many people they want to invite
def get_num_people():
    while True:
        try:
            num_people = int(input("How many people would you like to invite to your guest list? "))
        except ValueError:
            print("PLease enter a valid number ")

# user can now add the guest names

# remove guest
# add Guests
# main (so the user can choose to add or remove etc)
great_user()
get_num_people()