user_input= input("enter python input:")
user_input= list(user_input)
del user_input[3:5]
reversed_string = ''.join(reversed(user_input))
print(reversed_string)


