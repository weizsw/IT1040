# read_sales2.py
# Chapter 6.2 
import os
# This program uses the for loop to read
#all of the values in the randomnum.txt file.

def main():
    # Open the randomnum.txt file for reading.
    while True:
        try:
            if os.stat("randomnum.txt").st_size > 0:
                print("Processing....")
            else:
                print ("empty file")
                break
            
            
            # raise ValueError
        except OSError:
            print ("file is not exist")
            break
        else:
        # From program 6-12
        # Initialize an accumulator to 0.0
            num_file = open('randomnum.txt', 'r')

            total = 0.0

            # From program 6-12
            # Initialize a variable to keep count of the sales.
            count = 0

            #From program 6-12
            print('List of random numbers in randomnum.txt:')

            # Read all the lines from the file.
            # Get the values from the file and total them.
            for line in num_file:
                # Convert a line to a float.
                amount = float(line)

                # Add 1 to the count variable.
                count += 1

                # Display the sales.
                print(amount)

                # Add the time to total.
                # total += amount

            # Close the file
            num_file.close()

            #From program 6-12
            # Display the total of the running times.
            print('Random number count: ', count)
            break

    # Call the main function
main()
