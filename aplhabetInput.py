def inputAlphabetOnly(name):
    while True:
        user_input=input(name)
        if user_input.isalpha():
            return user_input
        else:
            print("Invalid input")

 name=inputAlphabetOnly("Enter your name: ")
 print(f"Hello, {name}!")