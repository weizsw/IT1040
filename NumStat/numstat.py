import statistics

def getSum(coverted_numbers):
    summation = 0
    for number in converted_numbers:
        summation += number
        #summation = summation + number
    return summation

def getCount(converted_numbers):
    count = 0
    for number in converted_numbers:
        count += 1
        #count = count + 1
    return count
def getLines(converted_numbers):
    num_lines = len(converted_numbers)
    return num_lines

def getAverage(converted_numbers):
    sumn = getSum(converted_numbers)
    avg = sumn/getLines(converted_numbers)
    return avg

def getMax(converted_numbers):
    _max = 0
    for i in converted_numbers:
        if i >= _max:
            _max = i
    return _max

def getMin(converted_numbers):
    _min = 9999
    for i in converted_numbers:
        if i <= _min:
            _min = i
    return _min

def getRange(converted_numbers):
    _max = getMax(converted_numbers)
    _min = getMin(converted_numbers)
    _range = _max - _min
    
    return _range
    
while (True):
    

    try:
        number_file_name = input("Enter the name of the file you would like to process: ")
        number_file = open(number_file_name, "r")
        unconverted_numbers = number_file.readlines()
        converted_numbers = []
        for number in unconverted_numbers:
            try:
                number = int(number)
                converted_numbers.append(int(number))
            except ValueError:
                converted_numbers.append(float(number))

        number_file.close()

    # If there's a problem reading the file, print an error
    except Exception as err:
        print ('An error occurred reading', number_file_name)
        print ('The error is', err)
        
    else:
        # Print the calculated statistics
        if getLines(converted_numbers) == 0:
            print ('Empty file ->', number_file_name)
            break
        print("File name:", number_file_name)
        print("Sum:", getSum(converted_numbers))
        print("Count:", getCount(converted_numbers))
        print("Average:", getAverage(converted_numbers))
        #+ ' %.1f' % 
        print("Maximum:", getMax(converted_numbers))
        print("Minimum:", getMin(converted_numbers))
        print("Range:", getRange(converted_numbers))
        _max = getMax(converted_numbers)
        _min = getMin(converted_numbers)
        if _max <= 100 and _min >= 0:
            _a = 0
            _b = 0
            _c = 0
            _d = 0
            _f = 0
            for i in converted_numbers:
                if i > 90:
                    _a+=1
                elif i > 80 and i < 90:
                    _b+=1
                elif i > 70 and i < 80:
                    _c+=1
                elif i > 60 and i < 70:
                    _d+=1
                else:
                    _f+=1
            print("Grade Distribution:")
            print("A's:", _a)
            print("B's:", _b)
            print("C's:", _c)
            print("D's:", _d)
            print("F's:", _f)

        calculate_again = input("Would you like to evaluate another file? (y/n) ")
        if (calculate_again != "y"):
            break


