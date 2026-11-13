import random
you1 = input("enter your choice out of s,w,g: ")
computer = random.choice([-1,1,2])

dict = {
    's':-1,
    'w':1,
    'g':2
}
dict2 = {
    -1:'snake ',
    1:'water',
    2:'gun'
}
you = dict[you1]

game = (f"you chosen {dict2[you]}, computer chosen {dict2[computer]}")


if you == -1 and computer ==1:
    print("you lose")
elif you == 1 and computer ==2:
    print("you lose")
elif you == 2 and computer == -1:
    print("you win")
elif you == computer:
    print("draw")
elif you == -1 and computer ==2:
    print("you lose")
elif you == 1 and computer == -1:
    print("you lose")
elif you == 2 and computer ==1:
    print("you lose")

else :
    print ("something went wrong")

print (game)