
print ("welcome to expence tracker , so you can know that how much does total costs ")
d = input("what is the event: ")
a = int(input("what is the cost of one item:  "))
b = int(input("how many items are there:  "))
c = int(input("how many persons are there:  "))

totalcost = a*b*c
priceperperson = totalcost/c
print(f"The total cost for the {d} is {totalcost}")
print(f"The cost per person for the {d} is {priceperperson}")