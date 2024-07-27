#Function that calculates square footage of a house
def HouseSquareFeet():
    """Function that calculates square footage of a house."""
    length = float(input("What is the length of the house? "))
    width = float(input("What is the width of the house? "))
    area = length * width
    print(f"The house you are measuring is {area} square feet.")

HouseSquareFeet()


#Function that calculates the circumference of a circle
def CircleCircumference():
    """Function that calculates the circumference of a circle - using diameter oriented formula."""
    diameter = float(input("What is the diameter of the cirle you are trying to find the area of?: "))
    circumference = diameter * 3.14159
    print(f"The circumference of the cirle you are measuring is {circumference}.")

CircleCircumference()
    
