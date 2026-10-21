#Ask user for width and loop 
#until they enter a number that is more than 0

def numCheck(question):

    error = ("Please enter a number that is more than 0\n")
    while True:

        try:
            # Ask user for a number
            response = float(input(question))

            # Check the number is more than 0
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


#Main routiene goes here
for item in range(0, 2):

    width = numCheck("width: ")
    print(width)


print()

for item in range(0, 2):

    hight = numCheck("Hight: ")
    print(hight)