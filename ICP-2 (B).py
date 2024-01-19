def string_alternative(full_name):
    return full_name[::2]

def main():
    input_str = "Good evening"
    result = string_alternative(input_str)
    print(result)

if __name__ == "__main__":
    main()
