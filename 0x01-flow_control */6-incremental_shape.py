while True:

    try:

        num = int(input("Type a number: "))

    except ValueError:

        print("Only integer character is allowed, try again")

        continue

    break

for i in range(num):

    print("#"*(i+1))
