print ("Hello, World!")


a=2 
b=7 
sum=a+b
print("The sum of", a, "and", b, "is", sum)
print ("The product of", a, "and", b, "is", a*b)
print ("The difference of", a, "and", b, "is", a-b)
print ("The quotient of", a, "and", b, "is", a/b)


#this is a single line comment 
x=5 # this is a another single line comment
print(x)


import math # this is an import statement
print(math.sqrt(25)) # this is a function call
print(math.pow(2, 3)) # this is a function call
print(math.factorial(5)) # this is a function call
print(math.perm(5, 3)) # this is a function call


list1 = [1, 2, 3, 4, 5] # this is a list
list1[1] = 10 # this is a list element assignment
print(list1)
#remember that lists are mutable, we can change the value of a list element


tuple1 = (1, 2, 3, 4, 5) # this is a tuple
print(tuple1)
# for remembering tuples are immutable, we cannot change the value of a tuple element


dict = {'name': 'vipul', 
        'age': 20} # this is a dictionary}
#always remember that dictionaries are mutable, we can change the value of a dictionary element
dict['age'] = 21 # this is a dictionary element assignment
print(dict)
print(dict.get('name')) # this is a dictionary element access
(dict.update({'age': 22})) # this is a dictionary element updateS
print(dict)


set1 = {1, 2, 3, 4, 5} # this is a set
print(set1)
# remember that sets are mutable, we can add or remove elements from a set
set1.add(6) # this is a set element addition
print(set1)
set1.remove(2) # this is a set element removal
print(set1)
#in set we cannot have duplicate elements and also we cannot have index of elements in set
#that means dublicate items are not counted in set and also we cannot access the elements of set by index


