#The user is going to input the numbers for rectangle 1 length and wight.
#The user will be asked again to input numbers for the wight and length of the second rectangle.
#Than it will be calculated.
#Than the final lines will show if recatngle one is greater than rectangle two or if they are the same.
#CTI-110 
#P3T1- Area of Rectangles 
#Alexis Navarro
#9/25/2019

length1 = int(input('Enter the length of rectangle 1: '))
wight1 = int(input('Enter the wight of rectangle 1: '))

length2 = int(input('Enter the length of rectangle 2: '))
wight2 = int(input('Enter the wight of rectangle 2 : '))

Area1 = length1 * wight1
Area2 = length2 * wight2

if Area1 > Area2:
    print('Rectangle 1 has the greater area.')

elif Area2 > Area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
    



 
