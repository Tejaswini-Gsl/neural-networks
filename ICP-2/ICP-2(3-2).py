inches = []
num = int(input("How many heights to input: "))

for i in range(num):
    inch = int(input("Enter height in inches: ")) 
    inches.append(inch)

centimeters = [inch * 2.54 for inch in inches]  


print(inches)   
print(centimeters)
