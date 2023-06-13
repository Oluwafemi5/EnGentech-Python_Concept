def shape():

    try:

        dent = int(input("Enter an odd number$ "))

        if dent % 2 == 0:

            print("== Invalid, only odd numbers are allowed ==")

            shape()

        else:

          space = 0

          for x in range(dent, 0, -2):

                print("  " * space + "* " * x)

                space = space + 1

          top_space = int(dent/2)

          for x in range(1, dent, 2):

                print("  " * top_space + "* " * x)

                top_space = top_space - 1

    except ValueError:

        print("== Only Odd integers are allowed ==")

    shape()

shape()