print(7 // 3) # this is a floor division operator
print(7 % 3) # this is a modulus operator
print(2 ** 3) # this is an exponentiation operator
print(7 > 3) # this is a comparison operator
print(7 < 3) # this is a comparison operator
print(7 == 3) # this is a comparison operator
print(7 != 3) # this is a comparison operator
print(7 >= 3) # this is a comparison operator
print(7 <= 3) # this is a comparison operator
print(7 and 3) # this is a logical operator
print(7 or 3) # this is a logical operator
print(not 7) # this is a logical operator
print(7 is 3) # this is an identity operator
print(7 is not 3) # this is an identity operator



 #starting with if else statements
age = 20 # this is a variable
if age >= 18:
     print("You are an adult.")
else:
     print("You are not an adult.")


a = 5
if a > 0:# this is an if statement
     print("a is positive.")

else:# this is an else statement
     print("a is negative.")


marks = 85
if marks >= 90: # this is an if statement
     print("Grade: A")
elif marks >= 80: # this is an elif statement
     print("Grade: B")
elif marks >= 70: # this is an elif statement
     print("Grade: C")
else: # this is an else statement
     print("Grade: D")


if age >= 18 and age <= 65: # this is an if statement with logical operators
     print("You are an adult.")
     if age < 18 or age > 65: # this is an if statement with logical operators
         print("You are not an adult.")


marks = 89
if marks >=90:
    print("O")
elif marks == 89:
    print("A")
elif marks >= 80:
    print("B")
elif marks >=60:
    print("C")
elif marks >=40:
    print("D")
else:
    print("F")


marks1 =99
marks2=67
if marks1 >=90:
    print('very good')
if marks2 >=90:
    print("very good ")
else:
    print ("not good")


a = int(input("Enter a number: ")) # this is an input statement
b = int(input("Enter another number: ")) # this is an input statement
if a > b: # this is an if statement
   print(a, "is greater than", b) # this is a print statement inside the if statement
elif a < b: # this is an elif statement
   print(a, "is less than", b) # this is a print statement inside the elif statement
else: # this is an else statement
   print(a, "is equal to", b) # this is a print statement inside the else statement


a=int(input("enter your number1:"))
b=int(input("enter your number2:"))
print("your number is ",a>b)


a=int(input("enter your number1:"))
b=int(input("enter your number2:"))
print("number average is",(a+b)/2)


name = "vipul"
namespace1 = name[0:4] # this is a string slicing
print(namespace1) # this is a print statement
character1 = name[0]
print(character1)


#this is slicing with skip value 
#best topic 
soum = "soumantyperstyle"
a = soum[1:9]
print(a)
b = a[0:3]
print(b)
c = b[1:3]
print(c)
d = soum[1:12:4]
print(d)


a = "amazing"
print (a[1:7:2])
print (a[:4])
print (a[2:])
print (a[1:4])


a="vipul"
print (a[-4:-1])


name = "vipul"
print (len(name))
print (name.endswith("pul"))
print (name.startswith("vip"))


# this is use to give new line in between
a= "vipul is a good boy \n but not a bad\t \"boy\"" # we have also escape sequence character is there 
print(a)



# we can print this using f string 
name = input("Enter your name :")
print (f"GOOD EVENING  {name}" )

#here you can make chain
letter ='''dear <|name|>
you are selected 
<|date|>
'''
print (letter.replace ("<|name|>", "vipul").replace("<|date|>","1 dec 2007"))
  


#here you can find double space in between line 
name = "my name is vipul  ok "
print (name.find("  "))



# to remove double space we have 
name = "my  name is  vipul  ok "
print (name.replace("  "," ")) 
# note that strings are immutable you cannot change them by any functions


#we can add in list by this 
contents = ['apple','banana',34,274.2]
contents.append("vipul")
print (contents)
# if we want to print to contents 1 or 2 then
print (contents[1:3])
print (contents[0])


# if we have to arrange our list then we have 
l1=[3,23,24,81,5,9,11]
l1.sort()
l1.insert(3,643735)
l1.reverse()
print (l1)


# i am making a program which can make a list according to which you can type
fruits =[]
f1 = input("enter your fruit name :")
fruits.append(f1)
f2 = input("enter your fruit name :")
fruits.append(f2)
f3 = input("enter your fruit name :")
fruits.append(f3)
print (fruits)


# now we have to sort our marks then
Marks = []
f1 = int(input("enter your Marks here :"))
Marks.append(f1)
f2 = int(input("enter your Marks here :"))
Marks.append(f2)
f3 = int(input("enter your Marks here :"))
Marks.append(f3)
Marks.sort()
print (Marks)


#for sum for a list elements 
del sum
l = [1,4,9,6]
print (sum(l))


#for count anything we can use
a = [7,3,53,56,0,0,0,0,0,0,0,0,0,0,0,0,0,65]
n = a.count(0)
print (n)


# dictionary in python 
marks ={
    "vipul":99,
    "rohan":78,
    "anuj":45 
}
print (marks ,type(marks))
print (marks.items()) 
print (marks.values())
print (marks.keys())
marks.update ({"vipul":"73%"}) 
marks.update({"shiv":77})
print (marks)

#print (marks.get("vipu")) # i changed the value so that it gives me none 
#print (marks["vipu"]) # but when i change value of this i get error 


# to make a empty set we dont use e = {} rather than its get dictionary so we use 
e= set() # this is an empty set 


# here we have sets and we are getting union and intersection
s1 = {1,3,4,5,4,87}
s2 = {2,3,35,5}
union = (s1.union(s2))
intersection = (s1.intersection(s2))
print (union)
print (intersection)


# now i am going to make dictionary in which we get disired output 
dict = {
    "kursi":"chair",
    "so ja":"sleep now",
    "banda":"man"
}
dic = input("enter your word :")
print (dict[dic])


#if we have to add something in the list
l=[1,2,3,4,5]
a= l.append(323)
print (l)


s1= {3,21232342,2234,234,23,"hreshewh"}
s2 ={3,41351,"opllly_665"}
c = s1.union(s2)
v= s1.intersection(s2)
print(c)
print(v)


# if we have to print our set with desired number
s = set()
n = int(input("ENTER YOUR NUMBER:"))
s.add(n)
n = int(input("ENTER YOUR NUMBER:"))
s.add(n)
n = int(input("ENTER YOUR NUMBER:"))
s.add(n)
n = int(input("ENTER YOUR NUMBER:"))
s.add(n)
n = int(input("ENTER YOUR NUMBER:"))
s.add(n)
n = int(input("ENTER YOUR NUMBER:"))
s.add(n)
n = int(input("ENTER YOUR NUMBER:"))
s.add(n)
n = int(input("ENTER YOUR NUMBER:"))
s.add(n)

print (s)


# if we print 18 as int and as string 
a = set()
a.add(18)
a.add("18")
print (a)


#if we have to make dictionary 
d ={}
name = input("Enter your name:")
language = input("enter your language:")
d.update({name : language})

name = input("Enter your name:")
language = input("enter your language:")
d.update({name : language})

name = input("Enter your name:")
language = input("enter your language:")
d.update({name : language})

name = input("Enter your name:")
language = input("enter your language:")
d.update({name : language})

print (d)


#if we have to take our marks values up right
marks = int(input("enter your marks"))

if (marks>=90):
    print("excellent good job bache ")
elif (marks==80):
    print("very good")
elif (marks>80):
    print("very good keep it up")
else:
    print ("you are not eligible for this")


#defining your age with if else 
a = int(input("Enter your age:"))

#1st condition
if (a%2 ==0):
    print("your age  is  in even")



#2nd condition
if (a>=18):
    print("you are above the consent")

else:
    print("you are below the consent")

#3rd condition
if (a>=13 and a<=19):
    print ("you are in teenage")

elif (a>=20):
    print("you are adult")

elif (a<=12):
    print ("you are a child")


#number checking which is bigger which user want to type
a1 = int(input("ENTER YOUR NUMBER:1 "))
a2 = int(input("ENTER YOUR NUMBER:2 "))
a3 = int(input("ENTER YOUR NUMBER:3 "))
a4 = int(input("ENTER YOUR NUMBER:4 "))

if (a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1: ",a1)
elif (a2>a1 and a2>a3 and a2>a4):
    print("greatest number is a2: ",a2)
elif (a3>a2 and a3>a1 and a3>a4):
    print("greatest number is a3: ",a3)
elif(a4>a2 and a4>a3 and a4>a1):
    print("greatest number is a4: ",a4)



#checking passing of a child
marks1 = int(input("Enter your sub1 marks:"))
marks2 = int(input("Enter your sub2 marks:"))
marks3 = int(input("Enter your sub3 marks:"))

total_percentage = (marks1+marks2+marks3)/3

if (total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print ("you passed the exam",total_percentage)

else:
    print ("you failed and better luck next time",total_percentage)



#spam detector in commment in any video 
p1= "make lot of money"
p2= "click here"
p3= "surprise for you"
message = input("Enter your comment")
if (p1 in message or p2 in message or p3 in message):
    print("this is spam")
else:
    print("this is comment")



#username valid or not 
username = input("Enter your username : ")
if (len(username)<5):
    print("invalid for this")
else:
    print ("valid ")



#checking name in list 
l = ["vipul","saksham","sameer","aham sahota"]
name = input("ENTER YOUR NAME:")
if(name in l):
    print("your name is in the list pleASE come inside",name)
else:
    print ("go outside")



#checking the post and also taking to lower post to compare 
post = input("Enter your post:")

if ("vipul" in post.lower()):
    print("this post is for vipul")
else:
    print("sorry")


#starting with loops lets start 
i = 1
while(i<6):
    print(i)
    i+=1


#printing name 5 times 
i=0
while i < 5 :
     print("vipul")
     i=i+1


# while loops in strings 
s = "vipul"
i = 0
while (i<len(s)):
    print(s[i])
    i=i+1



#using while lopps 
l = [1,"jatt","sam","college","going ","morning"]
i=0
while (i<len(l)):
    print(l[i])
    i=i+1


#using for loops in list 
l = [1,3,4,56,57,686,7]
for i in l:
    print(i)


#using for loops in tuple
t=(33,3,232,23,2,3)
for i in t:
    print(i)

#using for loops in string
s = "vipul"
for i in s:
    print(i)


for i in range(0, 80):
    print(i)
    if i == 3:
        break



for i in range(4):
    print("printing")
    if i == 2:
        continue 
    print(i)



#password checker working loop
password = ""
while password != "secret123":
    password = input("enter your password")

print ("access granted")



# in this we can make a table of any number which user want to type
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}") # f string is used to format the output nicely
# # The old way (harder to read and write)
#      print(n, "x", i, "=", n * i)



# in this type user can type thier desired number and also the range in which they want to print the table of that number
n= int(input("Enter a number: "))
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
for i in range(a, b+1):
    print(f"{n} x {i} = {n*i}")



#in this we can print hello to the name which starts with s and goodbye to the name which does not starts with s
l = ["vipul", "saksham", "sameer", "aham sahota"]
for name in l:
    if name.startswith("s"):
       print(f"hello {name}")
    else:
         print(f"goodbye {name}")



#this is a program to print the multiplication table of a number using while loop
n = int(input("Enter a number: "))
i=1
while (i<11):
    print(f"{n} x {i} = {n*i}")
    i+=1



#this is a program to check whether a number is prime or not
n= int(input("enter your number:"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")



#this is a program to find the sum of first n natural numbers using while loop
n = int(input("enter your number:"))
i=1
sum=0
while (i<=n):
    sum+=i
    i+=1
print(sum)


n = int(input("enter your number:"))
sum = 0
for i in range(1,n+1):
    sum+=i
    print(sum)


count = 0
for i in range(1, 20, 3):
    if i % 2 == 0:
        continue
    if i > 14:
        break
    count += 1
print(count)

#this is a program to find the factorial of a number using for loop
n = int(input("enter your number:"))
product = 1
for i in range(1,n+1):
    product*=i
print(f"factorial of {n} is {product}")



#this is a program to print a pyramid of stars
n = int(input("enter your number:"))
for i in range (1 , n+1):
    print ("  "*(n-i), end="")
    print ("*"* (2*i-1), end="")
    print ("")

n= int(input("enter your number :"))
for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("+"*(2*i-1),end="")
    print("")

n= int(input("enter your number :"))
for i in range (1,n+1):
    print(""*(n-1),end="")
    print("+"*(2*i-1),end="")
    print("")  


# #this is a program to print a diamond of stars
n = int(input("enter your number:"))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")
for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")



#this is a program to find the average of two numbers using function
def avg():
    a = int(input("Enter your number1:"))
    b = int(input("Enter your number2:"))
    print("number average is",(a+b)/2)
avg()
avg()



def avg(a,b):
    return (a+b)/2
print(avg(5, 10))


def func():
    i=1
    while i in range (1,6):
        print(i)
        i+=1
func()



def goodday(name,ending):
    print("good day,"+ name )
    print(ending)
goodday("vipul","bye")
goodday("saksham","bye")


def goodday(name):
    print("goodday,"+name )
goodday (input("enter your name "))



#this is a program to find the factorial of a number using recursion
def factorial(n):
    if (n==1 or n==0):
        return 1 
    return n * factorial(n-1)

n = int(input("enter a number "))
print(f"the factorial of number is :{factorial(n)}")



#this is a program to find the greatest of three numbers using function
def greatest (a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b 
    elif c>a and c>b:
        return c 
a = int(input("enter your number "))
b = int(input("enter your number "))
c = int(input("enter your number "))
print (greatest(a,b,c))



#this is a program to convert fahrenheit to celsius using function
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter your number :"))
c = f_to_c(f)
print (f"{round(c, 2)}")


#this is a program to find the sum of first n natural numbers using recursion
def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n
n = int(input("enter your number :"))
print(sum(n))


#to print a pattern of stars using recursion
def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n-1)
n = int(input("enter your number :"))
pattern(n)


#this is a program to convert inches to centimeters using function
def inch_to_cm(inches):
    return inches * 2.54
print("Enter the length in inches:")
inches = float(input())
print(f"The length in centimeters is: {inch_to_cm(inches)}")



#calculator app 
x = int(input("Enter a number1 : "))
u = input("enter operator (+,-,*,/)")
w = int(input("enter your number 2: "))

if u =='+':
    print(f"result = {x + w}")
elif u == '-':
    print (f"result = {x - w}")
elif u == '*':
    print (f"result = {x * w}")
elif u == '/':
    print (f"result = {x / w}")



def linux(name,end):

    print('goodday,'+name)

    print(end)

linux('vipul','bye')



def recursion(n):
    if n == 0:
        return
    print("*" * n)
    recursion(n-1)
n = int(input("enter your number :"))
recursion(n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter your number :"))
print(factorial(n))



# this is file read 
f  = open("file.txt") 
data = f.read()
print(data)
f.close()

#this is file write
wri = "hey hello"
f = open ("file.txt", "w")
data = f.write(wri)
print(data)
f.close()


#this is make file in list format 
f = open("file.txt")
lines = f.readlines()
print (lines,type(lines))
f.close()


#this is to print the file line by line by while loop
f = open("file.txt")
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
f.close()


f = open("file.txt")
with open("file.txt") as f:
    data = f.read()
    print(data)


# this is a program to check if a word is present in a file or not
f = open("file.txt")
content = f.read()
if ("question" in content):
    print("yes content is there in the file")
else:
    print("no content is not there in the file")  
f.close()


#to enter text in file 
a = input("enter your text to enter in file: ")
f = open("file.txt",'w')
data = f.write(a)
f.close()


def generatetable(n):
    table = ""
    for i in range (1,11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables/table{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generatetable(i)


#making points game with highscore 
import random
def game():
    print("you are playing the game..")
    score = random.randint(1,62)
    with open ("highscore.txt") as f:
        highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"your score is {score} and highscore is {highscore}")
    if score > highscore:
        with open ("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()


#for change the word to another 
word = "donkey"
with open("file.txt","r") as f:
    content = f.read()

newcontent = content.replace(word,"####")

with open("file.txt","w") as f:
    f.write(newcontent)


with open("file.txt","w")as f:
    f.write("i am vipul and learning programming")



class employee:
    company = "google"
    language = "python"
    salary = 140000

vipul = employee()
rohan = employee()

print(vipul.company,vipul.language,vipul.salary)
print(rohan.salary,rohan.language)



class employee1:
    salary = 120000
    language = "c++ "

    def __init__(self):#this is a constructor which is called when an object is created
        print("employee is created")

    def getinfo(self):#this is a method which is called when we want to get the information of the employee 
        print(f"the salary is {self.salary} and his language is {
            self.language}")

vipul = employee1()

vipul.language = "python"

print(vipul.salary,vipul.language)

vipul.getinfo()




class employee1:
    salary = 120000
    language = "c++ "

    def __init__(self,salary,language):
        self.salary = 130000
        self.language = "python"

vipul = employee1("language","salary")

print(vipul.salary,vipul.language)



class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, language, pincode):
        self.name = name
        self.salary = salary
        self.language = language
        self.pincode = pincode

p = programmer("vipul",13000,"python",176204)
print (p.name,p.language,p.salary,p.pincode)
r = programmer("rohan",140000,"java",112818)
print (r.name,r.language,r.salary,r.pincode)



# this is a program to make a calculator class which can calculate square, 
# cube and cuberoot of a number
class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube (self):
        print(f"the  cube is {self.n*self.n*self.n}")
    def cuberoot (self):
        print(f"the cuberoot is {self.n**(1/3)}")

    @staticmethod #this is use to greet or use for print something 
    def hello():
        print("hello there!")

    
a = calculator(int(input("enter your number:")))
a.hello()
a.square()
a.cube()
a.cuberoot()


#building logic for attributes
class vip:
    a = 3

o =vip()
print(o.a)#here class attribute prints
(o.a) = 0 #setted the instance attribute 
print(o.a)#here instance attribute prints as which is setted
print(vip.a)# here we get from class directly 




# making a train ticket booking system using class and object oriented programming
from random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print (f"your ticket is booked in {self.trainNo}from {fro} to {to}")

    def getStatus(self):
        print(f"train no {self.trainNo} running on time ")

    def fare(self , fro , to):
        print(f"ticket fare in train no :{self.trainNo} from {fro} to {to} is {randint(100,500)}")

t = train(int(input("enter your train number:")))
t.book(input("enter your from station:"),input("enter your to station:"))
t.getStatus()
t.fare(input("enter your from station:"),input("enter your to station:"))



#inheritance in OOPS
class employee:
    company = "imu"
    language = "python"

class programmar(employee):
    company = "itc infotwech"

a = employee()
b = programmar()

print(a.company,b.company,b.language)




class emplo:
    def __init__(self):
        print("hey hello me emplo")
    a = 6

class coder(emplo):
    def __init__(self):
        print("hey hello me coder")
    b = 9

class programme(coder):
    def __init__(self):
        super().__init__()# here we used super method to print its parent constructor
        print("i am programme")
    c= 8


o = emplo()
q = coder()
m = programme()
print(o.a)
print(q.b)
print(m.c)
print(m.a) 



#using class method in python
class emplo:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class value is {cls.a}")

e = emplo()
e.a = 23
e.show()



