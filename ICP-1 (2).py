import re 

user_input= input("enter python input:")
print(user_input)
user_input = re.sub(r'\b'+'python'+r'\b','pythons',user_input)
# user_input= user_input.replace('python','pythons')
print(user_input)