print('Ludo game ')

pick=['toss','quit']

while True:

    name=input("pick either toss or quit\t")

    if name not in pick:

          print("Invalid input") 

    elif name in pick:

           print("Program ends ")

           break
