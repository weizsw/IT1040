# Trip Planner
# ------------
# The following program helps to create a travel itinerary


# Import modules
import destinations
#destinations was destintations
import currency

#methods should be above main
def print_welcome():
    
    print("---------------------------")
    print("Welcome to the Trip Planner")
    #quotationmaker was ' shouble be "
    print("---------------------------")
    print()


def save_itinerary(destination, length_of_stay, cost):
    # Itinerary File Name
    file_name = "itinerary.txt"
    
    # Create a new file
    itinerary_file = open(file_name, "w")
    #save should use w instead of r
    # object name should be itinerary_file not file_name
    # Write trip information
    itinerary_file.write("Trip Itinerary\n")
    itinerary_file.write("--------------\n")
    itinerary_file.write("Destination: " + destination + "\n")
    itinerary_file.write("Length of stay: " + str(length_of_stay) + "\n")
    #need to convert int to str of length of stay
    #also new line sign missing
    itinerary_file.write("Cost: $" + format(cost, ",.2f"))

    # Close the file
    itinerary_file.close()

def main():
    # Print a welcome message
    print_welcome()


    # Show destinations
    destinations.print_options()
    
    # Pick destination
    choice = destinations.get_choice()
    
    # Get destination info
    destination, euro_rate = destinations.get_info(choice)


    # Calculate currency exchange
    dollar_rate = currency.convert_euros_to_dollars(euro_rate)
    #should convert euros to dollars

    # Determine length of stay
    while True:
        try:
            length_of_stay = int(input("And how many days will you be staying in " + destination + "? "))
            #use + instead of ,
            # Check for non-positive input
            if (length_of_stay <= 0):
            # 0 day stay is not avaiable
                print("Please enter a positive number of days.")
                continue
        except:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break   
            #space error

    # Calculate cost
    cost = dollar_rate * length_of_stay
    #should be mutiplication instead of plus


    # Save itinerary
    try:
        save_itinerary(destination, length_of_stay, cost)
        
    # Catch file errors
    except ValueError:
        print("Error: the itinerary could not be saved.")
        
    # Print confirmation
    else:
        print("\nYour trip to",  destination ,"has been booked!")
        # to use varialbe inside of sentence should be splited by comma 

# Call main
main()





