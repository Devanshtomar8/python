


from functions import *

# Welcome Interface
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("          WELCOME TO UPES FACULTY MANAGEMENT SYSTEM            ")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")



# Options to choose
def main_menu():
    print("1. Add Faculty\n2. Update Faculty\n3. search Faculty\n4. View all Faculty\n5. Delete Faculty\n6. Sign up\n7. Logout")
    # using exception handling we can tackel value error
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("warning..! Please enter only numbers")

def main():
    # For loggin
    logged_in = False
    while not logged_in:
        print("                             LOGIN             ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password):
            logged_in = True
        else:
            print("Invalid username or password.")

    while logged_in:
        choice = main_menu()
        if choice == 1:
            # To add a new facilty
            add_faculty()
        elif choice == 2:
            # To update a certain detail of a specific faculty
            update_faculty()
        elif choice == 3:
            # To search for the faculty by their name or email
            search_faculty()
        elif choice == 4:
            # To view all the faculties
            view_faculty()
        elif choice == 5:
            # To delete specific faculty
            delete_faculty()
        elif choice == 6:
            # To sign up:- for adding a new admin to login
            sign_up()
        elif choice == 7:
            # To Logout
            logged_in=False
        else:
            print("Invalid choice. Please try again.")

# calling main function
main()


