user_input = int(input("Enter the marks:"))
print(user_input)
if user_input>=90 and user_input<=100:
    print("Grade A")
elif user_input>=80 and user_input<=89:
    print("Grade B")
elif user_input>=70 and user_input<=79:
    print("Grade C")
elif user_input>=60 and user_input<=69:
    print("Grade D")
elif user_input>=0 and user_input<59:
    print("Grade F")
else:
    print("invalid input")