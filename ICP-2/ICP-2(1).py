import string_alternative as st

def fullname(a,b):
    Full_name = a+" "+b
    return (Full_name)
def main():

    First_name= input("Enter first name:")
    last_name= input("enter last name:")
    Full_name= fullname(First_name,last_name)
    print(Full_name)
    result = st.string_alternative(Full_name)
    print(result)

if __name__ == "__main__":
    main()
