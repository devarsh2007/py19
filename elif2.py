print("---------------------------------------")
print("enter 1 for addition")
print("enter 2 for substraction")
print("enter 3 for multiplication")
print("enter 4 for division")
print("---------------------------------------")

choise = int(input("enter a number : "))

a=int(input("enter a : "))
b=int(input("enter b : "))

if choise==1:
      print("addition : ",a+b)
      
elif choise==2:
      print("substraction : ",a-b)
      
elif choise==3:
      print("multiplication : ",a*b)
      
elif choise==4:
      print("division : ",a/b)
      
else:
      print("invalid input")