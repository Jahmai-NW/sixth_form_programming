#SUBROUTINE
def volume(radius, height):
    from math import pi
    volume = (pi * (radius * radius) * height)
    return volume

#MAIN PROGRAM
radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))
print("The volume of this cylinder is", volume(radius, height))
