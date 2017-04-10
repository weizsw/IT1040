# Destinations Module
# -------------------
# This module provides information about European destinations and rates
# All rates are in euros


def print_options():
    # Print travel options
    print("Travel Options")
    print("--------------")
    print("1. Rome")
    print("2. Berlin")
    print("3. Vienna")
    print("")


def get_choice():
    # Get destination choice
    while True:
        try:
            choice = int(input("Where would you like to go? "))
            #pareenthesis missing
            if (choice < 1 or choice > 3):
                #should use or instead of and 
                print("Please select a choice between 1 and 3.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            return choice


def get_info(choice):
    # Use numeric choice to look up destination info
    # Rates are listed in euros per day

    # Choice 1: Rome at €48/day
    #colonmissing for three blow
    if (choice == 1):

        return "Rome", 48

    # Choice 2: Berlin at €18/day
    elif (choice == 2):
        return "Berlin", 18

    # Choice 3: Vienna, €37/day
    elif (choice == 3):
        return "Vienna", 37
