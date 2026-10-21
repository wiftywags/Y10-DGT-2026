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

keepGoing = ""
while keepGoing == "":
    width = numCheck("Width: ")
    height = numCheck("Hight: ")

    #calculate the area / perimiter

    area = 2 * (width + height)
    perimiter = width * height

    #output the area / perimiter

    print(f"\nThe perimiter of the fence is {area}")
    print(f"The area of the fence is {perimiter}")

    # ask the user if they want to keep going
    keepGoing = input("\nPress enter to keep going or any other key to quit.\n")

print("Thank you for using the area / perimiter calculator")