import math

print("This program calculates the volume of")
print("a cylinder given radius and height")

#Input
r = input("What is the radius") #When inputs are taken it is assumed they are strings
r = float(r)                    #Casting r to a float and storing the result in r

h = float(input("What is the height: "))

#Process
#Volume = PI*radius^2*height

v = math.pi*r*r*h


#Output

print("END PROGRAM")