import Learneres_Mentors


def menu():
    print("Hi this is the platform for the registration of Learners and Trainers.")
    print("\nMenu to Access The System\n___________________________")
    print("\n\t 1. View the Database\n\t 2. User Registration\n\t 3. Check the Availability of Mentors\n\t 4. Exit")
    print("\n__________________________\nPlease select your choice...!")
    s = input()
    return s


def switcher(selection):
    if selection == 1:
        print("The list of registered user are given below:\n_____________________________________\n")
        return 0
    elif selection == 2:
        print("Register your Details here...\n")
        name = input("Enter Your Name")
        email = input("Enter your Email")
        contact = input("ENter your Contact Number")
        m = Learneres_Mentors.Learners_Mentors(name, email, contact)
        m.field = input('Hello Mr' + name + ' What is you area of interest in Computer Programming')
        return 0
    elif selection == 3:
        print("Enter your interested area to check the availability of mentor\n")
        return 0
    else:
        return 4


sel = 1
while sel != 4:
    x = int(menu())
    sel = int(switcher(x))
