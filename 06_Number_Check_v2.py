# This is the code that base on what I have done before in Movie Funderaiser Program

def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))

            if response < low:
                print("Too Cold!!")
            else:
                return response
            
        except ValueError:
            print("Please enter a number")

# main routine goes here
while True:
    number = temp_check(-273)

    print("You chose {}".format(number))

