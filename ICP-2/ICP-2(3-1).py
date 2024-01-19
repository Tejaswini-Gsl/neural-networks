 
inches = []
centimeters = []
num = int(input("How many heights to input: "))

for i in range(num):
    inch = int(input("Enter height in inches: "))
    inches.append(inch)

for i in inches:
    cm_val = i * 2.54 
    centimeters.append(cm_val)

print(inches)
  
print(centimeters)
