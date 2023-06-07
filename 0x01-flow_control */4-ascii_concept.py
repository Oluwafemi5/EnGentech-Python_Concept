def check(char):

    while True:

        if len(char) != 1:

            print("Not more than one character at a time, pls try again")

        elif not char.isalpha():

            print("None alphabetical character is  allowed, please try again")

        else:

            if char.lower() == char:

                return "lower"

            else:

                return "upper"

        char = input("Enter a single character: ")



character = input("Enter a single character: ")

result = check(character)

print(f"The character is {result}")

