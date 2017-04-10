# write_sales.py
# Chapter 6.2
from random import randint

def digitCheck(x):
    try:
        x = int(x)
        return True
    except:
        return False

def main():
    # Get the number of days
    while True:
        try:
            num_count = int(input('How many random numbers do you want? '))
            if digitCheck(num_count) == False or num_count < 0:
                raise ValueError
            
        except ValueError:
            print("Non numberrical value...Please enter again.")
        else:
        # Open a new file named sales.txt
            num_file = open('randomnum.txt', 'w')

            # Get the ammount of sales for each day and write
            # it to the file
            
            for count in range(1, num_count + 1):
                numbers = randint(0,100)

                
            # Write the sales amount to the file
                num_file.write(str(numbers) + '\n')

            # Close the file.
            num_file.close()
            print('Data written to randomnum.txt.')
            break

# Call the main function
main()
