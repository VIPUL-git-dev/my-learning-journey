import random
n = random.randint(1,50)
guess = 1
a = -1
while a!=n:
    a = int(input("enter your guess : "))
    guess += 1
    if a>n:
        print("lower number please")
    
    else:
        print("higher number please")

print(f"the number is {n}and in {guess} attempts")