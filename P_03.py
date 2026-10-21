# Ask the user for thier name
username = input("What is your name? ")

# Ask the user for thier favorate number
favNum = int(input("What is your favourite number? "))

# Double half nad square the number
double = favNum * 2
half = favNum / 2
square = favNum * favNum
# Greet the user
print(f"\nHi {username}, your favourite number is {favNum}")
# Output the results 
print(f"Double {favNum} is {double}")
print(f"Half {favNum} is {half}")
print(f"{favNum} squared is {square}")
print()
print("Have a nice day")
