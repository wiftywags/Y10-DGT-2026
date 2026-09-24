# hello there
# Noah
# 23 Sept 2026
# Version 2 


# TODO: check and reord inputs
#       checking for valid answer
#       


#Version 1
'''
like_coffee = input("Do you like coffe? ")
# print(like_coffee) # checking the input is stored
print(f"Your anser was '{like_coffee}'")

# Ask if they like coffe and respond
if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee == "Y":
    print("That is great <3<3<3<3")
else:
    print("You are missing out! why not give it a try?")'''

#Version 2
# Wheile loop to test the program
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like Coffe? ")
    # print(like_coffee) # checking the input is stored
    print(f"Your anser was '{like_coffee}'")

    if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee == "Y":
        print("That is great <3<3<3<3")
        keep_going = "Exit"
    elif like_coffee == "No" or like_coffee == "no" or like_coffee == "n" or like_coffee == "N":
        print("You are missing out! why not give it a try?")  
        keep_going = "somthing_Else"
    else:
        print("Nuh uh uh.")

    
