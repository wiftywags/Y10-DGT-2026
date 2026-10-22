# Ask the user for a width and hight
# (asume they put valid data)

width = float(input("Width: "))
height = float(input("Height: "))

#calculate the area / perimiter

area = 2 * (width + height)
perimiter = width * height

#output the area / perimiter

print(f"\nThe perimiter of the fence is {area}")
print(f"The area of the fence is {perimiter}")