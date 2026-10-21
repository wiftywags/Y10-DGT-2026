#Ask user for width and loop 
#until they enter a number that is more than 0
error = ("Please enter a number that is more than 0\n")

while True:

    try:
        # Ask user for a number
        width = float(input("Width: "))

        # Check the number is more than 0
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)