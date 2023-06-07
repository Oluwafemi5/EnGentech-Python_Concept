def tt(number):

    print(number, 'x', count, '=', number * count)

number = int(input ("Enter the number: "))

print("The Multiplication Table of: ", number)

for count in range(1, 13):

    tt(number)
